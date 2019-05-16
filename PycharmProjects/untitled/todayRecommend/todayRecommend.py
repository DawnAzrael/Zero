# -*- coding:utf-8 -*-
import pymysql
import json


def intoTodayRecommend():
    # table_name = 'xiami'
    try:
        db = pymysql.connect("localhost", "zero", "Azrael.134", "RecommendRes")
        cursor = db.cursor()
        empty_sql = 'TRUNCATE TABLE todayrecommend;'
        cursor.execute(empty_sql)
        db.commit()
        f = open("testdata.txt", 'r', encoding="utf8")
        testdata = f.read()
        todaydata = json.loads(testdata)
        # print(todaydata)
        for info in todaydata["result"]["data"]["songs"]:
            song_link = 'https://www.xiami.com/song/' + info["songStringId"]
            sql = 'INSERT INTO todayrecommend (songname, singer, link) VALUES ("{0}","{1}", "{2}");'.format(info["songName"], info["singers"], song_link)
            # print(sql)
            cursor.execute(sql)
            db.commit()  
    except:  
        db.rollback()
    db.close()


if __name__ == '__main__':
    intoTodayRecommend()
