# -*- coding:utf-8 -*-
from selenium import webdriver
import csv
import os


def init_file():
    try:
        os.remove('./data.csv')
        # csv_file = open("./data.csv", "w", newline='', encoding='utf-8')
    except:
        pass


def get_user_list(user_id):
    # 244467287
    getUrl = "https://www.xiami.com/favorite/" + str(user_id)
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option,
                               executable_path=r'/usr/bin/chromedriver')
    browser.get(getUrl)
    input_xpath1 = browser.find_elements_by_xpath('//div[@class="song-name em"]/a')
    input_xpath2 = browser.find_elements_by_xpath('//div[@class="singers"]')
    # csv_file = open("./data.csv", "a+", newline='', encoding='utf-8')
    with open("./data.csv", "a+", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for (ev1, ev2) in zip(input_xpath1, input_xpath2):
            # print(user_id, ev1.text, ev2.text, ev1.get_attribute('href'), ev1.get_attribute('href')[27:])
            writer.writerow([user_id, ev1.text, ev2.text, ev1.get_attribute('href'), ev1.get_attribute('href')[27:]])
    browser.close()


if __name__ == '__main__':
    # open id file for user_id in file
    # then get_user_list(user_id)
    # id list add manually, get_list auto
    # user_id = sys.argv[1]
    # # user_id = '244467287'
    # get_user_list(user_id)
    init_file()
    try:
        fp = open('./idpool.txt', 'r')
        res = fp.readlines()
        # print(res)
        for i in res:
            # print(i.replace('\n', ''))
            get_user_list(i.replace('\n', ''))
    except:
        pass
    fp.close()
