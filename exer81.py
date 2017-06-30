#!/usr/bin/python 
# -*- coding: utf-8 -*- 

a = 809
for i in range(10, 100):
    b = a * i + 1
    if b >= 1000 and b <= 10000 and 8*i < 100 and 9*i >= 100:
	print b, '/', i, '=809 * ', i, '+', b % i
