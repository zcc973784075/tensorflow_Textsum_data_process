#!/usr/bin/python 
# -*- coding:utf-8 -*-

if __name__ =='__main__':
    from sys import stdout 
    filename = raw_input('input a filename:\n')
    fp = open(filename, 'w')
    ch = raw_input('input a letter:\n')
    while ch != '#':
	fp.write(ch)
	stdout.write(ch)
	ch = raw_input('')
    fp.close()	
