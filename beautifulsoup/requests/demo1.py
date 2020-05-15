#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests

url = "https://www.baidu.com/"
kv = {"wd": "python"} 

response = requests.get(url, params=kv) 

try:
    if response.status_code == 200:
        print(response.request.url)
        print(response.text)


except Exception as e:
    print("无法爬取 {e}".format(**locals()))
finally:
    print("程序完成")
