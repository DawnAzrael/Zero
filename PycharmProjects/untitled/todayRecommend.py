# -*- coding:utf-8 -*-
import pymysql
import json


def intoTodayRecommend():
    # table_name = 'xiami'
    db = pymysql.connect("192.168.1.5", "zero", "Azrael.134", "RecommendRes")
    cursor = db.cursor()
    try:
        f = open("testdata.txt", 'r', encoding="utf8")
        testdata = f.read()
        todaydata = json.loads(testdata)
        # print(todaydata)
        for info in todaydata["result"]["data"]["songs"]:
            song_link = 'https://www.xiami.com/song/' + info["songStringId"]
            sql = r"INSERT INTO todayrecommend (song_name, singer, link) VALUES ('{0}','{1}', '{2}');".format(info["songName"], info["singers"], song_link)
            cursor.execute(sql)
            db.commit()  
    except:  
        db.rollback()
    db.close()


if __name__ == '__main__':
    intoTodayRecommend()
