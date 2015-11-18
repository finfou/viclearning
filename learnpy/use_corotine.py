#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    print(1)
    r = ''
    while True:
        n = yield r
        print('[CONSUMER] %s' % n)
        if not n:
            print('[CONSUMER] start')
            return
        print('[CONSUMER] Consuming %s' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    print("PD")
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
    
c = consumer()
produce(c)