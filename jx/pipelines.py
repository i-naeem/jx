from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CompanyFilterPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('company'):
            return item
        else:
            raise DropItem(f"Missing price in {item.get('source')}")
