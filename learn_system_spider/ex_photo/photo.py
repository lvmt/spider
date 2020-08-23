#!/usr/bin/env python 
#-*- coding:utf-8 -*-

'''批量爬取网站照片
'''


import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


class SpiderPhoto(object):
    
    def __init__(self, url):
        self.url = url
        
    
    def get_soup(self):
        '''根据输入url获取soup
        '''
        try:
            response = requests.get(self.url, headers=headers)
            print(response)
            response.raise_for_status
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print('aaaaaaaa',e)
            soup = 'None'
        return soup

    
    def get_all_img_urls(self,soup):
        imgs = soup.select('div.list li a img')
        return [item['src'] for item in imgs]
    
    
    def save_photo(self,imgurl):
        res = requests.get(imgurl)
        name = imgurl.split('/')[-1]
        with open(name, 'wb') as fw:
            fw.write(res.content)
            
    
    def start(self):
        soup = self.get_soup()
        imgs = self.get_all_img_urls(soup)
        
        for imgurl in imgs:
            print('\033[1;33m开始爬取图片: {imgurl}\033[0m'.format(**locals()))
            self.save_photo(imgurl)
            



if __name__ == '__main__':
    
    urls = ['http://www.netbian.com/index.htm']
    
    urls += ['http://www.netbian.com/index_{page}.htm'.format(**locals()) for page in range(2,10)]
    
    for page,url in enumerate(urls):
        print('\033[1;32m开始爬取第 {} 页\033[0m'.format(page+1))
        pp = SpiderPhoto(url)
        pp.start()
    
