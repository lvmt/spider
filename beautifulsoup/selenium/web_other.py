#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id("kw").size 
print(size)


# 返回百度页面底部备案信息
text = driver.find_element_by_id("s-bottom-layer-right").text
print(text) 

# 返回元素的属性值, 可以是id，name，type或者其他
attribute = driver.find_element_by_id("kw").get_attribute("type")
print(attribute)


# 返回元素的结果是否可见
result = driver.find_element_by_id("kw").is_displayed()
print(result)


time.sleep(8)

driver.quit()











# size = 255
# text = 