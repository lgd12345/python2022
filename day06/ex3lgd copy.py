from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

from sqlalchemy import true

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
driver.get('https://webtoon.kakao.com/')
# 공지사항 생겼을 때 공지사항없으면 끈다...
driver.find_element(
    By.XPATH, '/html/body/div[7]/div/div/div/div[2]').click()
# 웹툰원작
driver.find_element(
    By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div[3]/div[1]/div/div[8]').click()
time.sleep(1)
# 월요일
driver.find_element(
    By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div[3]/div[2]/div[2]/ul/li[2]').click()
time.sleep(1)
# 원하는 웹툰
driver.find_element(
    By.XPATH, '//*[@id="root"]/main/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div[3]/div[20]/div/div/a/div[1]').click()
time.sleep(1)
a = driver.find_element(
    By.XPATH, '//*[@id="root"]/main/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div[3]/div[20]/div/div/a/div[1]')

# pageNum = driver.find_elements(
#     By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img')


list = []
# for i in range(1, len(pageNum)+1):

# 클래스가 다름
# grade = item.find_element(
# By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div/div/p[2]').text
# print('좋아요 : ', grade)

# 페이지 넘기는 버튼
# btnItem = driver.find_element(
#     By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img').click()

for i in range(1, 10):

    title = a.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div/p[1]').text

    writer = a.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div/p[2]').text

    print('제목 : ', title)
    print('작가 : ', writer)

    print()

    list.append([title, writer])
    btnItem = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img').click()
    time.sleep(1)


print(list)


# 월요 웹툰
# webtoonM_df = pd.DataFrame(list, columns=('제목', '작가'))

# 파일 만들기
# hotel_df.to_csv('webtoonM.csv', mode='w', encoding='utf-8-sig', index=True)
