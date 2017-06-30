#!/usr/bin/python 
# -*- coding: utf-8 -*- 

if __name__ =="__main__":
    n = 0
    p = raw_input('input your number:')
    for i in range(len(p)):
	n = n*8 + ord(p[i]) - ord('0')
    print n
