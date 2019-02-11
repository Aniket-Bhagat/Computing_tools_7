#!/usr/bin/python

import re
s=raw_input("input String: ")

if re.search(r"a.*?b$",s):
	print('Pattern matched')
else:
	print('Pattern not matched')