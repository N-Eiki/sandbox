import scrapy
from myproject.items import Page
from myproject.utils import get_content

class BroadSpider(scrapy.Spider):
    name = "broad"
    start_urls = ["http://b.hatena.ne.jp/entrylist/all"]

    def parse(self, response):
        for url in response.css('.entrylist-contents-title > a::attr("href")').getall():
            yield scrapy.Request(url, callback=self.parse_page)
        url_more = response.css('.entrylist-readmore > a::attr("href")').re_first(r'.*\?page=\d(1)$')
        if url_more:
            yield response.follow(url_more)

    def parse_page(self, response):
        text = response.text
        # text.encoding = text.apparent_encoding
        title, content = get_content(text)
        # print('-----------------------')
        # print(title)
        # print(content)
        # print('-----------------------')
        yield Page(url=response.url, title=title, content=content)