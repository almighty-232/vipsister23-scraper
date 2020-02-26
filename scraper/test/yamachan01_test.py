import unittest
from scraper import yamachan01
from bs4 import BeautifulSoup as bs


class TestScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sc = yamachan01.Scraper()
        cls.test_url = 'https://yamachan01.com/blog-entry-11681.html'
        cls.url_regex_pattern = 'https://blog-imgs-[0-9]+.fc2.com/y/a/m/yamachan01/[0-9a-z/]+.jpg'

    def test_get_imges_from_url(self):
        title, imgs = self.sc.get_imges_from_url(self.test_url)
        self.assertGreater(len(imgs), 0)
        for img in imgs:
            self.assertRegex(img, self.url_regex_pattern)
        self.assertTrue('https://blog-imgs-103.fc2.com/y/a/m/yamachan01/20190720070419cb4.jpg' in imgs)
        self.assertTrue('https://blog-imgs-103.fc2.com/y/a/m/yamachan01/20190720070157169.jpg' in imgs)


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
