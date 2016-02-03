#!/usr/bin/env python

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value>200}
print(p1)

# Note above method is faster than init dict from tuple:
p1 = dict((key, value) for key, value in prices.items if value>200)