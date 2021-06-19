# -*- coding: utf-8 -*-
import scrapy
from ettoday_project.items import EttodayProjectItem  #從ettoday_project引用items.py的EttodayProjectItem類別


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'   #要執行的爬蟲名稱
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm',
                  'https://www.ettoday.net/news/20201009/1826868.htm']

    def parse(self, response):
        item = EttodayProjectItem() 
        item['title'] = response.xpath('//title/text()').get()    #對應items.py中EttodayProjectItem類別裡的Field()方法
        item['content'] = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        yield item