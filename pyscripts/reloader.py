#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reload modules after modification
Usage:
	python reloader.py [module_name]
"""

import sys
import os

mtimes = {}

def do_reload(handler=None):
	for module in sys.modules.values():
		filename = getattr(module, '__file__', None)
		if (not filename) or (not os.path.isfile(filename)):
			continue

		if filename[-4:] in ('.pyc', '.pyo', '.pyd'):
			filename = filename[:-1] # transform to .py

		try:
			mtime = os.stat(filename).st_mtime
		except OSError:
			continue

		old_time = mtimes.get(module)
		if old_time is None:
			mtimes[module] = mtime
		elif old_time < mtime:
			try:
				reload(module)
				mtimes[module] = mtime
				if handler:
					handler(module)
			except ImportError:
				pass

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.stderr.write(__doc__)
		sys.exit(1)

	test_module_name = sys.argv[1]
	from importlib import reload, import_module
	try:
		import_module(test_module_name)
	except ImportError as e:
		print(str(e))
		sys.exit(1)

	import time
	def handler(module):
		print(dir(module))

	print("Start relaoding module '%s' automatically..." % test_module_name)
	while True:
		try:
			do_reload(handler)
			time.sleep(2)
		except KeyboardInterrupt:
			break