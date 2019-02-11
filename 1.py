#!/usr/bin/env python

import re
s=raw_input("input phone no. in xxx-xxx-xxxx format:\n")
if re.match(r"[7-9][0-9]{2}[-][0-9]{3}[-][0-9]{4}$",s):		# in phone number first number is always 7 or 8 or 9 only
	print "Is a Phone number"
else:
	print "Not a Phone number"