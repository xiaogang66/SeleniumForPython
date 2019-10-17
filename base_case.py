
from base_manager import BaseManager
import unittest
from base_page import BasePage

class BaseCase(unittest.TestCase,BaseManager):

    base_page = BasePage()
    @classmethod
    def setUpClass(cls):
        """执行用例前回到首页，同时每个入口记录类名"""
        cls.logger = cls.get_logger()
        cls.logger.info("-----执行用例类：" + cls.__name__)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        """每个入口记录方法名"""
        self.logger.info("-----执行用例方法：" + self._testMethodName)

    def tearDown(self):
        pass