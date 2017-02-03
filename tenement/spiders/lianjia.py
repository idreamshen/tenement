# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["m.lianjia.com"]
    start_urls = [
        'https://m.lianjia.com/hz/zufang/wenjiao/pg1',
        'https://m.lianjia.com/hz/zufang/wenjiao/pg2',
        'https://m.lianjia.com/hz/zufang/wenjiao/pg3',
    ]

    def parse(self, response):
        for sel in response.xpath('//li[@class="pictext"]'):
            item = TenementItem()
            item['title'] = sel.xpath('.//div[@class="item_list"]/div[1]/text()').extract_first().strip()
            item['href'] = 'https://m.lianjia.com' + sel.xpath('./a/@href').extract_first()
            item['price'] = sel.xpath('.//div[@class="item_list"]/div[@class="item_minor"]/div[2]').re(r'\d+')[0]
            yield item
