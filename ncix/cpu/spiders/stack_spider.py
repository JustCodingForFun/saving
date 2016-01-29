from scrapy import Spider
import scrapy
from scrapy.selector import Selector
from stack.items import StackItem
from common.string_op import StringOp


class StackSpider(Spider):
    name = "ncix"
    allowed_domains = ["http://www.ncix.com"]
    start_urls = [
        "http://http://www.ncix.com/categories/",
    ]

    def parse(self, response):
        href = Selector(response).xpath('//a[contains(@href, "category")]/@href').extract()

        for url in href:
            yield scrapy.Request(url, self.parse_subcat)

    def parse_subcat(self, response):
        products_urls = response.xpath('//span[@class="listing"]/a/@href')
        for url in products_urls:
            yield scrapy.Request(url, self.parse_item)

    def parse_item(self, response):
        regular_price = StringOp.get_price(response.xpath('//*[@id="div_price"]').re(r'regular price of(.*)'))
        price = StringOp.get_price(response.xpath('//*[@id="div_price"]').re(r'itemprop="price">\s*(.*)'))
        url = response.url
        if 'intel' in url:
            specifications = response.xpath('//div [@class="productdetaildiv"]/table').extract()

            item = StackItem()
            item['url'] = url
            yield item

    def get_processor_number(self, specification):
        # pl = re.findall('\d+\.\d+', specification)

    def get_socket(self, specification):
        pass

    def get_frequency(self, specification):
        pass

    def get_core_thread(self, specification):
        pass