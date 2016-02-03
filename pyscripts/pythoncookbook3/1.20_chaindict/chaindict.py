#!/usr/bin/env python

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['z'])

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
print(values['x'])

values = values.parents
values['x']

merged = b.update(a) # no return value
print(b) #b got changed,
print(merged) # None