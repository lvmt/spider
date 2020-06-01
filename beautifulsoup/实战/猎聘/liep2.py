#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
from pprint import pprint
import time
from openpyxl import Workbook


class LiePin(object):

    def __init__(self,job):
        self.url = "https://www.liepin.com/zhaopin/?"
        self.job = job
        self.dict_list = []


    def get_html(self, url, data=None):
        """
        解析开始查询页： 第一页需要输入关键词
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
        }

        try:
            response = requests.get(url, params=data, headers=headers)
            print(response.url)
            if response.status_code == 200:
                return response.content
        except Exception:
            print("解析出现错误")
            self.get_html(url)
            

    def get_soup(self, html):
        try:
            soup = BeautifulSoup(html, 'lxml')
        except:
            soup = BeautifulSoup(html, 'html.parser')
        
        return soup


    def handle_one_page(self,soup):
        job_result = soup.select('.sojob-result ul.sojob-list')[0]   # soup 的select方法返回的是一个列表
        job_lists = job_result.select('li')

        for each_item in job_lists:
            print('*'*100)
            self.dict_list.append(self.handle_one_item(each_item))
            

    def handle_one_item(self,each_item):
        
        # 获取职位相关信息
        jobname = each_item.select('div[class="job-info"] h3')[0].get_text().strip()
        job_href =  each_item.select('div[class="job-info"] h3>a')[0].get('href')
        # 有的href存在问题，例如：/a/20486217.shtml， 这个时候，我们需要加上：https://www.liepin.com
        if job_href.startswith('/a'):
            job_href = 'https://www.liepin.com' + job_href
        ability_info = self.get_detail_ability_info(job_href)
        job_info = each_item.select('div[class="job-info"]>p')[0].get_text().strip().split("\n")
        money = job_info[0]
        site = job_info[1]
        edu = job_info[2]
        exp = job_info[3]
        date = each_item.select('div[class="job-info"] .time-info time')[0].get_text()

        # 获取公司相关信息
        company_info = each_item.select('div[class="company-info nohover"]>p')
        company_name = company_info[0].select('a')[0].get_text().strip()
        # company_class = company_info[1].select('span')[0].get_text().strip()
        company_class = company_info[1].get_text().strip()
        company_welfare = [item.get_text().strip() for item in company_info[-1].select('span') if item ]
        company_welfare = " ".join(company_welfare)

        job_info_dict = {
            "职位名称": jobname,
            '薪资统计': money,
            '工作点': site,
            '学历要求': edu,
            '工作经验': exp,
            '公司名称': company_name,
            '公司类型': company_class,
            '公司福利': company_welfare,
            '招聘详细链接': job_href,
            '岗位要求': ability_info,
            '招聘日期': date
        }

        pprint(job_info_dict)
        return job_info_dict


    def get_detail_ability_info(self, url):
        html = self.get_html(url)
        soup = self.get_soup(html)
        info_str = soup.select('.job-description>div')[0].get_text()
        return info_str

        
    def is_next_page(self,soup):
        print('\033[32m================== 开始打印下一页 ======================\033[0m')
        next_href = soup.select('.pagerbar>a')[-2].get('href')
        if next_href.startswith('/zhaopin'):
            next_url = 'https://www.liepin.com' + next_href
            return next_url

        print('达到最后一页了')
        return None

        
    def start(self):
        """
        先解析第一页，在解析后续页面
        """

        data = {
            'key': self.job
        }
        
        firt_html = self.get_html(self.url, data)
        soup = self.get_soup(firt_html)
        self.handle_one_page(soup)

        while self.is_next_page(soup):
            url = self.is_next_page(soup)
            html = self.get_html(url)
            soup = self.get_soup(html)
            self.handle_one_page(soup) 

            time.sleep(5)
        
        self.out_csv()


    def out_csv(self):
        wb = Workbook()
        ws = wb.create_sheet('招聘信息', index=0)

        for item_dict in self.dict_list:
            values = [value for value in item_dict.values()]
            ws.append(values)
        
        wb.save('猎聘_' + self.job + '.xlsx' )



if __name__ == "__main__":
    
    demo = LiePin('生物信息')
    demo.start()

