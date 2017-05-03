import scrapy
from bs4 import BeautifulSoup


class UpworkSpider(scrapy.Spider):
    name = 'upwork'
    start_urls = ['http://www.supercarros.com/carros',]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        print(soup)
