# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import scrapy


class JobItem(scrapy.Item):
    source = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    deadline = scrapy.Field()


class JobItemLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
