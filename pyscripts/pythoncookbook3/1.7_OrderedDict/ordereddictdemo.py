#!/usr/bin/env python

from collections import OrderedDict
import json

def print_dict(d):
	d['foo'] = 2
	d['bar'] = 1
	d['spam'] = 3
	d['grok'] = 4

	for key in d:
		print(key, d[key])
	print(json.dumps(d))

if __name__ == '__main__':
	print("Using normal dict")
	container = {}
	print_dict(container)
	print("Using collections' OrderedDict")
	container = OrderedDict()
	print_dict(container)


# Using normal dict
# grok 4
# spam 3
# foo 2
# bar 1
# {"grok": 4, "spam": 3, "foo": 2, "bar": 1}
# Using collections' OrderedDict
# foo 2
# bar 1
# spam 3
# grok 4
# {"foo": 2, "bar": 1, "spam": 3, "grok": 4}