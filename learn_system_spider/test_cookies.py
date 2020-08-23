#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''爬虫登陆问题解决
'''


import requests
from bs4 import BeautifulSoup


def QQ():
    url = 'https://user.qzone.qq.com/2546871627'
    headers = {
        'user-agent': 
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'cookie': 
            'Cookie: pgv_pvi=8141903872; RK=eF6FFdP33W; ptcz=4ab2fb3be5530811871b141246243765611727e457d1a077925f875183b878da; eas_sid=z1D5f8a443B4K5L619j4s0a9I5; pgv_pvid=3648950240; _ga=GA1.2.135710323.1596777054; pac_uid=0_b42f540d9cbd1; uin=o2546871627; skey=@PVTemCMmF; zzpaneluin=; zzpanelkey=; p_skey=iZW-kVao4QRMAOmi1o*DZWVJU9Cp14-8MplUpvIWRWw_; pt4_token=wnU9hMwOfp2H*kO5gm3cuW6POGjW7FaV*V7Et0YSWwo_; p_uin=o2546871627; pgv_si=s5516395520; _qpsvr_localtk=0.44740271146054433; pgv_info=ssid=s1170139288; Loading=Yes; qz_screen=1280x720; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=11'
    }
    
    try:
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
    except:
        html = 'None'
        
    with open('QQ.html', 'w', encoding='utf-8') as fw:
        fw.write(html)
        
        
QQ()