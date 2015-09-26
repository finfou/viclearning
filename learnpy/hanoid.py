#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
	if n == 1:
		print("move %s from %s to %s" % (n, a, c))
	else:
		move(n-1, a, c, b)
		print("move %s from %s to %s" % (n, a, c))
		move(n-1, b, a, c)


if __name__ == "__main__":
	move(3, "a", "b", "c")