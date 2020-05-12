#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
我们要爬取的是：http://lab.scrapyd.cn 这么一个网站，
并且顺着下一页、下一页把所有内容爬取完，
"""
 
import scrapy 
import logging



class mingyanSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://lab.scrapyd.cn",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            self.logger().info("开始输出爬取内容： ")
            yield {
                "内容": quote.css("span.text::text").extract_first() ,
                "作者": quote.xpath("span/small/text()").extract_first(),
            }

        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, self.parse)

    def logger(self):
        logging.basicConfig(
            format='[%(asctime)s %(funcname)s %(levelname)s %(message)s]',
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.INFO)
        log = logging.getLogger(__name__)
        return log

