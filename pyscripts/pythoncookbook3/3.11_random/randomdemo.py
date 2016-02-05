#!/usr/bin/env python

import random

values = [1,2,3,4,5,5]
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 3))

random.shuffle(values)
print(values)

print(random.randint(1,10))

print(random.random())

print(random.getrandbits(200))

random.seed() # Seed based on system time or os.urandom()