# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealStateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    investment = scrapy.Field()
    investor = scrapy.Field()


