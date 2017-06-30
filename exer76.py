#!/usr/bin/python 
# -*- coding: utf-8 -*-

def peven(n):
    s = 0.0
    for i in range(2, n+1, 2):
	s += 1.0/i
    return s 

def podd(n):
    s = 0.0
    for j in range(1, n+1, 2):
	s += 1.0/j
    return s 

if __name__ == '__main__':
    n = int(raw_input('input number:'))
    if n / 2.0 == 0:
	sum = lambda s:peven(n)
    else:
	sum = lambda s:podd(n)
print sum(n)

