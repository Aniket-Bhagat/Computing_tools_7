#!/usr/bin/python

print 'Checking for e-mail id format'
import re
s=raw_input("input String: ")
s=(s.split(','))

for i in s:
	if re.search(r"^[\w\S]+@[a-z]+[\.][a-z]*[\.]?[a-z]*[\.]?[a-z]*$",i):
		print('Pattern matched')
	else:
		print('Pattern not matched')