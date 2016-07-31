#!/usr/bin/python
#coding:utf-8
from urllib2 import  urlopen
import os

os.system("clear")

def getFirstCode():
	city_first_code = {}
	mes_url = "http://m.weather.com.cn/data5/city.xml"
	web = urlopen(mes_url)
	content = web.read()#content为字符串格式为01|北京,02|上海,03|天津,04|重庆,05|黑龙江
	#print  content ,"****" ,type(content)
	first_code = content.split(",")#first_code为列表
	#print first_code
	for coding in [ x for x in first_code ]:
		code , cityName = coding.split("|")
		city_first_code[cityName] = code
	#	print cityName ,code 
	#print "*" * 30 
	#print city_first_code
	return city_first_code




if __name__ == "__main__":
	print getFirstCode()
