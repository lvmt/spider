#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''实现中英文翻译
'''

import json
import requests


class Translate(object):

    def __init__(self,word):
        self.word = word

    def translate_result(self):
        '''自动识别，进行中英文翻译
        '''
        # 有道翻译api
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        # 传输的参数，其中 i 为需要翻译的内容
        key = {
            'type': "AUTO",
            'i': self.word,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        try:
            response = requests.post(url,data=key)
            if response.status_code == 200:
                result = json.loads(response.text)
                source_word = result['translateResult'][0][0]['src']
                translate_word = result['translateResult'][0][0]['tgt']
                # return [source_word, translate_word]
                return translate_word
            else:
                print('有道词典调用失败')
                return None
        except Exception as e:
            self.translate_result()


if __name__ == '__main__':
    
    import sys
    word = sys.argv[1]

    tt = Translate(word)
    print(tt.translate_result())

    