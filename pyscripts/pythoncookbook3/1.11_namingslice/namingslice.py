#!/usr/bin/env python

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'

PRICE = slice(31,37)
SHARE = slice(20,23)

cost = float(record[PRICE]) * int(record[SHARE])
print(cost)

# Following code use slice.indices() to protected IndexError
a = slice(5,50,2)
s = 'HelloWorld'
#print(type(*a.indices(len(s))))
print(*a.indices(len(s)))
a.indices(len(s))
for i in range(*a.indices(len(s))):
	print(s[i])