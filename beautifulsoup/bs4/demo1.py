#!/usr/bin/env python
#-*- coding:utf-8 -*- 


from bs4 import BeautifulSoup
import lxml

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc, 'lxml')

# 获取标题内容
print(soup.title.string)  # 学习python的正确姿势

# 获取p标签里面的内容
print(soup.p.string) # 小帅b的故事

# 获取超链接
print(soup.a)

# 获取所有的超链接
print(soup.find_all('a'))   # 返回list

# 获取id为link2的超链接
print(soup.find(id="link2"))

# 获取页面中的所有内容
print(soup.get_text())


## css ， select方法

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.select('title'))
print(soup.select('body a'))
print(soup.select('p > #link1'))
