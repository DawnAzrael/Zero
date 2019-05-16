#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pyhdfs


def hdfs_test():
    fs = pyhdfs.HdfsClient("localhost", 9000)
    f = fs.open('/common_step3/part-00000')
    for i in f:
        line = str(i, encoding='utf-8')
        # print(j)
        rules, confidence = line.split('\t')
        left_rules, right_rules = rules.split('->')
        print('{0}---->{1}---->{2}'.format(left_rules, right_rules, float(confidence.replace('\n', ''))))


def test():
    a = '244467287,在青春里遇见,卜冠今,https://www.xiami.com/song/xN7e8gdaa4d,xN7e8gdaa4d\n'
    a = a.split(',')
    print(a)


if __name__ == '__main__':
    test()
