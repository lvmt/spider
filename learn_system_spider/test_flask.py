#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
测试flask的安装
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<b style="background-color:red">hello world</b>' # 这样可以增加html格式

if __name__ == '__main__':
    app.run()
    
    
