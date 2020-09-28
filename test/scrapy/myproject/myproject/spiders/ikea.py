from scrapy.spiders import SitemapSpider

class IkeaSpider(SitemapSpider):
    name="ikea"
    allowed_domains = ["www.ikea.com"]
    custom_settings = {#ここのsettingを怠ると504になる, あるいはsettings.pyでuser_agentを設定しなければならない
        'USER_AGENT':"ikeabot",
    }
    sitemap_urls = [
        "https://www.ikea.com/robots.txt"
    ]

    sitemap_follow = [
        r'prod-ja_JP',
    ]

    #urlのコールバック処理のルールリスト, ルールは(正規表現, 関数)で与える
    sitemap_rules = [
        (r'/products/', "parse_product")
    ]

    def parse_product(self, response):
        yield {
            "url":response.url,
            "name":response.css('#name::text').get().strip(),
            "type":response.css('#type::text').get().strip(),
            "price":response.css('#price1::text').re_first("[\S\xa0]+").replace('\xa0'," ")
        }