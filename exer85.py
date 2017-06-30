#!/usr/bin/python 
# -*- coding: utf-8 -*- 

if __name__ == '__main__':
    z = int(raw_input('input ur number:'))
    n1 = 1
    sum1 = 9
    cum1 = 1
    num1 = 9
    while n1:
	if sum1 % z == 0:
	    n1 = 0
	else:
 	    num1 *= 10
	    sum1 += num1
	    cum1 += 1
    print '%d can be %d of 9 divided: %d' % (z, cum1, sum1)
