#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'weiqi'

from urllib import request
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.found_uk_nav_side = False
        self.urls = []

    def handle_starttag(self, tag, attrs):
        if tag == "ul" and ('class', 'uk-nav uk-nav-side') in attrs:
            # print(attrs)
            print("Found uk_nav_side")
            self.found_uk_nav_side = True

        if self.found_uk_nav_side and tag == 'a' and attrs[0][0] == 'href':
            print(attrs[0][1])
            self.urls.append(attrs[0][1])

    def handle_endtag(self, tag):
        if tag == "ul" and self.found_uk_nav_side:
            print("Close uk_nav_side")
            self.found_uk_nav_side = False

def get_urls(url):
    pr = urlparse(url)
    data = wget(url)
    myparser = MyHTMLParser()
    myparser.feed(data)
    s = set(myparser.urls)
    print(s)
    return s

def wget(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k,v in f.getheaders():
            print('%s: %s' % (k, v))
        return data.decode('utf-8')


if __name__ == "__main__":
    python_tut_url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000#0'
    urls = get_urls(python_tut_url)
    print(urls)
    for url in urls:
        full_url = "http://www.liaoxuefeng.com" + url
        print(full_url)
        page = wget(full_url)
        filename = full_url.split('/')[-1]
        print(filename)
        os.system('mkdir -p ~/python-tut/')
        with open('/home/weiqi/python-tut/%s.html'%filename, 'w') as f:
            f.write(page)


