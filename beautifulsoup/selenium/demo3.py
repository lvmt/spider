#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/") 
time.sleep(3)
driver.find_element_by_id("kw").send_keys("selenium")   # 百度输入框叫做： kw
driver.find_element_by_id("su").click()                 # 百度搜索点击按钮叫： su

time.sleep(3)  # 休眠3秒browser.quit()

# 把页面title打印出来，检查是否出错
print(driver.title)

driver.quit()  # 退出浏览器 ， 退出并关闭窗口的每一个相关的驱动程序


# browser.close() #  关闭当前窗口 ，用哪个看你的需求了。


# 添加休眠， 让浏览器跑慢点 time
# time.sleep() 函数随意插，哪里太快插哪里，再也不用担心看不清脚本的运行过程了。

"""
其实，这个函数的真正用途不是给我们看脚本的运行过程的，有时候网络原因，或页面加载慢。假设搜索框输入框输入了selenium ，
搜索按钮还没加载出来，那么脚本就报错。在适当的位置加入time.sleep()有助于减少网络原因造成的脚本执行失败；
"""
