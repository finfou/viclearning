#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

datapat = re.compile(r'\d+/\d+/\d+')
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if datapat.match(text1):
	print('yes')
else:
	print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datapat.match('11/27/2012')
