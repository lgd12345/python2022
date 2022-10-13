from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
# 'https://www.weather.go.kr/weather/observation/currentwerther.jsp'
req = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')
soup = BeautifulSoup(req.text, 'html.parser')

table = soup.find('table', {'class': 'table-col'})

datas = []
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) > 0:
        print(tds)
        print('지역 : ', tds[0].text)
        print('온도 : ', tds[5].text)
        print('습도 : ', tds[-4].text)
        datas.append([tds[0].text, tds[5].text, tds[-4].text])
# print(datas)
print()
# write라는 함수를 이용해서 파일을 생성한다.

# with open('weather.csv', 'w') as file:
#     file.write('point, temp, num \n')
#     for item in datas:
#         row = ','.join(item)
#         file.write(row+'\n')

df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
print(df)


# #weather_table > tbody
# 지역 온도 습도
# 지역 #weather_table > tbody > tr:nth-child(1) > td:nth-child(1) > a
# 온도 #weather_table > tbody > tr:nth-child(1) > td:nth-child(6)
# 습도 #weather_table > tbody > tr:nth-child(1) > td:nth-child(11)
# weather.csv
# def hollys_store(result):

#     url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
#     html = urllib.request.urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(url)fd
#     tag_tbody = soup.select_one('tbody')
#     # print(tag_tbody)

#     for store in tag_tbody.select('tr'):
#         tds = store.select('td')
#         sido = tds[0].string
#         name = tds[1].string
#         address = tds[3].string
#         phone = tds[-1].string
#         # 지역, 매장명, 주소, 전화번호
#         result.append([sido, name, address, phone])


# result = []
# hollys_store(result)
# # print(result)
# hollys_df = pd.DataFrame(result, columns=(
#     'sido', 'name', 'address', 'phone'))
# print(hollys_df)
# hollys_df.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
