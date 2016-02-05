#!/usr/bin/env python

from itertools import dropwhile

with open('/etc/pasword') as f:
	for line in dropwhile(lambda line: line.startwith('#'), f):
		print(line, end='')

from itertools import islice

items = ['a', 'b', 'c', 1,2,3,4]
for x in islice(items, 3, None):
	print(x)