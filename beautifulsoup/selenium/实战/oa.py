#!/usr/bin/evn python
#-*- coding:utf-8 -*-

"""
测试oa自动写周报
"""


import time 
from selenium import webdriver
from getpass import getpass



def write_content(content=""):
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="mainFrame"][id="mainFrame"]'))
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="tabcontentframe"][id="tabcontentframe"]'))
    driver.switch_to.frame(driver.find_element_by_id("ueditor_0"))
    driver.find_element_by_css_selector("html>body").send_keys(content)
    driver.switch_to.default_content()   #  退出刚刚进入的iframe框架
    pass

def write_question(question=""):
    # 遇到的问题
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="mainFrame"][id="mainFrame"]'))
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="tabcontentframe"][id="tabcontentframe"]'))
    driver.switch_to.frame(driver.find_element_by_id("ueditor_1"))
    driver.find_element_by_css_selector("html>body").send_keys(question)
    driver.switch_to.default_content()    

    pass


def write_plan(plan=""):
    # 下周计划
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="mainFrame"][id="mainFrame"]'))
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="tabcontentframe"][id="tabcontentframe"]'))
    driver.switch_to.frame(driver.find_element_by_id("ueditor_2"))
    driver.find_element_by_css_selector("html>body").send_keys(plan)
    driver.switch_to.default_content()    



if __name__ == "__main__":

    import sys

    args = sys.argv
    user =  args[1]
    passwd = args[2]
    content = args[3]
    question = args[4]
    plan = args[5]

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://oa.novogene.com/login/Login.jsp?gopage=&_token_=c8fe74ed-57dd-4d99-8276-f85cc3b794d4")
    # driver.switch_to.alert().accept()

    # OA登陆
    driver.find_element_by_id("loginid").clear
    driver.find_element_by_id("loginid").send_keys(user)
    driver.find_element_by_id("userpassword").send_keys(passwd)
    driver.find_element_by_id("login").click()
    time.sleep(5)

    # 点击周报按钮
    driver.find_element_by_css_selector('.topMenuDiv div div[title="周报"]').click()
    time.sleep(5)
    driver.find_element_by_css_selector('ul li div a[title="填写周报"] div span span').click()
    time.sleep(5)

    write_content(content)
    write_question(question)
    write_plan(plan) 

    # 保存
    driver.switch_to.frame(driver.find_element_by_css_selector('iframe[name="mainFrame"][id="mainFrame"]'))
    driver.find_element_by_css_selector('div div div div div div div span input').click() 
    driver.switch_to.default_content()   #  退出刚刚进入的iframe框架

    # 关闭窗口
    driver.quit()
    