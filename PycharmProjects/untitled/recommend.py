#!/usr/bin/python
# -*- coding:utf-8 -*-


import pymysql
import pyhdfs
import sys
import csv


def getusersongmids(id):
    # link db, then return songmids
    # if can not find database table or table is empty, return -1 , from xiami recommend table <- daily selenium
    db = pymysql.connect("localhost", "zero", "Azrael.134", "RecommendRes")
    cursor = db.cursor()
    sql_search = 'SELECT sign_link FROM xiami' + str(id) + ';'
    try:
        cursor.execute(sql_search)
        results = cursor.fetchall()
        lst = []
        for row in results:
            lst.append(row[0])
    except:
        print('fail')
    db.close()
    return lst


def recommendbysongmids(xmid, songmids):
    try:
        recommend_sets = []
        # then find -> double for
        for songmid in songmids:
            # read localhost:9000/common_step3/part*
            fs = pyhdfs.HdfsClient("localhost", 9000)
            f = fs.open('/common_step3/part-00000')
            for i in f:
                line = str(i, encoding='utf-8')
                # print(j)
                rules, confidence = line.split('\t')
                left_rules, right_rules = rules.split('->')
                # print('{0}---->{1}---->{2}'.format(left_rules, right_rules, float(confidence.replace('\n', ''))))
                if songmid in left_rules:
                    mids = right_rules.split(',')
                    for mid in mids:
                        recommend_sets.append(mid)
        recommend_sets = [i for i in recommend_sets if i != '']
        recommend_sets = {}.fromkeys(recommend_sets).keys()

        # limit counts -> 30
        if len(recommend_sets) > 30:
            recommend_sets = recommend_sets[:30]

        # print(recommend_sets)
        db = pymysql.connect("localhost", "zero", "Azrael.134", "RecommendRes")
        cursor = db.cursor()
        sql_delete = 'TRUNCATE TABLE RecommendRes.`' + str(xmid) + '_rec`;'
        sql_create = 'CREATE TABLE RecommendRes.`' + str(xmid) + '_rec` (songname varchar(255) NULL, singer varchar(255) NULL,link varchar(255) NULL);'
        try:
            cursor.execute(sql_create)
            db.commit()
        except:
            db.rollback()
            cursor.execute(sql_delete)
            db.commit()
        for sign_mid in recommend_sets:
            if sign_mid in songmids:
                continue
            else:
                link = 'https://www.xiami.com/song/' + sign_mid
                with open('/home/hadoop/PycharmProjects/untitled/data.csv', 'r', encoding="utf-8") as music_db:
                    read = csv.reader(music_db)
                    for allinfo in music_db:
                        if sign_mid == allinfo.split(',')[4].replace('\n', ''):
                            # print('{0}\t{1}\t{2}'.format(allinfo.split(',')[1], allinfo.split(',')[2], link))
                            sql_insert = "INSERT INTO RecommendRes.`" + str(xmid) + "_rec` VALUES('" + allinfo.split(',')[1] + "', '" + allinfo.split(',')[2] + "', '" + link + "');"
                            try:
                                cursor.execute(sql_insert)
                                db.commit()
                            except:
                                db.rollback()
                            break
        db.close()
        print(107,)
            # print(link)
    except:
        sys.exit(407)
    # list distinct upupup

    # selenium for info by songmids
    # into db


if __name__ == '__main__':
    # xmid = sys.argv[1];
    recommendbysongmids(sys.argv[1], getusersongmids(sys.argv[1]))

    # recommendbysongmids(244467287, getusersongmids(244467287))

    # xmid = 244467287
    # k = ['JAR9qX25705', 'xNkoVKa65d9,']
    # recommendbysongmids(xmid, k)
