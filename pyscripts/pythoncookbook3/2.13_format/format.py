#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'Hello World'

print(text.ljust(20))
print(text.rjust(20))
print(test.center(20))

print(text.ljust(20, '='))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '=<20s'))
print(format(text, '=^20s'))