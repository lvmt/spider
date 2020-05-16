#!/usr/bin/env python
#-*- coding:utf-8 -*- 


import requests
from bs4 import BeautifulSoup
import re 



html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')



# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# demo1 = soup.find_all(has_class_but_no_id)
# print(demo1)
# print(len(demo1))

# for index,i in enumerate(demo1):
#     print(index, i)
    
    
# def not_lacie(href):
#         return href and not re.compile("lacie").search(href)
# demo1 = soup.find_all(href=not_lacie)

# print(demo1)

# print(soup.find_all("title"))
# # [<title>The Dormouse's story</title>]

# print(soup.find_all("p", "title")) 
# # [<p class="title"><b>The Dormouse's story</b></p>]

# print(soup.find_all("a"))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# print(soup.find_all(id="link2"))
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# import re 
# print(soup.find(string=re.compile("sisters"))) 
# # Once upon a time there were three little sisters; and their names were 

print(soup.find_all(string="Elsie"))