#!/usr/bin/python

import re
s=raw_input("input String: ")

if re.search(r"ab*",s):
	print('Pattern matched')
else:
	print('Pattern not matched')