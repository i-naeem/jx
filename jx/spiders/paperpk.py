from datetime import date
import scrapy


class PaperPKSpider(scrapy.Spider):

    name = "paperpk"
    allowed_domains = ["paperpk.com"]

    def start_requests(self):
        today = date.today()
        url = f"http://paperpk.com/calendar-search.php?req={today}"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('//div[@id="job-table"]//tr[count(.//td)=3]')

        for row in rows:
            yield {
                "company_name": row.css('a#company_sub_link::text').get(),
                "post_title": row.css('td a:first-of-type::text').get()
            }
