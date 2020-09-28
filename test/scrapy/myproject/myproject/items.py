# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Headline(scrapy.Item):
    title=scrapy.Field()
    body =scrapy.Field()


class Restaurant(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    # latitude = scrapy.Field()
    # longitude = scrapy.Field()
    station = scrapy.Field()
    score  = scrapy.Field()


class Page(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def __repr__(self):
        p = Page(self)
        if len(p["conetnt"]>100):
            p["content"] = p["content"][:100]+"..."
        return super(Page, p).__repr__()

