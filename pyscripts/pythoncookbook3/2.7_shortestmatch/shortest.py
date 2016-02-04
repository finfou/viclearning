#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

str_pat = re.compile(r'\"(.*)\"')

short_str_pat = re.compile(r'\"(.*?)\"')

text = 'Computer say "no." Phone says "yes"'

print(str_pat.findall(text))

print(short_str_pat.findall(text))