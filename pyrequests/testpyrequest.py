import HtmlTestRunner
import unittest
import requests


class TestPyRequest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://api.douban.com'
    def test_douban_api(self):
        r = requests.get(self.url+'/v2/movie/top250',verify=False)
        self.assertTrue(r.status_code,200)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.'))