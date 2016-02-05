#!/usr/bin/env python

import heapq

a = [1, 4, 5, 9]
b = [2, 3, 7]

for c in heapq.merge(a, b):
	print(c)