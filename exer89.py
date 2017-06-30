#!/usr/bin/python
# -*- coding:utf-8 -*- 

from sys import stdout 
if __name__=='__main__':
    aa = int(raw_input('input a four-digit number:'))
    n = []
    n.append(aa/1000)
    n.append(aa%1000/100)
    n.append(aa%100/10)
    n.append(aa%10)

    for i in range(2):
	n[i], n[3-i] = n[3-i], n[i]

    for i in range(4):
	n[i] += 5
	n[i] %= 10

    for i in range(4):
	stdout.write(str(n[i]))
