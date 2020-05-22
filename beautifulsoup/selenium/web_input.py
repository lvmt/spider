#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from selenium import webdriver 

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(3)

driver.quit()