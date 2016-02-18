#!/usr/bin/env python

class B(object):
	def __repr__(self):
		return "<instance of %s>" % self.__class__.__name__

	@property
	def name(self):
	    return self._name

	@name.setter
	def name(self, value):
		self._name = value
	

class C(B):
	pass

class D(C):
	pass

c = C()
c.name = "Weiqi"
d = D()
print(type(super(C, C).name))
print(type(C.name.__set__))
print(type(C.name.fset))
print(type(C.name.setter))
print(type(c.name))
print(type(super(C, c).name))

print(super(C, C).name.fget(c))
# super(C, c).name = "Yao"
print(c.name)
super(C, C).name.fset(c, "Finfou")
print(c.name)

print("super(C,c)")
print(super(C, c).__repr__)
print("super(C,C)")
print(super(C,C).__repr__)
print("super(C, d)")
print(super(C, d).__repr__)
print(super(D, d).__repr__)
print("super(C, D)")
print(super(C, D).__repr__)
print("super(C)")
print(super(C).__repr__)