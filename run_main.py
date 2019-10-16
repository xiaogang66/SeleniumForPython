# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
from utils.configparam_util import ConfigEngine
from base_manager import BaseManager
"""
    主入口运行类：执行用例并生成报告
"""


# 设置报告名称
report_path = os.path.dirname(os.path.abspath('.')) + '/SeleniumForPython/reports/'
#获取当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#设置报告路径
HtmlFile = report_path + now + " Report.html"
# 二进制写文件流
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("case")


if __name__ =='__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner =  HTMLTestRunner.HTMLTestRunner(stream=fp, title='某某项目测试报告', description='描述信息')

    # 打开网址
    baseUrl = ConfigEngine.get_param_default("testServer", "URL")
    base_manager = BaseManager()
    driver = base_manager.get_driver()
    driver.get(baseUrl)

    # 开始执行测试套件
    try:
        runner.run(suite)
    except Exception as result:
        print("存在执行用例出错：%s"% result)
    else:
        print("所有执行用例成功")
    finally:
        fp.close()
        # 关闭浏览器
        driver.close();


