# -*- coding:utf-8 -*-

try:
    fp = open('./idpool.txt', 'r')
    res = fp.readlines()
    # print(res)
    for i in res:
        print(i.replace('\n', ''))
except:
    pass
fp.close()
