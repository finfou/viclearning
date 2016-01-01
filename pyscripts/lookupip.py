#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup as bs4

serviceURL = "http://1212.ip138.com/ic.asp"
ip_pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

def lookup():
	resp = requests.get("http://1212.ip138.com/ic.asp")
	resp.text
	ps = re.findall(ip_pattern, resp.text)
	return ps

if __name__ == "__main__":
	print(lookup())

