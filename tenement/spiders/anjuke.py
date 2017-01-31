# -*- coding: utf-8 -*-
import scrapy
import json
from tenement.items import TenementItem


class AnjukeSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["anjuke.com"]
    start_urls = [
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b2-0-0-f0/?page=1',
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b2-0-0-f0/?page=2',
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b2-0-0-f0/?page=3',
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b3-0-0-f0/?page=1',
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b3-0-0-f0/?page=2',
        'http://m.anjuke.com/hz/rentlistbypage/xihu/a0_0-b3-0-0-f0/?page=3'
    ]

    def parse(self, response):
        res = json.loads(response.body)

        for info in res['datas']['list_info']:
            item = TenementItem()
            item['title'] = info['title']
            item['href'] = info['prop_url']
            item['price'] = info['price']

            yield item

