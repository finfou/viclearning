#!/usr/bin/env python
items = ['a', 'b', 'c']

from itertools import permutations
from itertools import combinations

for p in permutations(items):
	print(p)

for p in permutations(items, 2):
	print(p)


for c in combinations(items, 3):
	print(c)

for c in combinations(items, 2):
	print(c)