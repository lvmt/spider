#!/usr/bin/env python
#-*- coding:utf-8 -*-


import scrapy


class mySpider(scrapy.Spider):

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"

        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "xxx", "password":"xxxx"},
            callback=self.parse
        )

    def parse(self, response):
        ## do something

        pass

    