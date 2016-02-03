#!/usr/bin/env python

prices = {
	'ACME': 45.23,
	'AAPL': 612.22,
	'IBM' : 205.55,
	'HPQ' : 37.20,
	'FB' : 10.74
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
