#！/usr/bin/env python
# -*- coding: utf-8 -*-

s = '{name} has {n} messages.'
name = 'Guido'
n = 37
print(s.format_map(vars()))

class Info:
	def __init__(self, name, n):
		self.name = name
		self.n = n

a = Info('Guido', n)
print(s.format_map(vars(a)))

print(vars(a))

class safesub(dict):
	def __missing__(self, key):
		return '{{{key}}}'.format(key=key)

s1 = '{{{key}}}'.format(key='weiqi')  # when using format or format_map, '{' and '}' need escape
print(s1)
s2 = s1.format(weiqi='yao')
print(s2)
del n

print(s.format_map(safesub(vars())))

import sys

def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'weiqi'
n = 38

print(sub('Hello {name}'))
print(sub('You have {n} balls'))
print(sub('{color}'))