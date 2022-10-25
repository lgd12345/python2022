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


# pageNum = driver.find_elements(
#     By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img')


list = []
# for i in range(1, len(pageNum)+1):

# 클래스가 다름
# grade = item.find_element(
# By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div/div/p[2]').text
# print('좋아요 : ', grade)
# 페이지 넘기는 거... 해야하는데 모르겠다.

boxItem = driver.find_elements(
    By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div[2]/div')
# //*[@id = "root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[7]/div[1]/div[4]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[8]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[9]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[11]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[8]/div[1]/div[3]/div[2]/div

# for i in range(1, 20):
#     for item in boxItem:
#         print(i)
#         try:
#             title = item.find_element(
#                 By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div/p[1]').text

#             writer = item.find_element(
#                 By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/p[2]').text
#             view = item.find_element(
#                 By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/div/p[2]').text
#             like = item.find_element(
#                 By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/div/p[3]').text

#             print('제목 : ', title)
#             print('작가 : ', writer)
#             print('조회수 : ', view)
#             print('좋아요 : ', like)

#             list.append([title, writer, view, like])
#             btnItem = driver.find_element(
#                 By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img').click()
#             time.sleep(1)
#         except:
#             continue

# print(list)


for i, item in enumerate(boxItem):
    try:
        title = item.find_element(
            By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div['+str(i+1)+']/div[1]/div[3]/div[2]/div/p[1]').text
        writer = item.find_element(
            By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div['+str(i+1)+']/div[1]/div[3]/div[2]/div/p[2]').text
        view = item.find_element(
            By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div['+str(i+1)+']/div[1]/div[3]/div[2]/div/div/p[2]').text
        like = item.find_element(
            By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div['+str(i+1)+']/div[1]/div[3]/div[2]/div/div/p[3]').text

        print('제목 : ', title)
        print('작가 : ', writer)
        print('조회수 : ', view)
        print('좋아요 : ', like)

        list.append([title, writer, view, like])
        btnItem = driver.find_element(
            By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div[3]/button[2]/img').click()
        time.sleep(1)
    except:
        continue

print(list)

# 월요 웹툰
# webtoonM_df = pd.DataFrame(list, columns=('제목', '작가','조회수','좋아요'))

# 파일 만들기
# webtoonM_df.to_csv('webtoonM.csv', mode='w', encoding='utf-8-sig', index=True)
