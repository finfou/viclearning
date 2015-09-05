#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Field import Field

class IntegerField(Field):

	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

