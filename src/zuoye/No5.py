#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import re
import os

url="http://jandan.net/ooxx"
s = requests.session()
header_jandan={'Host': 'jandan.net',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://jandan.net/ooxx',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8'}
resp = s.get(url,headers=header_jandan,timeout=10)
if len(resp.text) < 1500:
    resp2 = s.get(url,headers=header_jandan,timeout=10)
    text=resp2.text
else:
    text=resp.text
#print rn.text
img_url=re.findall(ur'(?<=\<img src\=").*?(?=\")',text)
d=os.getcwd()
for i in img_url:
    ret=i.split("/")
    file = ret[-1]
    #print file
    if i.find("http") == -1:
        url_img="http:"+i
        r_img=s.get(url_img,headers=header_jandan,timeout=10)
        open(os.path.join(d,file), 'wb+').write(r_img.content)
        print "write %s" % file
    
    
    