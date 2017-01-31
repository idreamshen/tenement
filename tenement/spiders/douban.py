# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["www.douban.com"]
    start_urls = [
        'https://www.douban.com/group/145219/discussion?start=0',
        'https://www.douban.com/group/145219/discussion?start=25',
        'https://www.douban.com/group/145219/discussion?start=50',
        'https://www.douban.com/group/145219/discussion?start=75',
        'https://www.douban.com/group/145219/discussion?start=100',
        'https://www.douban.com/group/145219/discussion?start=125',
        'https://www.douban.com/group/HZhome/discussion?start=0',
        'https://www.douban.com/group/HZhome/discussion?start=25',
        'https://www.douban.com/group/HZhome/discussion?start=50',
        'https://www.douban.com/group/HZhome/discussion?start=75',
        'https://www.douban.com/group/HZhome/discussion?start=100',
        'https://www.douban.com/group/HZhome/discussion?start=125'
    ]

    def parse(self, response):
        for sel in response.xpath('//td[@class="title"]/a'):
            item = TenementItem()
            item['title'] = sel.xpath('./@title').extract_first()
            item['href'] = sel.xpath('./@href').extract_first()
            item['price'] = 0

            if any(str_ in item['title'] for str_ in ("2室", "两室", "三室", "3室")):
                yield item
