#!/usr/bin/env python

mylist = [1,4,-5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0] #sequence
(n for n in mylist if n > 0) #generator

values = ['1', '2', '-3', '-', 'N/a', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

morethen5 = [n>5 for n in counts]

print(list(compress(addresses, morethen5)))

data = zip(addresses, morethen5)
print(data)
items = [key[0] for key in data if key[1]]
print(items)
