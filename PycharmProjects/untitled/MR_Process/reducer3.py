#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys


curr_rule = None
curr_confidence = 0


for line in sys.stdin:
    rule, confidence = line.split('\t')
    confidence = float(confidence.replace('\n', ''))
    if rule == curr_rule:
        curr_confidence += confidence
    else:
        if curr_rule:
            if curr_confidence >= 0.375 and curr_confidence <= 0.675:
                print('{0}\t{1}'.format(curr_rule, curr_confidence))
        curr_rule = rule
        curr_confidence = confidence
if curr_rule == rule:
    if curr_confidence >= 0.375 and curr_confidence <= 0.675:
        print('{0}\t{1}'.format(curr_rule, curr_confidence))
