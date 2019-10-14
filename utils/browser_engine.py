from selenium import webdriver
from utils.configparam_util import ConfigEngine
import os

"""
浏览器驱动引擎
"""


class BrowserEngine(object):
    @classmethod
    def get_driver(self):
        driver = None
        # 获取配置文件浏览器参数
        # file_path = os.path.dirname(os.path.abspath("."))+"/MySelenium/config/env.ini"
        file_path = os.path.dirname(os.path.abspath("."))+"/config/env.ini"
        browser_name = ConfigEngine.get_param(file_path,"browserType","browserName")
        # 根据参数启动对应浏览器驱动
        if browser_name == "Chrome":
            driver = webdriver.Chrome()
        elif browser_name == "Firefox":
            driver = webdriver.Firefox()
        elif browser_name == "Ie":
            driver = webdriver.Ie()
        return driver


