#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


for line in sys.stdin:
    words = line.split('\n')
    for word in words:
        print('{0}\t{1}'.format(word, 1))
