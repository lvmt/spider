#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
爬取猎聘上面的招聘信息
"""

from selenium import webdriver
import time
from pprint import pprint


class LiePin(object):
    
    def __init__(self,job,city):
        self.job = job
        self.city = city
        
        
    def start(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get('https://www.liepin.com/')
        
        # 
        driver.find_elements_by_css_selector('.search-main div.input-main input[name="key"]')[0].send_keys(self.job)
        driver.find_elements_by_css_selector('.search-btn')[0].click()
        time.sleep(5)
        
        # 选择地点， 默认是全国
        driver.find_elements_by_css_selector('.placeholder ~ em')[0].click()
        time.sleep(5)
        
        all_citys = driver.find_elements_by_css_selector('.data-list li a')
        target = None
        for city in all_citys:
            if city.text == self.city:
                target = city
                break
        
        if target is None:
            input(f'{self.city} 不在常见城市列表中，请手动选择，按回车键继续......')
        else:
            target.click()
            time.sleep(2)
            driver.find_element_by_css_selector('.vd-footer .vd-btn-ok').click()
            time.sleep(1)
        
        driver.find_element_by_css_selector('.input-main button').click()
        
        ## 输出打印查找到的工作信息
        self.handle_one_page(driver)
        
    def handle_one_page(self,driver):
        all_items = driver.find_elements_by_css_selector('.sojob-list li>div')
        
        for item in all_items:
            self.handle_one_item(item)
            
  
    def is_last_page(self):
        pass
    
    
    def handle_one_item(self,item):
        div1 = item.find_element_by_css_selector('div.job-info')
        div2 = item.find_element_by_css_selector('div.company-info')
        
        jobname = div1.find_element_by_css_selector('h3').text
        money = div1.find_element_by_css_selector('p span.text-warning').text
        site = div1.find_element_by_css_selector('p>a').text
        edu = div1.find_element_by_css_selector('p span.edu').text
        exp = div1.find_element_by_css_selector('p>span:nth-child(4)  ').text # 经验
        date = div1.find_element_by_css_selector('p>time').text
        
        company = div2.find_element_by_css_selector('p>a').text
        other = div2.find_element_by_css_selector('p:nth-last-child(1)').text 
        
        job_info = {
            '职位名称': jobname,
            '薪资': money,
            '工作地点': site,
            '学历要求':edu,
            '经验要求': exp,
            '发布日期': date,
            '招聘公司': company,
            '公司福利': other
        }
        
        pprint(job_info)
        

        
    
        
        
LiePin('生物信息', '武汉').start()
        
        
    