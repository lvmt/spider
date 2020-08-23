#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''爬取盗墓笔记小说免费版
'''


import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

class Story(object):
    
    def __init__(self,url):
        self.url = url
    
    
    def get_html(self,url):
        
        try:
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as e:
            print('wrong', e)
    
    
    def get_soup(self,html):
        try:
            soup = BeautifulSoup(html,'html.parser')
        except:
            soup = BeautifulSoup(html, 'xml')
        return soup


    def start(self):
        html = self.get_html(self.url)
        soup = self.get_soup(html)
        
        try:
            free_result = soup.select('div.volume span.free') 
            if free_result:
                for free in free_result:
                    chapters = free.parent.parent.select('li a')
                    for chapter in chapters:
                        title = chapter.text.strip().replace(' ', '_')
                        href = 'https:' + chapter['href']
                        
                        html = self.get_html(href)
                        soup = self.get_soup(html)
                        content =  soup.select('div.read-content')[0].text.strip().replace('\u3000', ' ')
                        print('\033[1;34m开始爬取:  {title}\033[0m'.format(**locals()))
                        with open(title+'.txt', 'w') as fw:
                            fw.write(content)
        except:
            None
    
    
    
if __name__ == '__main__':

    url = 'https://book.qidian.com/info/68223#Catalog'

    gg = Story(url)
    gg.start()
    