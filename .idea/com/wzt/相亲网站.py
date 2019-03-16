#!/usr/bin/python
#coding:utf-8

####################
#爬取相亲网站
#www.zhenai.com/zhenghun
#version:1.0
######################
import requests
import re                  #载入所需模块

class zhenghunlist():
	url='http://www.zhenai.com/zhenghun'  #周报系统日志网址的前缀
	
	def __init__(self, addr):
		self.url=zhenghunlist.url+"/"+addr        #网址=网址前缀+用户id
	def getHtml(self):                             #获取网页内容
		try:
			print(self.url)
			html = requests.get(self.url).content.decode("utf-8")
			return html
		except Exception:
			print('url error!!')
			
	def getTitle(self):                          #应用正则表达式提取网页中的日志标题
		html=self.getHtml()
		reg = '<a href="http://album.zhenai.com/u/[0-9]+"[^>]*>[^<]+</a>'
		
		m = re.findall(reg,html)
		return m
def main():
   
	users = ["chaoyang1","dongcheng"]
    
	for i in users:
		zheng = zhenghunlist(i)         #对象初始化

		girlList = zheng.getTitle()    #使用对象方法
		for girl in girlList:
			a = girl.split('"')
			print(a[1])
			index = girl.rfind('<')
			print(girl[index-2:index])
			

if __name__== '__main__':
	main()