#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def matchcase(word):
	def replace(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		if text.islower():
			return word.lower()
		if text[0].isupper():
			return word.capitalize()
		return word
	return replace

text = 'UPPER PYTHON, lower python, Mixed Python'

newtext = re.sub('python', matchcase('snake'), text, flags = re.IGNORECASE)

print(newtext)