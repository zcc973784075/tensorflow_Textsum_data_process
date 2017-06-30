#!/usr/bin/python 
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    i = 0 
    j = 1 
    x = 0
    while (i < 5):
	x = j * 4
	for i in range(5):
	    if (x%4 != 0):
		break
	    else:
		i += 1
	    x = (x/4) * 5 + 1
	j += 1
    print x, j
