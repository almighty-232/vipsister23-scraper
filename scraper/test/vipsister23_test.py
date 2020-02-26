import unittest
from scraper import vipsister23
from bs4 import BeautifulSoup as bs


class TestScraper(unittest.TestCase):
    def test_get_imges_from_url(self):
        title, imgs = vipsister23.get_imges_from_url('http://vipsister23.com/archives/9564571.html')
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
        res = vipsister23.get_title(obj)
        self.assertIsInstance(res, str)
        self.assertGreater(len(res), 0)