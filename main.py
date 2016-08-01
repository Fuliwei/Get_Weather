#!/usr/bin/python 
#coding:utf-8
from cityFirstCode import getCityCode ,showCityName,finalMes
def main():
#	print cityName
	firstCode = getCityCode()
	showCityName(firstCode,cityName="中国")
	cityName = raw_input("请输入要查询天气城市的省/直辖市名称:")
	if cityName not in firstCode.keys():
		print "请从%s的城市列表中选取" %(cityName)
	else :
		codeOne = firstCode[cityName]
		tmp_url = "http://m.weather.com.cn/data5/city%s.xml" %(codeOne)
		second_code_dict =  getCityCode(tmp_url)#获取的格式为  {'北京': '0101'}
		print "codeTwo :" 
		print second_code_dict[cityName]
		tmp_url = "http://m.weather.com.cn/data5/city%s.xml" %(second_code_dict[cityName])
		third_code_dict = getCityCode(tmp_url)
		##third_name_dict这个用来打印显示城市列表
		third_name_dict =  {k:v for k ,v in enumerate(third_code_dict.keys())}
		showCityName(third_name_dict,cityName)
		secondCityName = raw_input("请输入要查询天气的具体城市")
		if secondCityName in third_name_dict.values():
			tmp_url = "http://m.weather.com.cn/data5/city{}.xml".format(third_code_dict[secondCityName])
			end_code_dict = getCityCode(tmp_url)
			print end_code_dict
			for code  ,v  in end_code_dict.items():
				get_mes_code = code 
				print get_mes_code
			tmp_url = "http://m.weather.com.cn/data5/city{}.xml".format(get_mes_code)
			finalMes(tmp_url)
			#print "天气信息抓取如下： "
			#print final_mes_dict 
		else :
			print "请从%s的城市列表中选取" %(cityName)
if __name__ == "__main__":
	main()
