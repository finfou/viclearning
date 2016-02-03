#!/usr/bin/env python

def dedup(items, key=None):
	seen = set()
	for item in items:
		var = item if key is None else key(item)
		if var not in seen:
			yield item
		seen.add(var)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedup(a, key=lambda d:(d['x'],d['y']))))
print(list(dedup(a, key=lambda d:(d['x'],))))