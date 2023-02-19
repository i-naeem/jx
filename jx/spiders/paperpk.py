import scrapy


class PaperpkSpider(scrapy.Spider):
    name = "paperpk"
    allowed_domains = ["paperpk.com"]
    start_urls = ["http://paperpk.com/"]

    def parse(self, response):
        pass
