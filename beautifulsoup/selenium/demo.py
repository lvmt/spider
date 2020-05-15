#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver    # 导入web驱动模块
driver = webdriver.Firefox()      # 创建驱动

driver.get("http://baidu.com") 

input = driver.find_element_by_css_selector("#kw")   # 获取输入框
input.send_keys("python教程")   # 输入搜索内容

button = driver.find_element_by_css_selector("#su")
button.click()


# 获取请求链接
print(driver.current_url)

# 获取cookie
print(driver.get_cookies())

# 获取源代码
# print(driver.page_source)

# 获取文本的值
# print(input.text)

