#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Field import Field

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')
