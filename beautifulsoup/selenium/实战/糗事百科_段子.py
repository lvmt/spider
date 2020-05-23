#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time 
from selenium import webdriver 


"""
1. 获取一个标签就是：element
2. 获取多个标签就是：elements
"""


"""
获取标签文本：text
获取href属性值：href
"""


def get_text():
    content_list = driver.find_elements_by_class_name("main-list") 
    # print(content_list)

    for item in content_list:
        tm = item.find_element_by_class_name("fr").text
        title = item.find_element_by_class_name("title").text
        link = item.find_element_by_class_name("title").find_element_by_tag_name("a").get_attribute("href")
        text = item.find_element_by_class_name("content").text
        
        out_dict = {
            "发表时间": tm,
            "文章标题": title,
            "文章完整连接": link,
            "文章内容": text
        }
        
        print(out_dict)
    

def get_next():
    print("\033[32m开始进入下一页\033[0m")
    
    try:
        next_page = driver.find_element_by_class_name("next")
        next_page.click()
        return True
    except Exception as e:
        print("这是最后一页啦")
        return False
    
    
if __name__ == "__main__":
    driver =  webdriver.Firefox()
    driver.get("http://qiushidabaike.com/text_309.html") 
    get_text()
    time.sleep(2)


    while get_next():
        get_text()
    
    
    
