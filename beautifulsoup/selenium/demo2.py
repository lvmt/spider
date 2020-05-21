#!/usr/bin/env python
#-*- coding:utf-8 -*-


from selenium import webdriver
import re 
import time
import os

print("start >>>>")

# 打开firefox浏览器 ，
driver = webdriver.Firefox()

#定位节点
url = "https://www.qiushibaike.com/text/" 

driver.get(url)
content = driver.find_element_by_css_selector("div.content")
print(content.text)