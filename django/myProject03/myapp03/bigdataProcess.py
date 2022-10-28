from cProfile import label
from bs4 import BeautifulSoup
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import requests
import pandas as pd
import re
#
from myProject03.settings import STATIC_DIR
import os
# 크롤링하거나 빅데이터 처리할 부분
# 멜론 크롤링


def melon_crawling(datas):

    header = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(
        'https://www.melon.com/chart/week/index.htm', headers=header)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.select_one("#frm > div > table > tbody")

    trs = tbody.select("#lst50")

    for tr in trs[:10]:
        rank = tr.select_one("span.rank").get_text()
        name = re.sub('\n', '', tr.select_one(
            "div.ellipsis.rank01").get_text())
        signer = re.sub('\n', '', tr.select_one(
            "div.ellipsis.rank02 > a").get_text())
        album = re.sub('\n', '', tr.select_one(
            "div.ellipsis.rank03 > a").get_text())
        # print(rank)
        # print(name)
        # print(signer)
        # print(album)

        tmp = dict()
        tmp['rank'] = rank
        tmp['name'] = name
        tmp['signer'] = signer
        tmp['album'] = album

        datas.append(tmp)


# 날씨 크롤링 (모델 만들어서 db에 넣고 출력될 것임)


def weater_crawing(last_date, weather):
    print('weather_crawing')
    req = requests.get(
        'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108')

    soup = BeautifulSoup(req.text, 'html.parser')

    # city(키)를 찾고 벨류를 뽑겠다
    for i in soup.find_all('location'):
        weather[i.find('city').text] = []
        for j in i.find_all('data'):
            temp = []
            if(len(last_date) == 0) or (j.find('tmef').text > last_date[0]['tmef']):
                temp.append(j.find('tmef').text)
                temp.append(j.find('wf').text)
                temp.append(j.find('tmn').text)
                temp.append(j.find('tmx').text)
                # print('temp: ', temp)
                weather[i.find('city').string].append(temp)
    print('부산 날씨 : ', weather['부산'])

# 그래프 그리기


def weater_make_chart(result, wfs, dcounts):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family=font_name)

    high = []
    low = []
    xdata = []

    for row in result.values_list():
        high.append(row[5])
        low.append(row[4])
        xdata.append(row[2].split('-')[2])

    plt.cla()
    plt.figure(figsize=(10, 6))
    plt.plot(xdata, low, label="최저기온")
    plt.plot(xdata, high, label="최고기온")
    plt.legend()
    plt.savefig(os.path.join(STATIC_DIR, 'images\\weather_busan.png'), dpi=300)
# 이미지 저장완료
    plt.cla()
    plt.bar(wfs, dcounts)
    plt.savefig(os.path.join(STATIC_DIR, 'images\\weather_bar.png'), dpi=300)

    plt.cla()
    plt.pie(dcounts, labels=wfs, autopct='%.1f%%')
    plt.savefig(os.path.join(STATIC_DIR, 'images\\weather_pie.png'), dpi=300)

    image_dic = {
        'plot': 'weather_busan.png',
        'bar': 'weather_bar.png',
        'pie': 'weather_pie.png'

    }
    return image_dic
