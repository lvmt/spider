#!/usr/bin/env python
#-*- coding:utf-8 -*-


from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.cn")

# 定位到要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
