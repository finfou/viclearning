#!/usr/bin/env python

import struct

class Structure:
	def __init__(self, bytedata):
		self._buffer = memoryview(bytedata)

class StructField:
	def __init__(self, format, offset):
		self.format = format
		self.offset = offset

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			r = struct.unpack_from(self.format, instance._buffer, self.offset)
			return r[0] if len(r) == 1 else r

class PolyHeader(Structure):
	file_code = StructField('<i', 0)
	min_x = StructField('<d', 4)
	min_y = StructField('<d', 12)
	max_x = StructField('<d', 20)
	max_y = StructField('<d', 28)
	num_polys = StructField('<i', 36)

with open('test.dat', 'rb') as f:
	phead = PolyHeader(f.read(40))
	print(phead.file_code, phead.min_x, phead.min_y)
