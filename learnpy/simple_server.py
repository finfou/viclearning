#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'weiqi'

from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

httpd = make_server('', 8001, application)
print('Serving HTTP on port 8001...')

httpd.serve_forever()