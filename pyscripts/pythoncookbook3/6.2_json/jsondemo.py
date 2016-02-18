#!/usr/bin/env python

import json

data = {
	'name' : 'ACME',
	'shares': 100,
	'price' : 512.43
}

json_str = json.dumps(data)

data = json.loads(json_str)

class JSONObject:
	def __init__(self, d):
		self.__dict__ = d

data1 = json.loads(json_str, object_hook=JSONObject)

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

p = Point(2,3)

def serialize_instance(obj):
	d = {'__classname__' : type(obj).__name__}
	d.update(vars(obj))
	return d

classes = {
	'Point': Point
}

def deserialize_obj(d):
	clsname = d.pop('__classname__', None)
	if clsname:
		cls = classes[clsname]
		obj = cls.__new__(cls)
		for key, value in d.items():
			setattr(obj, key, value)
		return obj
	else:
		return d

s = json.dumps(p, default=serialize_instance)
a = json.loads(s, object_hook=deserialize_obj)