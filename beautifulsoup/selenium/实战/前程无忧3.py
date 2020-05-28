#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
完全利用selenium爬取前程无忧信息
"""

from selenium import webdriver
import time 
from openpyxl import Workbook


  
class QianChen(object):
    
    def __init__(self,user,passwd,job,city):
        self.user = user
        self.passwd = passwd
        self.job = job
        self.city = city
        
    
    def run(self):
        """爬虫主函数 
        """

        # #新建了一个表格，尚未保存
        wb = Workbook()     
        ws = wb.create_sheet("工作信息", index=0)   #新建工作表，位置为第2个sheet
        rows = []

        # login
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://jobs.51job.com/")
        driver.find_element_by_css_selector('div > p > a').click()
        time.sleep(2)
        driver.find_element_by_id('loginname').send_keys(self.user)
        driver.find_element_by_id('password').send_keys(self.passwd)
        driver.find_element_by_id('login_btn').click()
        time.sleep(3)
        
        # 查询job
        driver.find_element_by_id('kwdselectid').send_keys(self.job)
        # 选择城市
        driver.find_element_by_id('work_position_input').click()
        time.sleep(3)
        # 先清除默认选择的城市
        default_citys = driver.find_elements_by_css_selector('#work_position_click_multiple_selected span')
        for city in default_citys:
            city.click()
        
        # 便利城市，看我们的选择是否在其中，
        city_elements = driver.find_elements_by_css_selector('#work_position_click_center_right tr em')
        target = None
        for city_ele in city_elements:
            if city_ele.text == self.city:
                target = city_ele
                break
        # 如果不在，需要手动输入
        if target is None:
            input(f'{self.city} 不在热门城市列表中，请手动点击选择城市后，按回车继续...')
        else:
            target.click()
            driver.find_element_by_id('work_position_click_bottom_save').click()
        time.sleep(2)
        driver.find_element_by_css_selector('#searchForm button').click()
        time.sleep(2)
    
        rows1 = self.one_page_info(driver)
        rows.extend(rows1)
        if self.last_page(driver):    
        # 获取每一页的信息
            rows2 = self.one_page_info(driver)
            rows.extend(rows2)
        rows.sort(key=lambda item:item['公司名称'])  # 对写出的结果按照公司名称进行排序
        
        for row in rows:
            row_values = [value for value in row.values()]
            ws.append(row_values)
        wb.save("前程无忧_{self.job}_{self.city}.xlsx".format(**locals()))
        
        
    def one_page_info(self, driver):
        """获取每一页的详细信息
        """
        rows = []
        jobs = driver.find_elements_by_css_selector('#resultList div[class="el"]')
        for job in jobs:
            fields = job.find_elements_by_css_selector('span')
            string_fields = [field.text for field in fields]
            
            job_info_dict = {
            '职位名称': string_fields[0],
            '公司名称': string_fields[1],
            '工作地点': string_fields[2],
            '薪资': string_fields[3],
            '发布时间': string_fields[4],
            '职位要求': None
            }
            
            # 获取每个职位的详细要求, 切换窗口
            main_window = driver.current_window_handle
            fields[0].click()
            driver.switch_to.window(driver.window_handles[-1])
            info = driver.find_elements_by_css_selector('.job_msg')
            if info and len(info) == 1:
                job_info_dict['职位要求'] = info[-1].text
                
            driver.close()
            driver.switch_to.window(main_window)

            # 将每一页的信息存入列表中
            rows.append(job_info_dict)
            print(job_info_dict)
        
        return rows
    
    
    def last_page(self, driver):
        """是否还有下一页
        """
        last_link = driver.find_elements_by_css_selector('div.dw_page  ul   li:nth-last-child(1) a')
        if last_link and len(last_link) == 1:
            last_link[-1].click()
            print("\033[32m开始爬取下一页......\033[0m")
            return True
        return False



        
QianChen('13554221497', 'lmt921108', '生物信息 ', '武汉').run()
                
                
        
        
        
    
    