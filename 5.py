#!/usr/bin/python

print 'Checking for pattern "$[followed by digits].[2 digits]" i.e. $xxx.xx'

import re
s=raw_input("input String: ")

if re.search(r"^\$[\d]+[\.][\d]{2}$",s):
	print('Pattern matched')
else:
	print('Pattern not matched')