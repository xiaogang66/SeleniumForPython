from base_case import BaseCase
import unittest
from base_manager import BaseManager

class TestBaidu(BaseCase):
    def test_aa(self):
        """测试登录"""
        self.logger.info("aaa")
        print(1)

    def test_bb(self):
        """测试退出"""
        self.logger.info("bbb")
        print(2)


if __name__ == '__main__':
	unittest.main()