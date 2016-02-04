#!/usr/bin/env python

line = 'asdf fjdk; afed, fjek,asdf, foo'
line1 = 'asdf fjdk afed fjek asdf foo'
import re

def split1():
	print(line1.split(' '))

split1()

def split2():
	print(re.split(r'[;,\s]\s*',line))

split2()

def split3():
	print(re.split(r'(;|,|\s)\s*', line))

split3()

def split4():
	print(re.split(r'(?:;|,|\s)\s*', line))

split4()

print(5)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + [''] # add  [''] to align the number of elements
print(values)
print(delimiters)

print(''.join(v+d for v, d in zip(values, delimiters)))