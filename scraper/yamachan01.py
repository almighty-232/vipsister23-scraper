# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup as bs

from .master import ScrapeWebsite

"""
master.py
execute by `run()` and it returns page's title and including images
"""


class Scraper(ScrapeWebsite):
    basic_url = r'https://yamachan01.com/'

    def get_title(self, obj: bs) -> str:
        return obj.body.h2.text

    def get_files(self, obj: bs) -> list:
        img_list = list()
        for item in obj.findAll('div', {'class':'textBody'}):
            inners = item.select('img')
            if inners:
                for inner in inners:
                    url = inner['src']
                    pattern = 'https://blog-imgs-[0-9]+.fc2.com/y/a/m/yamachan01/[0-9a-z/]+.jpg'
                    if re.match(pattern, url):
                        img_list.append(url.replace('s.jpg', '.jpg'))
        return img_list


if __name__ == '__main__':
    print(Scraper().get_imges_from_url('http://vipsister23.com/archives/9564543.html'))
