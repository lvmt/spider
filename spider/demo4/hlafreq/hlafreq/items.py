# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HlafreqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    allele = scrapy.Field()
    freq = scrapy.Field()
    sample_size = scrapy.Field()
    igmt_database = scrapy.Field()
    
    
