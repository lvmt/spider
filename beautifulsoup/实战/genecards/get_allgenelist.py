#!/usr/bin/env python
#-*- coding:utf-8 -*-


from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient



## 链接本地mongo数据库
client = client = MongoClient('localhost', 27017)
db = client.genecards
collection = db.all_genelist


def get_html(url):
    try:
        UA = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        headers = {"User-Agent": UA}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    need_list = soup.find('pre').string
    need_list = need_list.strip().split('\n')
    for item in need_list:
        insert_item = {"gene_name": item}
        print("开始插入数据")
        print(insert_item)
        collection.insert_one(insert_item)


if __name__ == "__main__":
    url = "https://www.genecards.org/cgi-bin/cardlisttxt.pl"
    html = get_html(url)
    get_soup(html)




