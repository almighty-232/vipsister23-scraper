import unittest
from scraper import vipsister23
from bs4 import BeautifulSoup as bs


class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sc = vipsister23.Scraper()
        cls.test_url = 'http://vipsister23.com/archives/9564571.html'
        cls.url_regex_pattern = 'https://livedoor.blogimg.jp/vipsister23/imgs/[0-9a-z/]+.jpg'

    def test_get_imges_from_url(self):
        title, imgs = self.sc.get_imges_from_url(self.test_url)
        self.assertGreater(len(imgs), 0)
        for img in imgs:
            self.assertRegex(img, self.url_regex_pattern)

    def test_get_title(self):
        html = f'<html>' \
               f'<head>Test</head>' \
               f'<body>' \
                f'<h2>Title</h2>' \
               f'</body>' \
               f'</html>'
        obj = bs(html, 'html.parser')
        res = self.sc.get_title(obj)
        self.assertIsInstance(res, str)
        self.assertGreater(len(res), 0)
