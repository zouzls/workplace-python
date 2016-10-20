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
path='F:/workplace-Python/helloworld/1688.txt'
def demo():
	res=requests.get('https://wanwang.aliyun.com/domain/')
	print(type(res))
	print(res.status_code)
	print(res.encoding)
	print(res.cookies)

def parse():

	html=read()
	soup=BeautifulSoup(html,'lxml')
	s1=set()
	for a in soup.find_all(href=re.compile('https://detail.1688.com/offer/')):
		# print(a['href'])
		s1.add(a['href'])

	s2=set()
	f=open('F:/workplace-Python/helloworld/info.txt','w',encoding='utf-8')
	for href in s1:
		detail=BeautifulSoup(page(href),'lxml')
		contact=detail.find('a',href=re.compile('contactinfo.htm'))
		info=BeautifulSoup(page(contact['href']),'lxml')

		record=""

		company=info.find('div',class_='contact-info')
		if company.contents!=None and company.contents[1]!=None:
			comName=company.contents[1].string
			# print(comName)
			record=record+'公司名称：'+comName

		member=info.find('a',class_='membername')
		if member!=None:
			# print(member.string)
			record=record+'，联系人：'+member.string

		phone=info.find('dl',class_='m-mobilephone')
		if phone!=None and phone.contents[3]!=None:
			number=phone.contents[3].string
			if number ==None:
				record=record+'，联系方式：null'
				# print('null')
			else:
				record=record+'，联系方式：'+number.strip()
				# print(number.strip())

		addr=info.find('dd',class_='address')
		if addr!=None:
			record=record+'，地址：'+addr.string
			# print(addr.string)
		print(record)
		f.write(record)
		print('--------------------------------------------')
		# print(contact)
		# print(href)
	f.close()


def page(url):
	res=requests.get(url)
	return res.text

def write():
	params={'keywords':'apple',
			'descendOrder':'true',
			'sortType':'va_rmdarkgmv30',
			'uniqfield':'userid'
			}
	res=requests.get('https://s.1688.com/selloffer/offer_search.htm',params=params,headers=headers)
	with open(path,'w',encoding='utf-8') as f:
		f.write(res.text)

def read():
	with open(path,'r',encoding='utf-8') as f:
		return  f.read()

if __name__=='__main__':
	write()
	parse()