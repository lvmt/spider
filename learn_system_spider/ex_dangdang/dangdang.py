#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''爬取当当网top500书籍
'''

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
class SpiderDangdang(object):
    
    def __init__(self,url):
        self.url = url
        
        
    def get_collection(self):
        '''将下载的数据存入mongodb数据库
        '''
        client = MongoClient('localhost', 27017)
        database = client.spider
        collection = database.dangdang
        return collection
    
            
    def get_response(self):
        try:
            response = requests.get(self.url,headers=headers)
            response.raise_for_status
            response.encoding = response.apparent_encoding
            return response.text 
        except Exception as e:
            print('aa',e)
            return 'None'
    
    
    def get_soup(self,response):
        try:
            soup = BeautifulSoup(response,'html.parser')
        except:
            soup = BeautifulSoup(response,'html.parser')
        return soup
    
    
    def get_items(self,soup):
        items = soup.select('div.bang_list_box>ul>li')
        return items
    
    
    def get_item_content(self,item):
        num = item.select('div.list_num')[0].text.strip()
        name = item.select('div.name')[0].text.strip()
        star = item.select('div.star')[0].text.strip()
        author = item.select('div.publisher_info')[0].text.strip()
        try:
            if item.select('div.price>p>span.price_n'):
                price_n = item.select('div.price>p>span.price_n')[0].text.strip()
            else:
                price_n = 'None'
        except:
            price_n = 'None'
            
        try:
            if item.select('div.price>p>span.price_r'):
                price_r = item.select('div.price>p>span.price_r')[0].text.strip()
            else:
                price_r = 'None'
        except:
            price_r = 'None'
            
        try:
            if item.select('div.price>p>span.price_s'):
                price_s = item.select('div.price>p>span.price_s')[0].text.strip()
            else:
                price_s = 'None'
        except:
            price_s = 'None'

        content = {
            '排名': num,
            '书名': name,
            '评分': star,
            '作者': author,
            '当前价格': price_n,
            '原价': price_r,
            '折扣': price_s
        }
        return content 
    
    
    def start(self):
        collection = self.get_collection()
        response = self.get_response()
        soup = self.get_soup(response)
        items = self.get_items(soup)
        for item in items:
            content = self.get_item_content(item)
            query = {'排名': content['排名']}
            if collection.find_one(query):
                print('\033[1;31m该item已经存在，不进行存储\033[0m')
            else:
                collection.insert_one(content)
                print('\033[1;32m该item是新的, 进行存储\033[0m')
            
    


if __name__ == '__main__':
    
    urls = ['http://bang.dangdang.com/books/fivestars/1-{page}'.format(**locals()) for page in range(1,26)]
    
    for page,url in enumerate(urls):
        print('\033[1;33m开始爬取第{page}页\033[0m'.format(page=page+1))
        ss = SpiderDangdang(url)
        ss.start()
