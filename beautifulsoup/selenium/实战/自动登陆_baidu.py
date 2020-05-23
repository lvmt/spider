#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from selenium import   webdriver


driver = webdriver.Firefox()
driver.get("https://www.baidu.com/") 

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/a[2]").click()

time.sleep(5)  # 设置时间缓冲，网速过慢的话，会出现错误
driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()


driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("13554221497")
driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("lmt921108") 

driver.find_element_by_id("TANGRAM__PSP_11__submit").click()