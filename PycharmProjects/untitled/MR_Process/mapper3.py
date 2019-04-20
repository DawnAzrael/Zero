#!/usr/bin/python


import sys


for line in sys.stdin:
    allvalue = 0
    flag = 0
    k, v = line.split('\t')
    songmid = v.split('&')
    for i in songmid:
        # filter non-null
        if 'null,#' in i:
            a, b = i.split('#')
            # print('{0}\t{1}'.format(a, b))
            allvalue = int(b)
            flag = 1
    if flag == 1:
        for j in songmid:
            if 'null,#' not in j:
                a, b = j.split('#')
                cofidence = int(b) / allvalue
                print('{0}\t{1}'.format(k + '->' + a, cofidence))
        flag = 0
    # print('\n\n')
