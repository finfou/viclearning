#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'foo = 23 + 42 * 10'

import re
from collections import namedtuple

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))

scanner = master_pat.scanner('foo = 42')
m = scanner.match()
m.lastgroup, m.group()

def generate_tokens(pat, text):
	Token = namedtuple('Token', ['type', 'value'])
	scanner = pat.scanner(text)
	for m in iter(scanner.match, None):
		yield Token(m.lastgroup, m.group())

tokens = (tok for tok in generate_tokens(master_pat, 'foo = 42') if tok.type != 'WS')
for tok in tokens:
	print(tok)


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)