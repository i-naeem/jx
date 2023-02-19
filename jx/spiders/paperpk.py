"""paperpk.py - A scrapy spider to scrape https://paperpk.com"""
import scrapy


class PaperPKSpider(scrapy.Spider):
    """A scrapy spider that scrapes content from PaperPk"""
    name = "paperpk"
    allowed_domains = ["paperpk.com"]

    def start_requests(self):
        url: str = ""
        return scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
