#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys


class sub_set:
    def subsets(songmids):
        # ABC
        N = len(songmids)
        # print(N)
        prePart = []
        prePart.append(songmids[:1])
        # prePart = A
        tailPart = songmids[1:]
        # tailPart = BC
        # print(prePart)
        # print(tailPart)
        for i in range(0, N - 1):
            # i = 0 1 2
            # print(i)
            for j in tailPart:
                lst = []
                for k in prePart[0]:
                    lst.append(k)
                lst.append(j)
                # print(lst)
                # print(lst)
                co = '#' + freq
                sup_items = ''
                for kkkk in songmids:
                    sup_items = sup_items + kkkk + ','
                sup_key = ''
                for kk in lst:
                    sup_key = sup_key + kk + ','
                # print(sup_key)
                # print(sup_items)
                if sup_key != songmid:
                    print('{0}\t{1}'.format(sup_key, songmid + co.replace('\n', '')))
                    # if sup_key != sup_items:
                    #     print('{0}\t{1}'.format(sup_key, sup_items + co.replace('\n', '')))
                    # elif sup_key == sup_items:
                    #     print('{0}\t{1}'.format(sup_key, songmid + co.replace('\n', '')))
            prePart[0].append(tailPart[:1][0])
            # print(prePart[0])
            # print(tailPart)
            # prePart = AB tailPart = C
            # prePart = ABC tailPArt = []
            tailPart = tailPart[1:]

    def subsetuse(songmids):
        for ev in songmids:
            # print(ev.split(" "))
            co = '#' + freq
            sup_items = ''
            for kkk in songmids:
                sup_items = sup_items + kkk + ','
            print('{0}\t{1}'.format(ev + ',', sup_items + co.replace('\n', '')))
            # print(co)
        for times in range(0, len(songmids)):
            # ABC
            # BC
            # print('\n****')
            # print(songmids[times:])
            # print('\n****')
            sub_set.subsets(songmids[times:])


for line in sys.stdin:
    songmid, freq = line.split('\t')
    value_freq = 'null,#' + freq
    print('{0}\t{1}'.format(songmid, value_freq.replace('\n', '')))
    # print('{0}\t{1}'.format(songmid, freq.replace('\n', '')))
    lst = []
    for k in songmid.split(','):
        lst.append(k)
    # print(lst[:-1])
    # print('\n\n\n')
    # print(lst[:-1])
    # print('\n\n\n')
    # AB ABC
    sub_set.subsetuse(lst[:-1])
