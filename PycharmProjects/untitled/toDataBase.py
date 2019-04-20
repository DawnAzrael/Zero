# -*- coding:utf-8 -*-
# Made by Zero


import csv
import pymysql
import sys


def main():

    # 打开数据库连接
    db = pymysql.connect("localhost", "zero", "Azrael.134", "RecommendRes")

    # clear
    cursor = db.cursor()

    # SQL 插入语句
    try:
        cursor.execute("DELETE FROM QQHotList")
        db.commit()
        path = '/home/hadoop/PycharmProjects/untitled/QQplaylist.csv'
        with open(path, "r", encoding="utf-8") as mic_list:
            read = csv.reader(mic_list)
            for m_list in mic_list:
                m_list = m_list.split(',')
                # print(m_list[0], m_list[1], m_list[2])
                # sql = "INSERT INTO QQHotList (name, play_count, link) VALUES ('" + m_list[0] + "', '" + m_list[1] + "', '" + m_list[2] + "');"
                e_sql = r"INSERT INTO QQHotList (name, play_count, link) VALUES ('{0}', '{1}', '{2}');". \
                    format(m_list[0], m_list[1], m_list[2].replace(r"\n", ''))
                e_sql = e_sql.replace(r"\\", '')
                #print(e_sql)

                # 执行sql语句
                cursor.execute(e_sql)
                # 提交到数据库执行
                db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        sys.exit(201)

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    main()
