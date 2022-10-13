from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import re

# 실행할 때 cmd 를 이용 한다.
# C:\Users\admin>cd C:\Python\day05
# C:\Python\day05>python selenium04Beauti.py

# 셀레늄형식을 뷰티솝으로 바꿔서 실행한다.


path = "C:\\chromedriver_win32\\chromedriver.exe"
# driver = wd.Chrome(path)
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = wd.Chrome(path, options=options)

# 홈페이지 불러오는 것
driver.get('https://www.youtube.com/c/paikscuisine/videos')

# 불러온 값을 읽기
page = driver.page_source

# 뷰티풀솝
soup = BeautifulSoup(page, 'html.parser')

all_videos = soup.find_all(id='dismissible')
# print(all_videos)
print()

# 2초 기다린다.
time.sleep(2)

datas = []
for video in all_videos:

    title = video.find(id='video-title').text

    video_time = video.find(
        'span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer').text.strip()

    video_num = video.find(
        'span', {'class': 'style-scope ytd-grid-video-renderer'}).text

    print(title)
    print(video_time)
    print(video_num)
    print()

    datas.append([title, video_time, video_num])

# print(datas)


# DataFrame 형태로 변환하여 제목, 재생시간, 조회수
# youtubu.csv

yutubu_df = pd.DataFrame(datas, columns=('제목', '재생시간', '조회수'))
# yutubu_df.to_csv('youtube.csv', mode='w', encoding='utf-8-sig', index=True)

#
dict_youtubu = {'100만이상': 0, '50만이상': 0, '10만이상': 0}

print()

datas1 = []
for video2 in all_videos:
    numcut = re.compile('\d*\.?\d+')
    video_num2 = video2.find(
        'span', {'class': 'style-scope ytd-grid-video-renderer'}).text
    datas1.append([video_num2])
print(datas1)

# training_data = [['연두', 3, '사과'],
#                  ['노랑', 3, '사과'],
#                  ['빨강', 2, '포도'],
#                  ['빨강', 1, '포도'],
#                  ['노랑', 3, '레몬']]


# def fruit_color(data):
#     color_dic = {}
#     for row in data:
#         label = row[0]
#         if label not in color_dic:
#             color_dic[label] = 0
#         color_dic[label] += 1
#     return color_dic

# colorCnt = fruit_color(training_data)
# print(colorCnt)
# # {'연두' : 1, '노랑' : 2, '빨강' : 2}
