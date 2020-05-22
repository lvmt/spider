#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from selenium import webdriver


driver = webdriver.Firefox()

# 访问百度首页

first_url = "http://www.baidu.com"
print("now access {first_url}".format(**locals()))
driver.get(first_url)

time.sleep(3)

# 访问新闻网页
second_url = "http://news.baidu.com"
print("now access {second_url}".format(**locals()))
driver.get(second_url)

time.sleep(3)

# 返回（后退）到百度首页
print("back to {first_url}".format(**locals()))
driver.back()

time.sleep(3)

# 前进到新闻页
print("forward to {second_url}".format(**locals()))
driver.forward()

time.sleep(3)

driver.quit()
