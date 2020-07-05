# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from spiders.items import SpidersItem
from fake_useragent import UserAgent


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        header = {'User-Agent': UserAgent().random}
        yield scrapy.Request(url=url, callback=self.parse, headers=header)

    def parse(self, response):
        print(response.text)
        items = []
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        counter = 0
        for movie in movies:
            item = SpidersItem() 
            try:
                item['name'] = movie.xpath('./div[1]/span[1]/text()').extract()[0]
                item['tag'] = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip(' ').strip('\n')
                item['time'] = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip(' ').strip('\n')
                items.append(item)
            except:
                continue
            counter += 1
            if counter == 9:
                break
        return items
