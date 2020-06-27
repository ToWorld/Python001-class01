# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from spiders.items import SpidersItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        cookie = {
            "__mta": "119806007.1593107842173.1593161979973.1593161980009.10",
            "uuid_n_v": "v1",
            "uuid": "4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C",
            "_csr": "f61d9a8c249a5f79121e023b66d09dbe7b9686863d566aadb34ea3d63665ba07",
            "mojo-uuid": "cba42ebfbac7499726e6f55dac5fb937",
            "_lxsdk_cuid": "172eca072f0c8-0134bf7889df4-31617402-13c680-172eca072f1c8",
            "_lxsdk": "4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C",
            "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2": "1593171654,1593174010,1593189473,1593228626",
            "mojo-trace-id": "4",
            "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2": "1593228965", 
            "__mta": "119806007.1593107842173.1593161980009.1593228965406.11",
            "_lxsdk_s": "172f3d3885e-182-eff-2e8%7C%7C5"
        }
        yield scrapy.Request(url=url, callback=self.parse, cookies=cookie)

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
