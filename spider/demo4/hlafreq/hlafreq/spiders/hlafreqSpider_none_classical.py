#!/usr/bin/env python
#-*- coding:utf-8 -*-

import scrapy 
from hlafreq.items import HlafreqItem
import pymongo
import re 


## 将数据储存到mongo数据库中
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['hlafreq']
collections = db['non-classical']

class HlaFreq(scrapy.Spider):
    
    name = "hlafreq"
    # allowed_domains = ["http://www.allelefrequencies.net"]
    start_urls = ["http://www.allelefrequencies.net/hla6006a.asp?page=1&hla_locus=&hla_locus_type=Non-classical&hla_allele1=&hla_allele2=&hla_selection=&hla_pop_selection=&hla_population=&hla_country=&hla_dataset=&hla_region=&hla_ethnic=&hla_study=Controls%20for%20Disease%20Study&hla_sample_size=&hla_sample_size_pattern=equal&hla_sample_year=&hla_sample_year_pattern=equal&hla_level=&hla_level_pattern=equal&hla_show=&hla_order=order_1&standard=a"]
   
    for page in range(2,3):
        new_url = "http://www.allelefrequencies.net/hla6006a.asp?page={page}&hla_locus=&hla_locus_type=Non-classical&hla_allele1=&hla_allele2=&hla_selection=&hla_pop_selection=&hla_population=&hla_country=&hla_dataset=&hla_region=&hla_ethnic=&hla_study=Controls%20for%20Disease%20Study&hla_sample_size=&hla_sample_size_pattern=equal&hla_sample_year=&hla_sample_year_pattern=equal&hla_level=&hla_level_pattern=equal&hla_show=&hla_order=order_1&standard=a".format(**locals())
        start_urls.append(new_url)
   
    
    def parse(self, response):
        
        item = HlafreqItem()
        table = response.xpath('//*[@id="divGenDetail"]/table') 
        table_list = table.xpath('tr')  #将每行信息，储存在列表的元素里面
        del(table_list[0])              #删除表头信息
        print("*" * 20, table)
        for tr in table_list:
                   #
            allele = tr.xpath('td[2]/a/text()').extract()[0].strip()   #基因名在链接标签a里面
            country = tr.xpath('td[4]/a/text()').extract()[0].strip()
            freq =  tr.xpath('td[6]//text()').extract()[0].strip()
            #sam = tr.xpath('td[8]/text()').extract()[0]                  #由于人数超过1000，会采用科学计数法，修改
            sample_size = "".join((tr.xpath('td[8]/text()').extract()[0].split(',')))
            imgt_database = re.search(r'href=(.*)target.*', tr.xpath('td[9]/a').extract()[0]).group(1)
           
            insert_dict = {
                "allele":allele,
                "country":country,
                "freq":freq,
                "sample_size":sample_size,
                "imgt_database":imgt_database
            }

            ## 去除已经爬取的内容
            if collections.find_one(insert_dict):
                print("\033[31m该item已经爬取，跳过\033[0m")
            else:
                print("\033[32m爬取该item，存入数据库中\033[0m")
                print(insert_dict)
                collections.insert_one(insert_dict)           
            yield item
            
           
            
            
            
    