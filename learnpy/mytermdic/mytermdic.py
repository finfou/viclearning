#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import requests
from termcolor import colored
from bs4 import BeautifulSoup

def lookup(word):
	url = 'http://dict.youdao.com/search?q='
	r = requests.get(url+word)
	content = r.text
	soup = BeautifulSoup(content, 'html.parser')

	try:
		pronounces = soup.find_all('span', 'pronounce')
		for pronouce in pronounces:
			li = [text for text in pronouce.stripped_strings]
			print(colored("%s %s" % (li[0], li[1]), 'cyan'))
		meanings = soup.find_all('div', class_="trans-container", limit=1)
		print(meanings[0].ul.text)
	except:
		print("Can\'t find %s" % word)

if __name__ == '__main__':
	args = sys.argv[1:]
	word = " ".join(args)
	if word:
		lookup(word)
