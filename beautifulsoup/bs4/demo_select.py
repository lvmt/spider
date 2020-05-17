#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup


html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

soup = BeautifulSoup(html, 'html.parser')


## 通过标签名查找

# print(soup.select('title'))

# print(soup.select('a'))

# print(soup.select('b')) 


# ##  通过类型查找

# print(soup.select('.sister')) 


# ## 通过id名查找

# print(soup.select('#link1'))


## 组合查找 
## 组合查找即和写class文件时，标签名与类名与id名进行组合的原理是一样的，
## 例如和查找P标签中，id等于link1的内容，二者需要使用空格分开

# print(soup.select('p #link1'))

# print(soup.select('p.title'))

## 直接子标签查找

print(soup.select('head > title'))