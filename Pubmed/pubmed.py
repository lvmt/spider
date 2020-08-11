#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''提取pubmed上面的文献参考
'''

import time
import requests
from bs4 import BeautifulSoup
import translate


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
}


class Pubmed(object):

    def __init__(self,args):
        self.args = args
        self.url = args['url']
        self.keywords = args['keywords']
        self.pages = args['pages']
        
        self.queryurl = ''


    def get_response(self,url,data=None):
        try:
            response = requests.get(url,params=data,headers=headers)
            if response.status_code == 200:
                return response
            else:
                print(response.status_code)
                #exit('\033[1;34m被封啦\033[0m')
        except Exception as e:
            self.get_response(url)


    def get_soup(self,response):
        try:
            soup = BeautifulSoup(response.text,'html.parser')
        except:
            soup = BeautifulSoup(response.text,'xml')
        return soup


    def get_total_pages(self):
        '''得到查询结果的页数
        '''
        data = {
            'term': self.keywords
        }

        response = self.get_response(self.url,data)
        self.queryurl = response.url   #得到查询url 
        print('查询url：',self.queryurl)
        soup = self.get_soup(response)
        results = soup.select('.results-amount .value')[0].string
        results = int("".join(results.split(',')))
        total_page = int(results)/10 + 1

        return total_page


    def get_pmids(self,pages,total_page):
        '''得到需要页数的标题链接
        '''
        pmids_lists = []
        pages = total_page if total_page < pages else pages

        for page in range(1,pages+1):
            url = '{self.queryurl}/&page={page}'.format(**locals()) # 查询结果的每一个url
            response = self.get_response(url)
            soup = self.get_soup(response)
            pmids = soup.select('div.search-results-chunk')[0]['data-chunk-ids']
            pmids = pmids.split(',')
            pmids_lists.extend(pmids)

        return pmids_lists


    def get_content(self,pmid):
        '''得到每个标题链接的内容
        '''
        id_url = '{self.url}/{pmid}/'.format(**locals())
        response = self.get_response(id_url)
        soup = self.get_soup(response)

        try:
            title = soup.select('main.article-details h1')[0].text.strip()
        except:
            title = 'None'
        
        try:
            abstract = ''.join([item.text.strip().replace('\n', ' ').replace('  ', '') for item in soup.select('div.abstract p')])
        except:
            abstract = 'None'
            
        return '{title}\t{pmid}\t{abstract}'.format(**locals())
            
        # try:
        #     abstract = [item.text.strip().replace('\n', ' ').replace('  ', '') for item in soup.select('div.abstract p')]
            
        #     for item in abstract:
        #         print('\033[1;32m文献爬取结果:\033[0m')
        #         #print(item)
        #         items = item.split('.')
        #         for a in items:
        #             a = "{a}".format(**locals())
        #             print(a)
        #             print(translate.Translate(a).translate_result())
        #     # c_abstract = [translate.Translate(item).translate_result() for item in abstract]
        # except:
        #     abstract = 'None'
        #keywds = soup.select('div.abstract p')[1].text.strip().split('\n')[-1]

        #print('\033[1;32m文献爬取结果:\033[0m')

        # print(id_url)
        # print(pmid)
        # print(title)
        # print(abstract)
        # #print(c_abstract)


    def start(self):
        
        out = open('result.xls', 'w')
        
        total_page = self.get_total_pages()
        pmids_lists = self.get_pmids(self.pages,total_page)
        for idx,pmid in enumerate(pmids_lists):
            print('\033[1;35m爬取第{idx}篇文献.....\033[0m'.format(idx=idx+1))
            content = self.get_content(pmid)
            out.write(content+'\n')
            time.sleep(3)




if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser(description='爬取pubmed文献')
    parser.add_argument('--url', help='pubmed的url链接', default='https://pubmed.ncbi.nlm.nih.gov')
    parser.add_argument('keywords', help='查询关键字')
    parser.add_argument('--pages', type=int, help='爬取页数', default=2)

    args = vars(parser.parse_args())

    pp = Pubmed(args)
    pp.start()

    # http://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile 
    # 利用百度api进行翻译