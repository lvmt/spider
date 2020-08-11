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


        pass