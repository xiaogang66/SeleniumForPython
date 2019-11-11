# _*_ coding: utf-8 _*_


from utils.logger_util import Logger
from utils.browser_engine import BrowserEngine
import time
import unittest
import requests

class TestMethod(unittest.TestCase):
    def test_log_method(self):
        logger = Logger('TestMethod')
        logger = logger.get_logger_with_level(logger)
        logger.info("打开浏览器")

    def test_open_browser(self):
        test = BrowserEngine()
        driver = test.get_driver()
        driver.get("https://www.baidu.com")

# if __name__ == "__main__":
#     testmethodclass  = TestMethod()
#     # testmethodclass.test_log_method()
#     testmethodclass.test_open_browser();