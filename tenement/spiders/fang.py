# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem


class FangSpider(scrapy.Spider):
    name = "fang"
    allowed_domains = ["m.fang.com"]
    start_urls = [
        'http://m.fang.com/zf/?purpose=%D7%A1%D5%AC&district=%CE%F7%BA%FE&comarea=%CE%C4%D0%C2&room=2&rtype=zz&city=%BA%BC%D6%DD&renttype=cz&c=zf&a=ajaxGetList&city=hz&page=1',
        'http://m.fang.com/zf/?purpose=%D7%A1%D5%AC&district=%CE%F7%BA%FE&comarea=%CE%C4%D0%C2&room=2&rtype=zz&city=%BA%BC%D6%DD&renttype=cz&c=zf&a=ajaxGetList&city=hz&page=2',
        'http://m.fang.com/zf/?purpose=%D7%A1%D5%AC&district=%CE%F7%BA%FE&comarea=%CE%C4%D0%C2&room=2&rtype=zz&city=%BA%BC%D6%DD&renttype=cz&c=zf&a=ajaxGetList&city=hz&page=3'
    ]

    def parse(self, response):
        for sel in response.xpath('//li/a'):
            item = TenementItem()
            item['title'] = sel.xpath('./div[@class="txt"]/h3/text()').extract_first().strip()
            item['href'] = 'http:' + sel.xpath('./@href').extract_first()
            item['price'] = sel.xpath('./div[@class="txt"]/p[1]/span/text()').re(r'\d+')[0]

            yield item
