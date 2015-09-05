#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Model import Model
from IntegerField import IntegerField
from StringField import StringField

print(type(Model))

class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField("password")

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()