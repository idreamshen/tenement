# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem


class GanjiSpider(scrapy.Spider):
    name = "ganji"
    allowed_domains = ["3g.ganji.com"]
    start_urls = [
        'http://3g.ganji.com/hz_fang1/wenxin/h3m1o1/',
        'http://3g.ganji.com/hz_fang1/wenxin/h3m1o2/',
        'http://3g.ganji.com/hz_fang1/wenxin/h3m1o3/'
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="list-items"]'):
            item = TenementItem()
            item['title'] = sel.xpath('.//div[1]/text()').extract_first().strip()
            item['href'] = 'http://3g.ganji.com' + sel.xpath('./a/@href').extract_first().split('?', 1)[0]
            item['price'] = sel.xpath('.//div[5]/text()').re(r'\d+')[0]
            yield item
