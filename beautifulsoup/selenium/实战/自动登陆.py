#!/usr/bin/env python
#-*- coding:utf-8 -*-


from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://accounts.douban.com/passport/login") 
driver.find_element_by_class_name("account-tab-account").click()

driver.find_element_by_id("username").send_keys("13554221497")
driver.find_element_by_id("password").send_keys("123123qqq")

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a").click()