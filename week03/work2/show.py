#-*- coding: utf-8 -*-
import csv
from datetime import datetime
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
filename='job_info.csv'
with open(filename,'r', encoding='utf8')as file:
	reader=csv.reader(file)
	header_row=next(reader)

	area,salary=[],[]
	for row in reader:
		curr_area = row[3]
		print(type(curr_area))
		curr_salary = row[4]
		area.append(curr_area)
		salary.append(int(curr_salary))
	print(area)
	print(salary)
	plt.plot(area, salary)
	plt.show()
