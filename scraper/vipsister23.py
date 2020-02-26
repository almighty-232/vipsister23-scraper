# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

"""
scraper.py
execute by `run()` and it returns page's title and including images
"""


def get_imges_from_url(url: str):
    """

    :param url: str
        scraper's url
    :return: tuple
        page's title, image(list)
    """
    if not url:
        raise ValueError('url is empty')

    res = requests.get(url)
    if res.status_code != 200:
        raise requests.HTTPError
    # res.encoding = res.apparent_encoding
    bsobj = bs(res.text, 'html.parser')
    page_title = get_title(bsobj)

    img_list = list()
    for item in bsobj.findAll('div', {'class':'t_b'}):
        inners = item.select('a')
        if inners:
            for inner in inners:
                img_list.append(inner['href'].replace('-s', ''))

    return page_title, img_list


def get_title(obj: bs):
    return obj.body.h2.text


if __name__ == '__main__':
    print(get_imges_from_url('http://vipsister23.com/archives/9564543.html'))
