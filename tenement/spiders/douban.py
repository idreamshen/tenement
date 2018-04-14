# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["www.douban.com"]
    city = 'hangzhou'
    urls = {
        'hangzhou': [
            'https://www.douban.com/group/145219/discussion',
            'https://www.douban.com/group/HZhome/discussion'
        ],
        'shanghai': [
            'https://www.douban.com/group/shanghaizufang/discussion',
            'https://www.douban.com/group/homeatshanghai/discussion',
            'https://www.douban.com/group/shzf/discussion',
            'https://www.douban.com/group/zufan/discussion'
        ]
    }

    def __init__(self, city=None, *args, **kwargs):
        super(DoubanSpider, self).__init__(*args, **kwargs)
        print('请求查询城市为', city)
        if city in self.urls:
            self.city = city
        print('最终查询城市为', self.city)

        for url in self.urls[self.city]:
            for i in range(5):
                self.start_urls.append(url + "?start=" + str(i * 25))

    def parse(self, response):
        for sel in response.xpath('//td[@class="title"]/a'):
            item = TenementItem()
            item['title'] = sel.xpath('./@title').extract_first()
            item['href'] = sel.xpath('./@href').extract_first()
            item['price'] = 0

            if any(str_ in item['title'] for str_ in ("2室", "两室", "三室", "3室")):
                yield item
