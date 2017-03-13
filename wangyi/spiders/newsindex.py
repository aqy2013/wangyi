# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from ..items import WangyiItem
import re


class NewsindexSpider(scrapy.Spider):
    name = "newsindex"
    # allowed_domains = ["newindex.com"]
    start_urls = ['http://news.163.com/special/0001386F/rank_news.html']

    ''' 获取标题'''
    # def parse(self, response):
    #     itemList = response.css('.tabContents.active td >a::text').extract()
    #     data = []
    #     for item in itemList:
    #         # print item
    #         temp = WangyiItem()
    #         temp['title'] = item
    #         data.append(temp)
    #     # inspect_response(response,self)
    #     return data

    ''' 获取全部新闻链接url'''

    # def parse(self, response):
    #     itemList = response.css('.tabContents.active td >a::attr(href)').extract()
    #     data = []
    #     for item in itemList:
    #         # print item
    #         temp = WangyiItem()
    #         temp['link'] = item
    #         data.append(temp)
    #     #inspect_response(response,self)
    #     return data

    def parse(self, response):
        itemList = response.css('.tabContents.active td >a::attr(href)').extract()
        for item in itemList:
            print item
            yield scrapy.Request(item, callback=self.detail)

    def detail(self, response):
        temp = WangyiItem()
        # inspect_response(response,self)
        temp['title'] = response.css('.post_content_main > h1::text').extract_first()
        newtimestring = response.css('.post_content_main  .post_time_source::text').extract_first()
        temp['newstime'] = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', newtimestring).group()
        # newtimestring1 = response.css('.post_content_main  .post_time_source::text').extract()
        # temp['location'] = re.search('\((\w{1,})\)', newtimestring1).group()
        temp['desc'] = response.css('.post_content_main  .post_time_source #ne_article_source::text').extract_first()

        return temp
