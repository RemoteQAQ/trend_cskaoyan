#coding=utf-8

import cookielib
import urllib2
import re

ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}	
url_head ="http://www.cskaoyan.com/"

responsel=urllib2.urlopen("http://www.cskaoyan.com/forum.php")
pattern = re.compile("forum-[0-9]*-1.html")
f =  responsel.read()

url_rail_list = pattern.findall(f)
url_list=[]
for i in url_rail_list:
	url_list.append("http://cskaoyan.com/"+i)

'''
for i in url_list:
	responsel=urllib2.urlopen(i)
	data = responsel.read().decode('gbk')
	print data
'''

for k in url_list:
	responsel=urllib2.urlopen(k)
	data = responsel.read().decode('gbk').encode('utf8')
	pattern=re.compile("<title>.*?大学")
	school_name = pattern.findall(data)
	for i in school_name:
		print i.decode('utf8').encode('utf8')
	pattern=re.compile('title=\\"上次排名:[0-9]{1,3}')
	school_rank = pattern.findall(data)
	for i in school_rank:
		print i.decode('utf8').encode('utf8')
	print "工作正常"
