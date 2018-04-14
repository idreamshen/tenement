# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TenementPipeline(object):
    def process_item(self, item, spider):
        print('链接=' + item['href'], '地址=' + item['title'], '价格=' + str(item['price']))
        return item
