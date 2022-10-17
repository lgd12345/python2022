from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

# https://tour.interpark.com/?mbn=tour&mln=tour

# 가격 평점 호텔

path = "C:\\chromedriver_win32\\chromedriver.exe"
# driver = wd.Chrome(path)
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = wd.Chrome(path, options=options)
# 2초 기다린다.(Time쓰듯이)
driver.implicitly_wait(2)
# 홈페이지 불러오는 것
driver.get('https://tour.interpark.com/?mbn=tour&mln=tour')
driver.find_element(By.ID, 'SearchGNBText').send_keys('제주도')
driver.find_element(By.CLASS_NAME, 'search-btn').click()
time.sleep(2)
# 국내 숙박 더보기
driver.find_element(By.CLASS_NAME, 'moreBtn').click()
time.sleep(2)


boxItem = driver.find_elements(By.CLASS_NAME, 'boxItem')
datas = []
for i in boxItem:
    try:

        title = i.find_element(
            By.CLASS_NAME, 'infoTitle').text

        price = i.find_element(
            By.CLASS_NAME, 'final').find_element(By.TAG_NAME, 'strong').text

        grade = i.find_element(
            By.XPATH, '//*[@id="boxList"]/li[1]/div/div[2]/div[3]/div[2]/p[1]').text

        print('이름 : ', title)
        print('가격 : ', price)
        print(grade)
        print()

        datas.append([title, price, grade])
    except:
        continue

print(datas)
