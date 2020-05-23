#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
目的：

从前程无忧网站上提取指定工作的详细信息
"""


import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup



def get_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # response.apparent_encoding = "utf-8"
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
    except:
        print("爬取失败")
    return soup


def get_content(soup):
    content = soup.find("div", class_="bmsg job_msg inbox").text
    # print(content)
    return content.strip()
    

def final_result(url):
    soup = get_soup(url)
    result = get_content(soup)
    return result


# 登陆
driver = webdriver.Firefox()
driver.get("https://login.51job.com/login.php?lang=c") 

driver.find_element_by_id("loginname").send_keys("13554221497")
driver.find_element_by_id("password").send_keys("lmt921108")
driver.find_element_by_id("login_btn").click()
print("登陆中，请稍等。。。")
time.sleep(20)

# 返回首页
print("进入首页。。。")
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/p/a[1]").click()
time.sleep(5)
# 添加多个地区
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/p[2]/em").click()
driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_180200"]').click()
driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()

# 搜索job
print("搜索职位。。")
driver.find_element_by_id("kwdselectid").send_keys("生物信息工程师")
driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/button").click()
time.sleep(20)


# 获取内容
all_list = driver.find_element_by_id("resultList").find_elements_by_class_name("el")

for item in all_list[1:]:
    jobname = item.find_element_by_class_name("t1").find_element_by_tag_name("a").text
    jobhref = item.find_element_by_class_name("t1").find_element_by_tag_name("a").get_attribute("href") 
    jobskill = final_result(jobhref)
        
    company = item.find_element_by_class_name("t2").text
    site = item.find_element_by_class_name("t3").text
    money = item.find_element_by_class_name("t4").text
    date = item.find_element_by_class_name("t5").text 
    
    out_dict = {
        "职位": jobname,
        "职位要求": jobskill,
        "职位详细信息": jobhref,
        "招聘公司": company,
        "工作地点": site,
        "薪水": money,
        "发布日期": date
    }
    
    print(out_dict)

# print(len(all_list))