#!/usr/bin/env python
#-*- coding:utf-8 -*-

from urllib import request, parse
import ssl

context = ssl._create_unverified_context()


# url = "https://passport.baidu.com/v2/api/?login"

# # 伪装自己是浏览器
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
# }

# # 定义请求参数
# dict_data = {
#     "username": "13554221497",
#     "password": "lmt921108"
# }

# # 把请求的参数转化为byte
# data = bytes(parse.urlencode(dict_data), "utf-8")

# req = request.Request(url, data=data, headers=headers, method="POST")

# response = request.urlopen(req, context=context)
# print(response.read().decode("utf-8"))


