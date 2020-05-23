#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time  
from selenium import webdriver 


driver = webdriver.Firefox() 
driver.get("http://www.baidu.com") 

driver.find_element_by_id("kw").send_keys("美女")
driver.find_element_by_id("su").click()


# 截屏
time.sleep(10)   # 给浏览器渲染时间
driver.save_screenshot("截图_美女.png")

# 获取cookies
print(driver.get_cookies())

# 获取网页当前url
print(driver.current_url)

# 获取页面渲染之后的数据, 检查数据，返回的内容
print(driver.page_source)


# 退出浏览器
driver.quit()