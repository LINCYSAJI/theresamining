import scrapy


class TheresaSpider(scrapy.Spider):
    name = "theresa"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ["https://www.mytheresa.com"]

    def parse(self, response):
        pass
