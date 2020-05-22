#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

search_text = driver.find_element_by_id("kw")
search_text.send_keys("selenium")
search_text.submit() 

time.sleep(5)

driver.quit()