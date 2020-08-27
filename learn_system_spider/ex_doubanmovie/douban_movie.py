#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

class SpiderDouban(object):
    
    def __init__(self, url):
        self.url = url

    def get_collection(self):
        client = MongoClient('localhost', 27017)
        database = client.spider
        collection = database.douban
        return collection
    
    def get_reponse(self):
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status
            response.encoding = response.apparent_encoding
            html = response.text
        except Exception as e:
            html = 'None'
        return html

    def get_soup(self,html):
        try:
            soup = BeautifulSoup(html,'html.parser')
        except:
            soup = BeautifulSoup(html, 'xml')
        return soup
    
    def get_items(self,soup):
        items = soup.select('div.article>ol>li')
        return items
    
    def get_item_content(self,item):
        try:
            head = item.select('div.hd')[0].text.strip()
        except:
            head = 'None'
        
        try:
            people = item.select("div.article>ol>li>div p[class='']")[0].text.strip().replace('  ', '')
        except:
            people = 'None'
            
        try:
            star = item.select('div.article>ol>li>div div.star')[0].text.strip().replace('\n',' ')
        except:
            star = 'None'
            
        try:
            comment = item.select('div.article>ol>li>div p.quote')[0].text.strip()
        except:
            comment = 'None'

        content = {
            'head': head,
            'people': people,
            'star': star,
            'comment': comment
        }
        
        return content
    
    def start(self):
        collection = self.get_collection()
        
        html = self.get_reponse()
        soup = self.get_soup(html)
        items = self.get_items(soup)
        
        for item in items:
            content = self.get_item_content(item)
            if collection.find_one(content):
                print('\033[1;31m该item已经在数据库中,不进行存储\033[0m')
            else:
                collection.insert_one(content)
                print('\033[1;32m该item是新的, 进行存储\033[0m')

    

if __name__ == '__main__':
    
    urls = ['https://movie.douban.com/top250?start={num}&filter='.format(num=num) for num in range(0,250,25)]

    for page,url in enumerate(urls):
        print('\033[1;33m开始爬取第{page}页\033[0m'.format(page=page+1))
        ss = SpiderDouban(url)
        ss.start()
        
 