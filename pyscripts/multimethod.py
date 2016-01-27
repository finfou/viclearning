#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a copy of implementation of multimethod from
http://www.artima.com/weblogs/viewpost.jsp?thread=101605

Which use decorator to simulate method overload.
"""

registry = {}

class MultiMethod(object):

	def __init__(self, name):
		self.name = name
		self.typemap = {}
	def __call__(self, *args):
		types = tuple(arg.__class__ for arg in args)
		function = self.typemap.get(types)
		if function is None:
			raise TypeError("no match")
		return function(*args)
	def register(self, types, function):
		if types in self.typemap:
			raise TypeError("duplicate registration")
		self.typemap[types] = function

def multimethod(*types):
	def register(function):
		function = getattr(function, "__lastreg__", function) #multi decorator 
		name = function.__name__
		mm = registry.get(name)
		if mm is None:
			mm = registry[name] = MultiMethod(name)
		mm.register(types, function)
		mm.__lastreg__ = function # multi decorator
		return mm
	return register

if __name__ == '__main__':

	@multimethod(int, int)
	def foo(a, b):
		print(a+b)

	@multimethod(int, int, int)
	def foo(a, b, c):
		print(a*100+b*10+c)

	foo(10,2)
	foo(1,2,3)