import requests
import json
# 引用requests,json模块

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for x in range(5):

    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.lyric_next',
    'searchid':'94267071827046963',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(x+1),
    'n':'10',
    'w':'周杰伦',
    'g_tk':'1714057807',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'
    }

    res = requests.get(url, params = params)
    print(res.url)
    
    # #下载该网页，赋值给res
    # jsonres = json.loads(res.text)
    # #使用json来解析res.text
    # list_lyric = jsonres['data']['lyric']['list']
    # #一层一层地取字典，获取歌词的列表

    # for lyric in list_lyric:
    # #lyric是一个列表，x是它里面的元素
    #     print(lyric['content'])
    # #以content为键，查找歌词