#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import textwrap

width = os.get_terminal_size().columns

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(dir(textwrap))

print(textwrap.fill(s, width))