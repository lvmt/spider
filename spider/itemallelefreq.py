#!/usr/bin/env python
#-*- coding:utf-8 -*-

import scrapy

class ItemfreqSpider(scrapy.Spider):

    name = "itemfreq"
    start_urls = ["http://www.allelefrequencies.net/hla6006a.asp?hla_locus_type=Classical&hla_locus=&hla_allele1=&hla_allele2=&hla_selection=&hla_pop_selection=&hla_population=&hla_country=&hla_dataset=&hla_region=&hla_ethnic=&hla_study=Controls+for+Disease+Study&hla_order=order_1&hla_sample_size_pattern=equal&hla_sample_size=&hla_sample_year_pattern=equal&hla_sample_year=&hla_level_pattern=equal&hla_level=&standard=a&hla_show="]

    def parse(self, response):

        tables = response.css(".tblNormal")
        trlist = tables.css('tr') 

        head = trlist[0]
        content = trlist[1:] 

        for index,item in enumerate(content):
            itemlist = item.css('td') 
            
            allele = itemlist[1].css("a ::text").extract_first().strip()    # hla 名称
            country = itemlist[3].css("a ::text").extract_first().strip()   # 国家名称
            freq = itemlist[5].css("::text").extract_first().strip()   # 频率
            number = itemlist[7].css("::text").extract_first().strip()   # 频率
            imgt = itemlist[8].css("a::attr(href)").extract_first().strip() 

            print(index, allele, country, freq, number, imgt)


        