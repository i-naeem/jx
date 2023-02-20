from jx.items import JobItem
from datetime import date
import scrapy


SELECTORS = {
    "title": '//td[contains(., "Hiring Organization")]//following-sibling::td//text()',
    "company": '//td[contains(., "Jobs Location")]//following-sibling::td//text()',
    "deadline": '//td[contains(., "Valid Through")]//following-sibling::td//text()',
}


class JobustadSpider(scrapy.Spider):
    name = 'jobustad'
    allowed_domains = ['www.jobustad.com']

    def start_requests(self):
        year, month, day = str(date.today()).split('-')
        url = f"https://www.jobustad.com/{year}/{month}/{day}/"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield from response.follow_all(css="h2.entry-title a", callback=self.parse_post)

        next_page = response.css('a.next-page::attr(href)').get()

        if next_page is not None:
            yield response.follow(url=next_page, callback=self.parse)

    def parse_post(self, response):
        item = JobItem()
        item['source'] = response.url
        item['title'] = response.xpath(SELECTORS.get('title')).get()
        item['company'] = response.xpath(SELECTORS.get('company')).get()
        item['deadline'] = response.xpath(SELECTORS.get('deadline')).get()

        return item
