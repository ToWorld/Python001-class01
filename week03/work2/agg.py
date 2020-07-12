#-*- coding: utf-8 -*-
from numpy import *
import pandas as pd
import csv
from datetime import datetime
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
filename='job_info.csv'
with open(filename,'r', encoding='utf8')as file:
	reader=csv.reader(file)
	header_row=next(reader)

	data = dict()
	for row in reader:
		curr_area = row[2]
		curr_salary = row[4]
		if curr_area in data:
			data[curr_area].append(int(curr_salary))
		else:
			data[curr_area] = [int(curr_salary)]

	agg_list = []
	for area_name in data:
		avg = mean(data[area_name])
		agg_list.append([area_name, avg])

	print(agg_list)
	columns_name = ["地区", '平均待遇']
	pd.DataFrame(columns=columns_name, data=agg_list).to_csv('agg.json', mode='a', encoding='utf-8', header=False)
