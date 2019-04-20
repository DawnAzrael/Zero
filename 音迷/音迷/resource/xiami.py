# -*- coding:utf-8 -*-
from selenium import webdriver
import pymysql
import sys


db = pymysql.connect("192.168.199.201", "zero", "Azrael.134", "RecommendRes")
cursor = db.cursor()


def get_user_list(user_id):
    # 244467287
    getUrl = "https://www.xiami.com/favorite/" + str(user_id)
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option,
                               executable_path=r'C:\Users\13414\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    browser.get(getUrl)
    input_xpath1 = browser.find_elements_by_xpath('//div[@class="song-name em"]/a')
    input_xpath2 = browser.find_elements_by_xpath('//div[@class="singers"]')
    table_name = 'xiami' + user_id
    try:
        sql_for_create = r'CREATE TABLE ' + table_name + ' (User_id varchar(255), song_name varchar(255), singer varchar(255), link varchar(255), sign_link varchar(255));'
        cursor.execute(sql_for_create)
        db.commit()
        for (ev1, ev2) in zip(input_xpath1, input_xpath2):
            # print(user_id, ev1.text, ev2.text, ev1.get_attribute('href'), ev1.get_attribute('href')[27:])
            sql = r"INSERT INTO " + table_name + " (User_id, song_name, singer, link, sign_link) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}');"\
                .format(table_name, user_id, ev1.text, ev2.text, ev1.get_attribute('href'), ev1.get_attribute('href')[27:])
            cursor.execute(sql)
            db.commit()
    except:
        db.rollback()
        cursor.execute(r'DROP TABLE ' + table_name + ';')
        db.commit()
        sql_for_create = r'CREATE TABLE ' + table_name + ' (User_id varchar(255), song_name varchar(255), singer varchar(255), link varchar(255), sign_link varchar(255));'
        cursor.execute(sql_for_create)
        db.commit()
        for (ev1, ev2) in zip(input_xpath1, input_xpath2):
            print(user_id, ev1.text, ev2.text, ev1.get_attribute('href'), ev1.get_attribute('href')[27:])
            sql = r"INSERT INTO " + table_name + " (User_id, song_name, singer, link, sign_link) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}');" \
                .format(table_name, user_id, ev1.text, ev2.text, ev1.get_attribute('href'),
                        ev1.get_attribute('href')[27:])
            cursor.execute(sql)
            db.commit()
        # 修改 动态创建 表名是User_id
        # sys.exit(301)
    db.close()
    browser.close()


if __name__ == '__main__':
    user_id = sys.argv[1]
    # user_id = '244467287'
    get_user_list(user_id)
