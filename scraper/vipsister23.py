# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

from .master import ScrapeWebsite

"""
master.py
execute by `run()` and it returns page's title and including images
"""


class Scraper(ScrapeWebsite):
    def get_title(self, obj: bs) -> str:
        return obj.body.h2.text

    def get_files(self, obj: bs) -> list:
        img_list = list()
        for item in obj.findAll('div', {'class':'t_b'}):
            inners = item.select('a')
            if inners:
                for inner in inners:
                    img_list.append(inner['href'].replace('-s', ''))
        return img_list


if __name__ == '__main__':
    print(Scraper().get_imges_from_url('http://vipsister23.com/archives/9564543.html'))
