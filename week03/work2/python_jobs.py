import time
import requests
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, wait

def normal_salary(salary):
	normal1 = salary.split('·')[0].split('-')
	min = int(normal1[0].split('k')[0])
	max = int(normal1[1].split('k')[0])
	return (max + min) * 500

def extract_job_info(limit, url, area_name):
	job_list = []
	count = 15
	if limit > 100:
		count = 10
	'''
	f = open('11.html', 'r', encoding='utf-8')
	selector = etree.HTML(f.read())
	'''
	header = {'user-agent': UserAgent().random}
	r = requests.get(url,headers=header)
	r.encoding = 'utf-8'
	selector = etree.HTML(r.text)
	row_num = str(0)
	i = 0
	for item in selector.xpath('//*[@id="s_position_list"]/ul/li'):
		p_name = item.xpath('div[1]/div[1]/div[1]/a/h3/text()'.format(row_num))[0]
		# 暂时不去重
		p_local = item.xpath('div[1]/div[1]/div[1]/a/span/em/text()'.format(row_num))[0]
		p_area = area_name
		p_salary = normal_salary(item.xpath('div[1]/div[1]/div[2]/div/span/text()'.format(row_num))[0])
		job_list.append([p_name, p_area, p_local, p_salary])
		i += 1
		if i > count:
			break

	return job_list
	
if __name__ == "__main__":
	run('21aa32b779f94a0abf8c00c6ecb76556', '北京')
	run('39fc661a87214fceb89d0021916a2cdd', '上海')
	run('5a6d1b0a7a8a4553bc94149571aa72ce', '广州')
	run('f89fc9c5fd2342c0a50095b2e9dca976', '深圳')

def run(area_id, area_name)
	# 地区, 首页html, 每页多少条数据, 总共抓多少条数据
    # 最小子任务即抓取一个网页
	page_list = [(15, 'https://www.lagou.com/zhaopin/Python/?filterOption=3&sid=%s' % (area_id, ))]
	for i in range(2, 8):
		tmp_page = 'https://www.lagou.com/zhaopin/Python/%d/?filterOption=3&sid=%s' % (i, area_id, )
		page_list.append((15*i, tmp_page))

	'''
	for page in page_list:
		print(page[1])
		myurl = page[1]
		header = {'user-agent': UserAgent().random}
		r = requests.get(myurl,headers=header)
		r.encoding = 'utf-8'
	'''
	executor = ThreadPoolExecutor(max_workers=4)
	all_task = [executor.submit(extract_job_info, page[0],page[1]) for page in page_list]
	wait(all_task)
	'''
	for task in all_task:
		print(task.result())
	'''
	columns_name = ["name", "area", "local", "salary"]
	file_name = "job_info.csv"
	for task in all_task:
		pd.DataFrame(columns=columns_name, data=task.result()).to_csv(file_name, mode='a', encoding='utf-8', header=False)
