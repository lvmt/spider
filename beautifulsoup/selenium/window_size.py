#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
set_window_size() 控制浏览器大小
"""

import time
from selenium import webdriver



driver = webdriver.Firefox()
driver.get("http://m.baidu.com") 

print("设置浏览器宽480，高800显示")
# driver.set_window_size(480, 800)
driver.maximize_window()    # 全屏显示
time.sleep(3)

driver.quit()



# 全屏显示 maximize_window() 