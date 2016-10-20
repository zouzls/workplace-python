#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
import re

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) '
					 'AppleWebKit/537.36 (KHTML, like Gecko) '
					 'Chrome/49.0.2623.75 Safari/537.36',
		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'accept-encoding':'gzip, deflate, sdch',
		'accept-language':'zh-CN,zh;q=0.8',
		'cache-control':'no-cache'
}

def write():
	res=requests.get('http://ssl.gongyi.qq.com/wxact/201699/index.html',headers=headers)
	html=res.text
	soup=BeautifulSoup(html,'lxml')
	total=soup.find_all("span")
	print(html)
	# print(total)


if __name__=='__main__':
	write()
