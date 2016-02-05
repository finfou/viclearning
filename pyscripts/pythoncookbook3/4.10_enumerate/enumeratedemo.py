#/usr/bin/env python

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
	print(idx, val)

from collections import defaultdict

word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
	lines = f.readlines()

for idx, line in enumerate(lines):
	words = [w.strip().lower() for w in line.split()]
	for word in words:
		word_summary[word].append(idx)