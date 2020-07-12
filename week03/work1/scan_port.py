# -*- coding: utf-8 -*-

import argparse
import os
import sys
from parallel import scanner_with_thread, scanner_with_process

# 增加参数说明
parser = argparse.ArgumentParser(description='scan port parameter')
parser.add_argument('-n', type=int, default=1)
parser.add_argument('-f', type=str, default='ping')
parser.add_argument('-ip', type=str, default=None)
parser.add_argument('-w', type=str, default=None)
parser.add_argument('-m', type=str, default='proc')
args = parser.parse_args()

def get_port_list():
	ret_port_list = []
	for i in range(1, 1025):
		ret_port_list.append(i)
	return ret_port_list

def get_ip_list():
	if args.ip is None:
		raise Exception("ip is required")
	ip_list = args.ip.split('-')
	if len(ip_list) == 1:
		return ip_list
	tmp_ip1 = ip_list[0]
	fields = tmp_ip1.split('.')
	prefix = fields[0] + '.' + fields[1] + '.' + fields[2]
	start_field = int(fields[3])
	end_field = int(ip_list[1].split('.')[3])
	ret_ip_list = []
	for i in range(start_field, end_field+1):
		ret_ip_list.append(prefix+'.'+str(i))
	return ret_ip_list

def multi_thread():
	ip_list = []
	port_list = []
	if args.f == 'ping':
		ip_list = get_ip_list()
	if args.f == 'tcp':
		port_list = get_port_list()

	t1 = scanner_with_thread.ScannerWithThread(cmd_type=args.f,
											   ip_list=ip_list,
											   sink_file=args.w,
											   ip=args.ip,
											   port_list=port_list,
											   parallel=args.n)
	t1.start()
	t1.join()
	

def multi_process():
	ip_list = []
	port_list = []
	if args.f == 'ping':
		ip_list = get_ip_list()
	if args.f == 'tcp':
		port_list = get_port_list()
	p1 = scanner_with_process.ScannerWithProcess(cmd_type=args.f,
											   ip_list=ip_list,
											   sink_file=args.w,
											   ip=args.ip,
											   port_list=port_list,
											   parallel=args.n)
	p1.run()
		
if __name__ == "__main__":
	if args.m == 'thread':
		multi_thread()
	if args.m == 'proc':
		multi_process()
