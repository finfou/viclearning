#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import signal

alphabet = "abcdefghijklmnopqrstvuwxyz"

def found(word, args, cwd = None, shell = True):
	child = subprocess.Popen(args,
		shell = shell,
		stdin = subprocess.PIPE,
		stdout = subprocess.PIPE,
		cwd = cwd,
		universal_newlines = True)
	child.stdout.readline()
	(stdout, stdint) = child.communicate(word)
	if ": " in stdout:
		stdout = stdout.rstrip("\n")
		left, candidates = stdout.split(": ", 1)
		candidates = candidates.split(", ")
		for item in candidates:
			if item[0] != word[0]:
				candidates.remove(item)
				candidates.append(item)
		return candidates
	else:
		return None

def correct(word):
	candidates1 = found(word, 'aspell -a')
	if not candidates1:
		print("No suggestion")
		return
	print(candidates1[0])

def signal_handler(signal, frame):
	sys.exit(0)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	while True:
		input = raw_input()
		correct(input)