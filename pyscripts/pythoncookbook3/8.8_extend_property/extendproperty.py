#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
	    return self._name

	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected a string.')
		self._name = value

	@name.deleter
	def name(self):
		raise AttributeError("Can't delete attribute")

class SubPerson(Person):
	@property
	def name(self):
	    print('Getting name')
	    return super(SubPerson, self).name

	@name.setter
	def name(self, value):
		print('Setting name to', value)
		super(SubPerson, SubPerson).name.fset(self, value)

	@name.deleter
	def name(self):
		print('Deleting name')
		del super(SubPerson, SubPerson).name

s = SubPerson('Guido')
print(s.name)

s.name = 'Larry'
print(s.name)
# s.name = 42
