from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter


from pymongo import MongoClient
class MongoPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['scraping-book']
        self.collection = self.db["items"]

    def close_spider(self, spider):
        self.client_close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

# class ValidationPipeline:
#     def process_item(self, item, spider):
#         if not item["title"]:
#             raise DropItem('missing title')
#         return item
