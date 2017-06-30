#!/usr/bin/python 
# -*- coding: utf-8 -*- 

if __name__ =="__main__":
    person = {'li':20, 'Ghao':12}
    m = 'li'
    for key in person.keys():
	if person[m]<person[key]:
		m = key
    print '%s-%d' % (m, person[m])
