# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
from test.test_class import TestMethod

# 设置报告名称
report_path = os.path.dirname(os.path.abspath('.')) + '/MySelenium/reports/'			#设置报告路径
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))		#获取当前时间
HtmlFile = report_path + now + " Report.html"
fp = open(HtmlFile, "wb")												#二进制写文件流

# 构建suite
suite = unittest.TestLoader().discover("case")

if __name__ =='__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner =  HTMLTestRunner.HTMLTestRunner(stream=fp,title='某某项目测试报告',description='描述信息')
    # 开始执行测试套件
    runner.run(suite)
    fp.close()