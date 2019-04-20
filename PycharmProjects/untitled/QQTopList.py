# -*- coding:utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import sys


# 用PhantomJS接口创建一个selemium的webDriver
# driver = webdriver.PhantomJS(executable_path="D:\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', chrome_options=chrome_options)

# 准备好存储歌单的csv文件
csv_file = open("QQplaylist.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(csv_file)
# writer.writerow(['标题', '播放数', '链接'])


def main():
    # 解析每一页直到下一页为空
    count = 1
    max_num = 0
    url = 'https://y.qq.com/portal/playlist.html#t3='
    while url != 'javascript:void(0)':
        try:
            url = 'https://y.qq.com/portal/playlist.html#t3='
            url = url + str(count) + '&'
            # print(url)
            driver.get(url)
            # driver.switch_to.frame("contentFrame")
            time.sleep(1)
            data = driver.find_element_by_id("playlist_box").find_elements_by_tag_name("li")
            if max_num == 0:
                index_data = driver.find_elements_by_class_name("js_pageindex")
                max_num = int(index_data[3].get_attribute("data-index"))
            for i in range(len(data)):
                nb = data[i].find_element_by_class_name("playlist__other").text.replace('播放量：', '').replace(' ', '')
                # print(nb)
                if '万' in nb and float(nb.split("万")[0]) > 500:
                    msk = data[i].find_element_by_css_selector("a.js_playlist")
                    writer.writerow([msk.get_attribute("title"), nb, msk.get_attribute("href")])

            if max_num != 0 and count < max_num and count <= 100:
                count += 1

            else:
                url = 'javascript:void(0)'
        except Exception:
            sys.exit(1)

    csv_file.close()
    

if __name__ == '__main__':
    main()
