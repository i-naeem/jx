# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    title = scrapy.Field()
    source = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    last_date = scrapy.Field()
    image_urls = scrapy.Field()
