#coding=gbk

import cookielib
import urllib2
import re

url_head ="http://www.cskaoyan.com/"

responsel=urllib2.urlopen("http://www.cskaoyan.com/forum.php")
pattern = re.compile("forum-[0-9]*-1.html")
f =  responsel.read()

url_rail_list = pattern.findall(f)
url_list=[]
for i in url_rail_list:
	url_list.append("http://cskaoyan.com/"+i)

for i in url_list:
	responsel=urllib2.urlopen(i)
	data = responsel.read().decode('gbk')
	print data
