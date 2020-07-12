# -*- coding: utf-8 -*-

import threading
from concurrent.futures import ThreadPoolExecutor, wait
import os

class ScannerWithThread(threading.Thread):
	def __init__(self, cmd_type, ip_list, ip, port_list, sink_file, parallel):
		super().__init__()
		self.cmd_type = cmd_type
		self.ip_list = ip_list
		self.ip = ip
		self.port_list = port_list
		self.sink_file = sink_file
		self.file = None
		self.parallel = parallel
		self.executor = ThreadPoolExecutor(max_workers=parallel)

	def run(self):
		if self.sink_file is not None:
			self.file = open(self.sink_file, 'a+')
		if self.cmd_type == 'ping':
			if self.ip_list is None:
				raise Exception("ip list is required")
			all_task = [self.executor.submit(self.run_ping, ip) for ip in self.ip_list]
			wait(all_task)
			if self.file is not None:
				for task in all_task:
					self.file.write(task.result+'\n')
				self.file.close()
		if self.cmd_type == 'tcp':
			if self.port_list is None:
				raise Exception("port list is required")
			all_task = [self.executor.submit(self.run_tcp, port) for port in self.port_list]
			wait(all_task)
			if self.file is not None:
				for task in all_task:
					self.file.write(task.result+'\n')
				self.file.close()

	def run_ping(self, ip):
		cmd_str = 'ping -c 1 -i 0.5 %s >> /dev/null' % (ip,)
		ret = os.system(cmd_str)
		ret_str = ""
		if ret < 1:
			ret_str = '{"%s" : "ok"}' % (ip, )
		else:
			ret_str = '{"%s" : "fail"}' % (ip, )
		return ret_str

	def run_tcp(self, port):
		cmd_str = 'nc -vz %s %s >> /dev/null' % (self.ip, port, )
		ret = os.system(cmd_str)
		ret_str = ""
		if ret == 0:
			ret_str = '{"%s" : "ok"}' % (port, )
		else:
			ret_str = '{"%s" : "fail"}' % (port, )
		return ret_str
