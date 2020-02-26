# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import re

import requests
from bs4 import BeautifulSoup as bs


class ScrapeWebsite(metaclass=ABCMeta):
    basic_url = None

    def url_checker(self, url: str):
        return None if re.match(f'{self.basic_url}.*', url) is None else self

    def get_imges_from_url(self, url: str):
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

        return self.get_title(bsobj), self.get_files(bsobj)

    @abstractmethod
    def get_title(self, obj: bs) -> str:
        pass

    @abstractmethod
    def get_files(self, obj: bs) -> list:
        pass


if __name__ == '__main__':
    pass

