#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''提取pubmed上面的文献参考
'''

import requests
from bs4 import BeautifulSoup

import time


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}


class Pubmed(object):

    def __init__(self,args):
        self.args = args
        self.url = args['url']
        self.query = args['query']
        
        self.queryurl = ''


    def get_response(self,url,data=None):
        '''get response
        '''
        N = 1 # 最多允许重复测试10次
        try:
            response = requests.get(url,params=data,headers=headers)
            if response.status_code == 200:
                print('\033[1;32m响应码：200\033[0m')
                self.queryurl = response.url
                return response.text
            else:
                print(response.status_code)
        except Exception as e:
            if N < 10:
                print('\033[1;32m响应错误:{}'.format(e))
                print('\033[1;33m休息3秒,try again 第{}次\033[0m'.format(N))
                time.sleep(3)
                self.get_response(url)
                N += 1

    def get_soup(self,response):
        '''get beautifulsoup
        '''
        try:
            soup = BeautifulSoup(response,'html.parser')
        except:
            soup = BeautifulSoup(response, 'xml')
        return soup

    def parser_html(self,soup,pages=10):
        '''解析文档，使用css_select方法
        结果也每次展示10条信息,其他也面显示信息为查询url + &page=2
        默认爬取10页内容,少于10页信息，则全部爬取
        '''
        # get total items
        item_number = soup.select('.results-amount .value')[0].string
        item_number = int("".join(item_number.split(',')))

        # get total page
        total_page = int(item_number)/10 + 1

        if total_page < 10:
            pages = total_page            

        for page in range(pages):
            url = self.queryurl + '&page={}'.format(page)  # https://pubmed.ncbi.nlm.nih.gov/?term=WES&page=1
            response = self.get_response(url)
            soup = self.get_soup(response)

            results_list = soup.select('.search-results-list .full-docsum')
            for result in results_list:
                #title = result.select('.docsum-title')[0].text.strip()
                href = self.url.rstrip('?')+result.select('.docsum-title')[0]['href'] # 文献的完整链接
                # https://pubmed.ncbi.nlm.nih.gov/26742503/
                response = self.get_response(href)
                soup = self.get_soup(response)
                
                title = soup.select('div#full-view-heading>.heading-title')[0].text.strip()
                pmid = soup.select('div#full-view-heading .current-id')[0].text.strip()
                pmcid = soup.select('div#full-view-heading [class="identifier pmc"] .id-link')[0].text.strip()








        pass

    def start(self):

        data = {
            'term':self.query
        }

        # 查询页soup
        response = self.get_response(url,data)
        soup = self.get_soup(response)

        self.parser_html(soup)






data = {
    'term': 'WES'
}

url = 'https://pubmed.ncbi.nlm.nih.gov/?'


response = requests.get(url, params=data, headers=headers)

if response.status_code == 200:
    response.encoding = "utf-8"
    # with open('demo.html', 'w') as fw:
    #     fw.write(str(response.content))
    print(response.url)
else:
    print('\033[1;32m爬取失败\033[0m')

