#!/usr/bin/env python
#-*- coding:utf-8 -*-


import re
import requests
from bs4 import BeautifulSoup
import xlwt
from pymongo import MongoClient


## 链接本地mongo数据库
client = client = MongoClient('localhost', 27017)
db = client.spider
collection = db.douban_movie


# 刚开始运行的时候，状态码为418，伪装头部信息后，即可正常运行
def request_douban(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        response = requests.get(url, headers=headers) 
        if response.status_code == 200:
            print("获取正常")
            return response.text
        else:
            print(response.status_code)
    except requests.RequestException:
        print("获取失败")
        return None


def save_to_excel(soup):

    lists = soup.find(class_="grid_view").find_all("li")
    # print(lists)

    for item in lists:
        item_name = item.find(class_="title").string 
        item_image = item.find('a').find('img').get('src')
        item_index = item.find(class_="").string
        item_score = item.find(class_="rating_num").string 
        item_author = item.find('p').text.strip()
        item_intr = item.find(class_='inq').string if item.find(class_='inq') else "None"
        print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + item_intr )
        with open('douban.txt', 'a', encoding="utf-8") as fw:
            fw.write("{item_index}\t{item_name}\t{item_score}\t{item_intr}\n".format(**locals())) 

        insert_item = {
            'item_name': item_name,
            'item_image': item_image,
            'item_index': item_index,
            'item_score': item_score,
            'item_author': item_author,
            'item_intr': item_intr
        }
        collection.insert_one(insert_item)


def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    print(url)
    html = request_douban(url)
    soup = BeautifulSoup(html, 'html.parser')
    save_to_excel(soup)

if __name__ == "__main__":
    for page in range(0, 10):
        main(page)