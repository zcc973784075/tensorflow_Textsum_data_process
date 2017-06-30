#!/usr/bin/python 
# -*- coding: utf-8 -*- 

if __name__ == '__main__':
    n = int(raw_input('input your number:'))
    num = []
    for i in range(n):
        num.append(i+1)

    i = 0
    j = 0 
    m = 0

    while m < n-1:
	if num[i] != 0: j+=1
	if j == 3:
	    num[i] = 0
	    j = 0
	    m += 1
	i += 1
	if i == n: i=0
    i = 0
    while num[i] == 0: i+=1
    print num[i]
