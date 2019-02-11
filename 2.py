#!/usr/bin/python

import re
s=raw_input("input String: ")

if s=='\n':
	print 'Dont press Enter kye. Give some input'

if re.search(r"\D",s):
	if re.search(r"[^a-z]",s):
		if re.search(r"[^A-Z]",s):
			# print ('Invalid')
			if re.search(r"[a-zA-Z\d\s]",s):
				print "[Mixture of more than one charecter set]"
			else:
				print "[Special Charecter set]"
		else:
			print "[A-Z]"
	else:
		print "[a-z]"
else:
	print "[0-9]"