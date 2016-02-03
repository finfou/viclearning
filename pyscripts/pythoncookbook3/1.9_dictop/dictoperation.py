#!/usr/bin/env python

a = {
	'x': 1,
	'y': 2,
	'z': 3
}

b = {
	'w': 1,
	'y': 2,
	'z': 12
}

print(a.keys() & b.keys())
print(a.keys()-b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys()-{'z'}}

print(c)
