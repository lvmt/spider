#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''爬取小说昆仑
'''

import requests
from bs4 import BeautifulSoup
import time
import multiprocessing
from multiprocessing import Pool


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

class SpiderKun(object):
    
    def __init__(self,url):
        self.url = url
        
    
    def get_html(self,url):
        try:
            res = requests.get(url, headers=headers, verify=False)
            res.encoding = res.apparent_encoding 
            return res.text  
        except Exception as e:
            return None
        
    def get_soup(self,html):
        try:
            soup = BeautifulSoup(html,'html.parser')
        except:
            soup = BeautifulSoup(html, 'xml')
        return soup
        
    
    def start(self):
        '''开始爬取，爬取有内容的结果文件
        '''
        html = self.get_html(self.url)
        soup = self.get_soup(html)
        
        kunlun = open('kun.txt', 'w',encoding='utf-8')
        head = soup.select('div.dirtitone') 
        content = soup.select('div.clearfix') 
        
        dd = dict(zip(head, content))
        
        for k,v in dd.items():
            title = k.text 
            print('\033[1;32m开始爬取大单元 {}\033[0m'.format(title))
            kunlun.write(title + '\n')
            if dd[k].select('li'):
                li_list = v.select('li')
                for li in li_list:
                    t1 = li.text
                    kunlun.write(t1 + '\n')
                    print('\033[1;34m开始爬取小单元 {}\033[0m'.format(t1))
                    href = 'https://www.xiaoshuodaquan.com' + li.a['href']
                    html = self.get_html(href)
                    soup = self.get_soup(html)
                    text = soup.select('div.page-content')[0].text
                    kunlun.write(text)
                    time.sleep(3)
            time.sleep(3)
                    
        
        
if __name__ == '__main__':
    
    p = Pool(3)
    
    url = 'https://www.xiaoshuodaquan.com/kunlun/' 
    
    # ss = SpiderKun(url)
    # ss.start()
    p.apply(SpiderKun(url).start, args=())
    p.close()
    p.join()
    
    