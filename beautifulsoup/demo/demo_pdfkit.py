#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pdfkit

content_url = "https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484657&idx=1&sn=998bfcce6cd22b7fedff29e68a46fe3f&chksm=fc8bbc60cbfc3576f117d3566fbea8a042ee573d840bbe6a3d4ec9bffef815c691b7f9a59711&scene=27#wechat_redirect"


# test_url = "https://www.dogedoge.com/results?q=python++pdfkit"
# pdfkit.from_file(test_url, "demo.pdf") 

pdfkit.from_url('https://www.dogedoge.com/', 'out.pdf')