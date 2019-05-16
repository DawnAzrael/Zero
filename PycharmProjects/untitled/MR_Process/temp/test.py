#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys


def test(a):
    if float(a) >= 0.325 and float(a) <= 0.675:
        print(a)


if __name__ == '__main__':
    test(sys.argv[1])
