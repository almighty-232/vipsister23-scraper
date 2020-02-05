import unittest
from vipsister23 import scraper
from bs4 import BeautifulSoup as bs


class TestScraper(unittest.TestCase):
    def test_get_imges_from_url(self):
        title, imgs = scraper.get_imges_from_url('http://vipsister23.com/archives/9564571.html')
        self.assertGreater(len(imgs), 0)
        for img in imgs:
            self.assertRegex(img, 'https://livedoor.blogimg.jp/vipsister23/imgs/[0-9a-z/]+.jpg')

    def test_get_title(self):
        html = f'<html>' \
               f'<head>Test</head>' \
               f'<body>' \
                f'<h2>Title</h2>' \
               f'</body>' \
               f'</html>'
        obj = bs(html, 'html.parser')
        res = scraper.get_title(obj)
        self.assertIsInstance(res, str)
        self.assertGreater(len(res), 0)