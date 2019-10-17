from base_case import BaseCase
import unittest
import time

class TestBaidu(BaseCase):
    def test_aa(self):
        """测试登录"""
        self.logger.info("点击百度新闻")
        self.base_page.click(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[1]"))
        self.assertTrue(1==1,"测试用例执行失败")

    def test_bb(self):
        """测试退出"""
        self.base_page.back()
        self.logger.info("点击百度贴吧")
        self.base_page.click(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[5]"))
        self.assertTrue(1==2,"测试用例执行失败")
        time.sleep(2)

if __name__ == '__main__':
	unittest.main()