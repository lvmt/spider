#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from selenium import webdriver


driver = webdriver.Firefox()

# 访问百度首页

first_url = "http://www.baidu.com"
print("now access {first_url}".format(**locals()))

driver.get(first_url)


# 访问新闻网页



