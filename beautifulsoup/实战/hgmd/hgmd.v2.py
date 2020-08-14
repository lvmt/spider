#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''爬取HGMD全站注释信息
'''

import requests
from bs4 import BeautifulSoup

class HGMD(object):

    def __init__(self,args):
        pass

    def get_response(self):
        pass

    def get_soup(self,html):

        try:
            soup = BeautifulSoup(html, 'html.parser')
        except:
            soup = BeautifulSoup(html, 'html.parser')

        return soup


    def get_gene(self,page):
        '''得到指定页面上面的基因名称
        '''
        url = 'http://hgmdtrial.biobase-international.com/hgmd/pro/numGene.php'

        data = {
            'display': '',
            'limit': 5,
            'fuzz': '', 
            'mut': '', 
            'poly': '', 
            'search4': '', 
            'searchType': '',
            'out': '', 
            'batchInput1': '', 
            'page': page,
            'DM': '', 
            'DP': '', 
            'prior': '' 
        }
        
        response = requests.post(url, data=data)
        html = response.text 
        soup =  self.get_soup(html)

        total_page = int(soup.select('table')[0].select('tr>td')[1].text.split('of')[-1].replace(' ', ''))

        if page < total_page + 1:
            