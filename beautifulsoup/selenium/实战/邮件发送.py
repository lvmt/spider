#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
利用163邮箱发邮件
"""

import time
from  selenium import webdriver 
from getpass import getpass


def loging(user, passwd, reciver, subject, content):
    driver = webdriver.Firefox()
    driver.get("https://mail.163.com/") 
    driver.implicitly_wait(30)


    # 进入登陆iframe框架中
    driver.switch_to.frame(3)   # 这个不知道咋就对了， 无语了。。。 
    driver.find_element_by_name('email').clear()
    driver.find_element_by_name('email').send_keys(user)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(passwd)
    driver.find_element_by_id("dologin").click()
    driver.switch_to.default_content()   #  退出刚刚进入的iframe框架

    # 点击写信
    time.sleep(10)
    driver.find_elements_by_css_selector("div nav div ul li")[1].click()   # 写信
    time.sleep(20)
    driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys(reciver)
    driver.find_elements_by_css_selector("div section header div div div div input")[2].send_keys(subject)


    # 信的正文内容在iframe中
    driver.switch_to.frame(driver.find_element_by_class_name("APP-editor-iframe"))
    driver.find_element_by_css_selector("body").send_keys(content)
    driver.switch_to.default_content() 


    # 邮件发送
    driver.find_element_by_css_selector("div > header > div > div > div > span").click()
    
    # 关闭浏览器
    time.sleep(4)
    driver.quit()


if __name__ == "__main__":
    user = input("user: ")
    passwd = getpass()
    reciver = input("接收者: ")
    subject = input("主题: ")
    content = input("内容: ")
    
    loging(user, passwd, reciver, subject, content)
    
