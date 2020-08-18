#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''爬取HGMD全站注释信息
'''

import requests
from bs4 import BeautifulSoup

import time


headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}



class HGMD(object):

    def __init__(self):
        pass

    def get_html(self,url,data='',method='GET'):
        '''得到页面的html信息
        '''
        if method == 'GET':
            try:
                response = requests.get(url,params=data,headers=headers)
                if response.status_code == 200:
                    return response.text
                else:
                    print('No')
                    return None
            except Exception as e:
                print('soup no')
                return None
            
        if method == 'POST':
            try:
                response = requests.post(url,data=data,headers=headers)
                if response.status_code == 200:
                    return response.text
                else:
                    return 'NO'
            except Exception as e:
                print('post no')
                print('wrong' ,e)
                return 'no'
            

    def get_soup(self,html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
        except:
            soup = BeautifulSoup(html, 'html.parser')
        return soup


    def total_page_number(self):
        '''得到hgmd所以的页面数目
        '''
        url = 'http://hgmdtrial.biobase-international.com/hgmd/pro/numGene.php' 
        html = self.get_html(url,method='GET')
        soup = self.get_soup(html)
        page_numbers = int(soup.select('div.content')[0].select('table tr td')[1].text.replace('\n', '').split(' ')[-1])
        
        return page_numbers
    
        
    def get_gene_info(self,page):
        '''得到页面上的基因名称
        ['MSH2', 'F9', 'MLH1', 'RB1', 'COL1A1']
        POST方法
        '''
        gene_info = []
        
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
        
        html = self.get_html(url,data=data,method='POST')
        soup =  self.get_soup(html)
        try:
            trs =  soup.select('div.content table')[-1].select('tr') 
        except:
            print(soup)
        for tr in trs[1:]:
            tds = tr.select('td')
            try:
                gene = tds[0].a.text
            except:
                gene = tds[0].text
            refseq = tds[1].text.split('.')[0]
            
            info = (gene,refseq)
            gene_info.append(info)
            
        return gene_info
        
    
    def get_gene_content(self,geneinfo):
        '''获取每个基因的结果
        '''
        gene_content = []
        url = 'http://hgmdtrial.biobase-international.com/hgmd/pro/all.php'
        data = {
            'gene': geneinfo[0],
            'inclsnp': 'N',
            'base': 'Z',
            'refcore': geneinfo[1],
            'sort': 'location',
            'database': 'Get all mutations'
            }
        html = self.get_html(url,data=data,method='POST')
        soup = self.get_soup(html)
        
        # 每个基因存在多个变异类型，需要分开处理，表头不一样
        # 然后对每个table进行处理
        gene_tabls = soup.select('div.content table.gene') 
        for table in gene_tabls:
            trs = table.select('tr')
            head = [item.text for item in trs[0].select('th')]
            
            for tr in trs[1:]:
                tr_content = []
                tds = tr.select('td')
                acc =  tds[0].form.input['value']
                tr_content.append(acc)
                for td in tds[1:-1]:
                    tr_content.append(td.text)
                try:
                    hg38 =  tds[-1].select('span')[0]['title']
                    hg19 =  tds[-1].select('span')[1]['title']
                except:
                    hg38 = 'None'
                    hg19 = 'None'
                tr_content.extend([hg38,hg19]) 
                
                gene_content.append(tr_content)
                
        return gene_content
                                
    
    def spider(self):
        # total_pages = self.total_page_number()
        # print('\033[1;32m总页数为：{total_pages}\033[0m'.format(**locals()))
        
        print('start')
        page = 2
        
        gene_info = self.get_gene_info(page)
        
        with open('hgmd1.txt', 'w') as fw:
            for geneinfo in gene_info:
                genename = geneinfo[0]
                gene_content = self.get_gene_content(geneinfo)                
                for content in gene_content:
                    fw.write('{}\t'.format(genename))
                    print(content.encode('utf-8'))
                    for item in content:
                        fw.write('{}\t'.format(item.encode('utf-8')))
                        #fw.write('{}\t'.format(item))
                    fw.write('\n')
        
        
if __name__ == '__main__':
    
    # import argparse
    # parser = argparse.ArgumentParser(description='HGMD spider')
    # parser.add_argument('')
    
    dd = HGMD()
    dd.spider()
