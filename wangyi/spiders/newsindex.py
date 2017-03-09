# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from ..items import WangyiItem

class NewsindexSpider(scrapy.Spider):

    name = "newsindex"
    allowed_domains = ["newindex.com"]
    start_urls = ['http://news.163.com/special/0001386F/rank_news.html']


    def parse(self, response):
        itemList = response.css('.tabContents.active td >a::text').extract()
        data = []
        for item in itemList:
            # print item
            temp = WangyiItem()
            temp['title'] = item
            data.append(temp)
        # inspect_response(response,self)
        return data

