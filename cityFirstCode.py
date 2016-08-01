#!/usr/bin/python
#coding:utf-8
from urllib2 import  urlopen
import os

os.system("clear")

def getCityCode(mes_url = "http://m.weather.com.cn/data5/city.xml"):
	city_code = {}
	web = urlopen(mes_url)
	content = web.read()#content为字符串格式为01|北京,02|上海,03|天津,04|重庆,05|黑龙江
	#print  content ,"****" ,type(content)
	first_code = content.split(",")#first_code为列表
	#print first_code
	for coding in [ x for x in first_code ]:
		code , cityName = coding.split("|")
		city_code[cityName] = code
	#	print cityName ,code 
	#print "*" * 30 
	#print city_first_code
	return city_code

def showCityName(tmp_dict,cityName):
	print "{} 的城市列表".format(cityName)
	for k ,v in tmp_dict.items():
		print k ,v  

def finalMes(tmp_url)
	web = urlopen(tmp_url)
	content = web.read()
	print content
	
	


if __name__ == "__main__":
	print getCityCode()
