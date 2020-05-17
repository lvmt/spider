#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
练习post用法
"""


import requests 
from bs4 import BeautifulSoup


url = "http://hgmdtrial.biobase-international.com/hgmd/pro/all.php/"

BASE_URL = 'http://hgmdtrial.biobase-international.com/hgmd/pro'

query_dict ={
    "gene": "DMD",
    "sort": "location",
    "database": "Get+all+mutations"
}

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        } 


def get_soup(url, method="GET", **kwargs):
    
    if method == "GET":
        response = requests.get(url, headers=headers, **kwargs)
    elif method == "POST":
        response = requests.post(url, headers=headers, **kwargs)
        
    try:
        soup = BeautifulSoup(response.content, 'lxml')
    except Exception as e:
        soup = BeautifulSoup(response.content, 'html.parser')
        
    return soup

def get_gene_mutation(gene):
    url = "http://hgmdtrial.biobase-international.com/hgmd/pro/all.php/"
    url = url
    data ={
        "gene": gene,
        "sort": "location",
        "database": "Get all mutations"
    }
    
    soup = get_soup(url, method="POST", data=data)
    
    # tables = soup.select('table.gene')
    tables = soup.find('table', class_='gene').find_all('tr')
    
    for i in tables:
        print(i)
    
    
    return tables
    

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("gene", help="请输入基因名称")
    
    args = vars(parser.parse_args())
    
    gene = args["gene"]
    
    mutation = get_gene_mutation(gene)
    
    print(mutation)



















# response = requests.get(url, data=query_dict, headers=headers)

# print(response.status_code)


# html = response.content

# soup = BeautifulSoup(html, 'lxml')

# info = soup.find('table')
# print(soup)