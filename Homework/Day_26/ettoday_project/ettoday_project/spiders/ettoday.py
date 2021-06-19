# -*- coding: utf-8 -*-
import scrapy
from ettoday_project.items import ScrapyDemoItem  #爬蟲專案名稱 #items.py #引用裡面的類別


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm',
                  'https://www.ettoday.net/news/20201009/1826868.htm']

    def parse(self, response):
        item = ScrapyDemoItem()    #使用類別
        item['title'] = response.xpath('//title/text()').get()   #使用類別下的方法
        item['content'] = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()  #使用類別下的方法
        yield item