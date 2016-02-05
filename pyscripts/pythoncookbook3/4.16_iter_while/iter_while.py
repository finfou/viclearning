#!/usr/bin/env python

CHUNKSIZE = 8192

def reader(s):
	for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
		pass

# iter's first arguments is a callable object, and 2nd parameter is the end condition