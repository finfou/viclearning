#!/usr/bin/env python

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd']

for i in zip(a, b):
	print(i)

from itertools import zip_longest
for i in zip_longest(a,b,fillvalue=0):
	print(i)