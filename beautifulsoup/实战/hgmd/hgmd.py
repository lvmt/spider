#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
联系爬取hgmd某个基因的全部变异位点
"""

import requests
import re 
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }


def get_soup(url, method="GET", **kwargs):

    if method == "GET":
        response = requests.get(url, headers=headers, **kwargs)
    elif method == "POST":
        response = requests.post(url, headers=headers, **kwargs)
    
    response = response.decode("utf-8")
    try:
        soup = BeautifulSoup(response.content, 'lxml')
    except:
        soup = BeautifulSoup(response.content, 'html.parser')
    
    print(response.status_code)
    
    return soup


def get_gene_mutation(gene):
    url = "http://hgmdtrial.biobase-international.com/hgmd/pro/all.php/"
    data ={
        "gene": gene,
        "sort": "location",
        "database": "Get all mutations"
    }

    soup = get_soup(url, method="POST", data=data)
 
    tables = soup.select('table.gene')

    print(tables)
    # for item in tables:
    #     print(soup)
    #     print(item)

 
if __name__ == "__main__":

    import sys
    args = sys.argv

    gene = args[1]
    get_gene_mutation(gene)
