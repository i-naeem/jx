from scrapy.loader import itemloaders
from jx.items import JobItem
from datetime import date
import scrapy


class PaperPKSpider(scrapy.Spider):

    name = "paperpk"
    allowed_domains = ["paperpk.com"]

    def start_requests(self):
        today = date.today()
        url = f"http://paperpk.com/calendar-search.php?req=2023-02-19"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//div[@id="job-table"]//tr[count(.//td)=3]'):
            title = row.xpath('./td/a').get()
            url = row.xpath('./td/a/@href').get()
            company = row.xpath('./td/a[@id]').get()
            location = row.xpath('./td/a[contains(@href,"/city/")]').get()

            meta = dict(title=title, company=company, location=location)
            yield scrapy.follow(url=url, callback=self.parse_post, meta=meta)

    def parse_post(self, response):
        loader = itemloaders(item=JobItem(), response=response)

        loader.add_value('title', response.meta.get('title'))
        loader.add_value('company', response.meta.get('company'))
        loader.add_value('location', response.meta.get('location'))
        loader.add_xpath('image_urls', './/img[@id=img_path]/@src')

        yield loader.load_item()
