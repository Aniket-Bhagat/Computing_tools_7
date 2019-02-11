#!/usr/bin/python

import re
s=raw_input("input String: ")

if re.search(r"\D",s):
	if re.search(r"[^a-z]",s):
		if re.search(r"[^A-Z]",s):
			print ('Not any Perticular charecter set may be a Mixture')
		else:
			print "[A-Z]"
	else:
		print "[a-z]"
else:
	print "[0-9]"