#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
import sys
import os

if os.path.exists('/home/hadoop/PycharmProjects/untitled/MR_Process/subUnionsData.txt'):
    os.remove('/home/hadoop/PycharmProjects/untitled/MR_Process/subUnionsData.txt')


class sub_set:
    def subsets(songmids):
        N = len(songmids)
        prePart = []
        prePart.append(songmids[:1])
        tailPart = songmids[1:]
        for i in range(0, N - 1):
            for j in tailPart:
                lst = []
                for k in prePart[0]:
                    lst.append(k)
                lst.append(j)
                # print(lst)
                with open(r'/home/hadoop/PycharmProjects/untitled/MR_Process/subUnionsData.txt', 'a') as file1:
                    # file1.write(str(lst))
                    for l in lst:
                        file1.write(l)
                        file1.write(',')
                    file1.write('\n')
            prePart[0].append(tailPart[:1][0])
            tailPart = tailPart[1:]

    def subsetuse(songmids):
        for ev in songmids:
            # print(ev.split(" "))
            with open(r'/home/hadoop/PycharmProjects/untitled/MR_Process/subUnionsData.txt', 'a') as file1:
                file1.write(str(ev))
                file1.write(',')
                file1.write('\n')
        for times in range(0, len(songmids)):
            sub_set.subsets(songmids[times:])


try:
    path = '/home/hadoop/PycharmProjects/untitled/data.csv'
    with open(path, "r", encoding="utf-8") as mic_ele:
        read = csv.reader(mic_ele)
        or_list = [[]]
        i = 0
        cur_id = ''
        for u_list in mic_ele:
            if not cur_id:
                cur_id = u_list.split(',')[0]
                or_list[i].append(u_list.split(',')[4].replace('\n', ''))
            else:
                if cur_id != u_list.split(',')[0]:
                    cur_id = u_list.split(',')[0]
                    i += 1
                    or_list.append([])
                    or_list[i].append(u_list.split(',')[4].replace('\n', ''))
                else:
                    or_list[i].append(u_list.split(',')[4].replace('\n', ''))
        #  print(or_list)
except:
    sys.exit(303)

for ii in or_list:
    sub_set.subsetuse(ii)
