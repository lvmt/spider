#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
利用163邮箱发邮件
"""

import re
import time
from  selenium import webdriver 
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://mail.163.com/") 
driver.implicitly_wait(30)


# 进入登陆iframe框架中
driver.switch_to.frame(3) # 这个不知道咋就对了， 无语了。。。 
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys("13554221497")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("lmt921108")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()   #  退出刚刚进入的iframe框架



driver.find_elements_by_css_selector("div nav div ul li")[1].click()   # 写信
time.sleep(20)
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("lvmengting4480@novogene.com")
driver.find_elements_by_css_selector("div section header div div div div input")[2].send_keys("selenium 测试")


# 写信在iframe中
driver.switch_to.frame(driver.find_element_by_class_name("APP-editor-iframe"))
driver.find_element_by_css_selector("body").send_keys("hhhhhhh selenium 测试")
driver.switch_to.default_content() 


# 邮件发送
driver.find_element_by_css_selector("div > header > div > div > div > span").click()

# # time.sleep(4)
# # driver.quit()