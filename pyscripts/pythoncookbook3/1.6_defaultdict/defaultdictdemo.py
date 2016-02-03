#!/usr/bin/env python

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
d['a'].add(4)

print(d['b']) # surprise: this is not null
