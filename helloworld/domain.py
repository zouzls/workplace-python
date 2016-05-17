#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup

def get_page_urllib():
	res=request.urlopen('https://wanwang.aliyun.com/domain/')
	html=res.read()
	print(html)

def get_page_request():
	req=request.Request('https://wanwang.aliyun.com/domain/')
	res=request.urlopen(req)
	html=res.read();
	print(html)
	return html

if __name__=='__main__':
	html=get_page_request()
