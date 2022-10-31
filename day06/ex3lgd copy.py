from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    By.XPATH, '//*[@id="root"]/main/div/div[1]/div[2]/div/div[3]/div/div/div/div/div[1]/div[3]/div[13]/div/div/a/div[1]').click()
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
# test = driver.find_elements(By.CLASS_NAME, 'overflow-hidden')


boxItem = driver.find_elements(
    By.XPATH, '//*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div/div[1]/div[3]/div[2]/div')
# //*[@id = "root"]/main/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[3]/div[1]/div[3]/div[2]/div
# //*[@id="root"]/main/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/div[3]/div[2]/div

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

        # 좋아요 쉼표 온점 제거
        view = re.sub(',', '', view)
        like = re.sub(',', '', like)

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

# (나도 있어 근육)과 그림체가 비슷한 웹툰
webtoonW_df = pd.DataFrame(list, columns=('제목', '작가', '조회수', '좋아요'))

# 파일 만들기
# webtoonW_df.to_csv('webtoonW.csv', mode='w', encoding='utf-8-sig', index=True)

# 딕형식으로 만들기
dict_webtoon = {'100만이상': 0, '10만이상': 0, '1만이상': 0}

# 조회수에서 숫자만 추출
for item in list:
    item2 = item[3].replace('만', '000')
    item3 = item2.replace('.', '')
    item4 = float(item3)
    print(item4)

    if item4 >= 1000000:
        dict_webtoon['100만이상'] += 1
    elif item4 >= 100000:
        dict_webtoon['10만이상'] += 1
    elif item4 >= 10000:
        dict_webtoon['1만이상'] += 1

print(dict_webtoon)

# 그래프 그리기

# 폰트 불러오기
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
# 폰트 적용
mpl.rc('font', family=font_name)

# 차트종류, 제목, 차트크기,범례,폰트 크기 설정
# 그래프 객체만들기
figure = plt.figure()
# 그래프 위치 1행 1열 1번째
axes = figure.add_subplot(111)
# 파이차트 # autopct : 숫자 어느정도까지 보여줄지
axes.pie(dict_webtoon.values(), labels=dict_webtoon.keys(), autopct='%.1f%%')
plt.show()
