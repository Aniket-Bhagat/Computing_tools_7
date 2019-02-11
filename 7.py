#!/usr/bin/python

print 'Checking for word at end of string, with optional punctuation (.)'
import re
s=raw_input("input String: ")

if re.search(r"\w.+[\.]*$",s):
	print('Pattern matched')
else:
	print('Pattern not matched')