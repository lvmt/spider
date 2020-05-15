#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")  # 打开百度
print(response.read().decode("utf-8"))