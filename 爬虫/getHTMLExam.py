from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import random

# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', uset='root', passwd=None, db='mysql', charset='utf8')
# cur = conn.cursor()
# cur.execute("USE ")

def getContent(year, page, province):
	url = "http://www.huatu.com/a/ztk/list/"+province+"/1/"+year+"/t/"+page+".html"
	html = urlopen(url)
	bsObj = BeautifulSoup(html)
	divs = bsObj.findAll("div",{"class":"con_stAll_tg"})	
	try:
		for div in divs:
			ps = div.findAll("p")
			# p[0]单选多选
			# p[1]题目
			# p[2]A、
			# p[2]B、
			# p[3]C、
			# p[4]D、
			for p in ps:
				# 如果p标签了有img标签
				print(p.get_text())


		title = bsObj.find("h4").get_text()
	finally:
		print("Empty !!!")

def getExamWithProvinceAndYear(province, year):
	url = "http://www.huatu.com/a/ztk/list/"+province+"/1/"+year+"/t/1.html"
	html = urlopen(url)
	bsObj = BeautifulSoup(html)
	pages = bsObj.find("div",{"class":"fanye","id":"fenye"}).findAll("a")
	for page in pages:
		if page.get_text().isdigit():
			text = page.get_text()
			getContent(year, text , province)
			speed = random.randint(2,5)
			time.sleep(speed)

def getExamBy():
	years = ("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016")
	for province in range(1, 34):
		for year in years:
			getExamWithProvinceAndYear(str(province), year)



getExamBy()





