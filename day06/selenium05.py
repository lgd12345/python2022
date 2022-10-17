from selenium import webdriver as wd
import time
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# 실행할 때 cmd 를 이용 한다.
# C:\Users\admin>cd C:\Python\day06
# C:\Python\day05>python selenium05.py

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

# 딕형식으로 만들기
dict_youtubu = {'100만이상': 0, '50만이상': 0, '10만이상': 0}

print()

# 조회수에서 숫자만 추출
for item in datas:
    item = float(str(item).split('조회수')[1].split('만회')[0].strip())

    print(item)

    if item >= 100:
        dict_youtubu['100만이상'] += 1
    elif item >= 50:
        dict_youtubu['50만이상'] += 1
    elif item >= 10:
        dict_youtubu['10만이상'] += 1

print(dict_youtubu)

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
axes.pie(dict_youtubu.values(), labels=dict_youtubu.keys(), autopct='%.1f%%')
plt.show()
