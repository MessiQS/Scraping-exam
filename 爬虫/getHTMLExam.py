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
	category_of_problem = ""
	try:
		for div in divs:
			ps = div.findAll("p")
			# 处理p标签内容
			# handleJSON(year, province, ps)
			type_new = div.findPrevious('h5', {"class":"shitiCon01tit"})
			#如果有新的类型
			if !len(type_new):
				category_of_problem = new_category_of_problem

			handleJSON(year, province, ps, category_of_problem)
			

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

def handleJSON(year, province, psTag, category_of_problem): 
	type_of_problem, number, analysis, recipe, expand = ""
	
	for p in ps:
		# 如果p标签了有img标签
		imgs = p.findAll("img")
		if len(imgs):
			for img in imgs:
				print(img.get('src'))
		#判断p的类型
		#单选多选
		if "单选题" in p.get_text():
			type_of_problem = "单选题"
		#题号
		# if len(p.find("span"))
		# 	number = p.find("span").get_text()
		#题目
		if "【解析】" in p.get_text():
			analysis = p.get_text() 

		if "【技巧】" in p.get_text():
			recipe = p.get_text()

		if "【拓展】" in p.get_text():
			expand = p.get_text()

	# p[0]单选多选,题号
	# p[1]题目
	# p[2]A、
	# p[2]B、
	# p[3]C、
	# p[4]D、
	question = ps[1].get_text()
	option_A = ps[2].get_text()
	option_B = ps[3].get_text()
	option_C = ps[4].get_text()
	option_D = ps[5].get_text()
	answer = ps[6].get_text()

	data = {
		"year": year,
		"province": province,
		"type_of_problem":type_of_problem,
		"number":number,
	 	"category_of_problem":category_of_problem,
		"question": question,
		"option_A" : option_A,
		"option_B" : option_B,
		"option_C" : option_C,
		"option_D" : option_D,
		"answer" : answer,
		"analysis": analysis,
		"recipe" : recipe,
		"expand": expand
	}
	return data


getContent("2011", "18", "3")




