#!/usr/bin/env python3

count = 0

def show_count():
	print(count)
	

def set_count(c):
	global count
	count = c
	
if (__name__ == "__main__"):
	#print(__name__)
	count = 5
	set_count(7)
	show_count()
	
#print(__name__)
