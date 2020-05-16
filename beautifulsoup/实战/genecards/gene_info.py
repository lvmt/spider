#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup


def get_html(genename):
    
    url = "https://www.genecards.org/cgi-bin/carddisp.pl?"
    kw = {"gene": genename}
    headers = {
        "User-Agent": "https://www.genecards.org/cgi-bin/carddisp.pl?gene=AKT3"
        }
    
    try:
        response = requests.get(url, params=kw, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None 
    

def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def clean_html_info(info):
    """
    爬取到的html元素可能带有标签元素，或者多余的空白行
    """
    if info:
        return info.get_text().strip("\n")
    else:
        return info
        

def get_info(soup):
    # info = soup.find("h2", class_="gc-section-header")
    
    info = soup.find(id="summaries").find_all(class_="gc-subsection")
    
    for div in info:
        title = clean_html_info(div.find('h3'))
        content = clean_html_info(div.find('p'))
        
        print("\033[31m开始打印内容：\033[0m")
        print(title)
        print(content)

    return info
    

def main():
    html = get_html(genename)
    soup = get_soup(html)
    info = get_info(soup)
    
    

if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser() 
    parser.add_argument('--genename', '-g', help="输入基因名称")
    
    args = vars(parser.parse_args())
    
    genename = args["genename"]
    main()
