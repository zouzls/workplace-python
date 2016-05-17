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
		'cache-control':'no-cache',
		'cookie':'cna=mW7BD4YmWD4CATussE+++NE4; '
				 'ali_beacon_id=59.172.176.79.1463473284459.442952.6; '
				 'JSESSIONID=8L78onQv1-gwgVutvuDHoUD2psQ7-k7lgRlP-NIc7;'
				 ' __cn_logon__=false; alicnweb=touch_tb_at%3D1463473367123; '
				 'ad_prefer="2016/05/17 16:37:52"; '
				 'h_keys="%u5efa%u7b51%u6750%u6599#%u5be4%u8679%u74da%u93c9%u612d%u67a1"; '
				 'alisw=swIs1200%3D1%7C; '
				 'ali_ab=59.172.176.79.1463473284832.6; '
				 '_csrf_token=1463474340283; '
				 '_tmp_ck_0="pgW8OZwgGvhoMFapZFISyoL1E4kyivVmFjlqhgfbirbfh8kbcrwlUQ8'
				 'MGiWE0Ljq1W%2BJxvCAjAeydki4u%2FMfF5Rd1DvzAQFwFp38ywm7w72zNThL7ufK7nZn'
				 '3DLPyVnNZ8MM0NftXPyRsn%2Fe0FG7nKFiM0Q22Skm8IAE3nmNQ9Ihb8Yk2zDlQWir19811'
				 'ylSEG14x8b4tcR1N5FhwGy8zn51kS81kSy9t65aRL18Dlr19uY3LgdpmNqv4X5W%2FXqfwh'
				 '6ZZmLwJ8vbcVXnLHtIZuXrNaPMk9K7cpvpV7gTVUDH1EjrzNkvliaPgcZNpvL9t2547%2BI'
				 'ildprGAXxxhDA6OBhRsxn%2BimnUYhuGKC2wvctptfBeFKXy3egkmBSGXzECyjB%2BjPiK%2B8%3D"; '
				 'l=AgkJZhetI4dEXR4e6BEiGkdUmT9jVv2I'
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
	f=open('F:/workplace-Python/helloworld/info.txt','w')
	for href in s1:
		detail=BeautifulSoup(page(href),'lxml')
		contact=detail.find('a',href=re.compile('contactinfo.htm'))
		info=BeautifulSoup(page(contact['href']),'lxml')
		# print(len(info.find('dl',class_='m-mobilephone').contents))
		# print('公司名称：'+info.find('div',class_='contact-info').contents[1].string+
		# 	  '|联系人：'+info.find('a',class_='membername').string+
		# 	  '|移动电话：'+info.find('dl',class_='m-mobilephone').contents[3].string+
		# 	  '|地址：'+info.find('dd',class_='address').string)

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
	params={'keywords':'apple'}
	res=requests.get('https://s.1688.com/selloffer/offer_search.htm',params=params,headers=headers)
	with open(path,'w') as f:
		f.write(res.text)

def read():
	with open(path,'r') as f:
		return  f.read()

if __name__=='__main__':
	parse()