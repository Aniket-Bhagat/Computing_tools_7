#!/usr/bin/python

print 'Checking for string with capital letter, followed by\nan arbitrary number of alphanumeric characters'
import re
s=raw_input("input String: ")

if re.search(r"[A-Z][\w]+$",s):
	print('Pattern matched')
else:
	print('Pattern not matched')