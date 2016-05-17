#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

res=requests.get('https://wanwang.aliyun.com/domain/')
soup=BeautifulSoup(res.text,'lxml')
def func():
	res=requests.get('https://wanwang.aliyun.com/domain/')
	soup=BeautifulSoup(res.text,'lxml')
	print(soup.a)
	print(type(soup.a))
	print(soup.a.attrs)
	print(soup.a.get('href'))

def visit():
	res=requests.get('https://wanwang.aliyun.com/domain/')
	soup=BeautifulSoup(res.text,'lxml')
	# print(soup.head.contents)
	# print(soup.head.contents[1])
	#
	# ul=soup.ul
	# print(ul.contents)
	# print(ul.children)
	# for child in ul.children:
	# 	print(child)

	# for des in soup.descendants:
	# 	print(des)

	for li in soup.li.next_siblings:
		print(li.string)

def search():
	# for var in soup.find_all('li'):
	# 	print(var.string)
	# for tag in soup.find_all(True):
	# 	print(tag.name)
	for a in soup.find_all('a'):
		print(a.get('href'))

if __name__=='__main__':
	search()