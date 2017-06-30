#!/usr/bin/python
# -*- coding:utf-8 -*-

if __name__ =='__main__':
	import time 
	start = time.clock()
	for i in range(3000):
		print i 
	end = time.clock()
	print end-start
