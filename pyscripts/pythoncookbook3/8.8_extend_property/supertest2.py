#!/usr/bin/env python

class A(object):
    def __init__(self):
        print('A.__init__')
        super().__init__()

class B(object):
    def __init__(self):
        print('B.__init__')
        super().__init__()

class C(A, B):
    def __init__(self):
        print('C.__init__')
        super().__init__()

c = C()
print(C.__mro__)
print(B.__mro__)