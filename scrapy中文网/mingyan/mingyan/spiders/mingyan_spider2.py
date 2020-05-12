#!/usr/bin/env python
#-*- coding:utf-8 -*-

import scrapy

"""
scrapy 初始化url的两种写法：
一种是常量： start_urls，但是必须定义一个方法 parse()
另一种是直接定义一个方法：start_requests()
"""


class mingyan(scrapy.Spider):

    name = "simpleUrl"
    start_urls = [
        "http://lab.scrapyd.cn/page/1/",
        "http://lab.scrapyd.cn/page/2/"
    ]

    # 另一种初始化链接写法
    # def start_requests(self):   # 由此方法通过下面的链接爬取页面
    #     # 定义爬取链接
    #     urls = [
    #         "http://lab.scrapyd.cn/page/1/",
    #         "http://lab.scrapyd.cn/page/2/"
    #     ]

    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse) # 爬取到的页面如何处理，交给parse方法处理

    def parse(self, response):

        """
        start_requests: 已经爬取到页面， 如何提取我们想要的内容，可以定义在这个方法里面，
        此次没有定义，只是简单的保存页面，
        可以使用xpath, css 或者正则进行相应提取, 
        scrapy运行规则：
        1、定义链接
        2、通过链接爬取（下载）页面
        3、定义规则，然后提取数据
        """

        page = response.url.split("/")[-2]   #  根据url，提取页面信息
        filename = "mingyan-%s.html" % page 
        with open(filename, 'wb') as fw:
            fw.write(response.body)          # response.body 就代表了刚才下载的页面
        self.log("保存文件： %s" % filename) 
        