#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import os
import sys
from collections import namedtuple

if len(sys.argv) != 2:
	sys.exit(0)

fileName = sys.argv[1]

BitmapInfo = namedtuple('BitmapInfo', ['sign', 'size', 'reserved', 'offset', 'header', 'width', 'height', 'const', 'colors'])

with open(fileName, 'rb') as f:
	data = f.read(30)
	meta_info = BitmapInfo(*struct.unpack('<2sIIIIIIHH', data))
	print(meta_info)
	# meta_info = struct.unpack('<ccIIIIIIHH', data)
	# print("%s%s:" % (meta_info[0], meta_info[1]))
	# print("Size of image: %s", meta_info[2])
	# print("Width: %s" % meta_info[6])
	# print("Height: %s" %meta_info[7])
