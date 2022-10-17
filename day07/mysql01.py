import pymysql
import requests
from bs4 import BeautifulSoup

# 데이터 베이스 연결 : connect()
# 데이터 베이스 작업을 전달하기 위한 객체 생성:cursor()
# 질의문 전달:execute()
# 실행 : commit()
# select한결과를 가져옴 fetchone(),fetchall()


dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True)

insert_weather = (
    "insert into forecast(city,tmef,wf,tmn,tmax)""values(%s,%s,%s,%s,%s)")
# insert_weather =
#  "insert into forecast(city,tmef,wf,tmn,tmax)values(%s,%s,%s,%s,%s)"

# (최신날짜 구해서 최신날짜가 있으면 비교해서 더 최신날짜가 있으면 들어가게 한다.)똑같은 데이터 또 들어가는 것 방지
select_data = "select tmef from forecast order by tmef desc limit 1"
cur = conn.cursor()
cur.execute(select_data)
last_date = cur.fetchone()  # db에 있는 최신날짜
print(type(last_date))
print(last_date)

req = requests.get(
    'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')

html = req.text
soup = BeautifulSoup(html, 'lxml')

weather = {}
for i in soup.find_all('location'):
    weather[i.find('city').text] = []
    for j in i.find_all('data'):
        tmp = []
        if(last_date is None) or (str(last_date[0]) < j.find('tmef').text):
            tmp.append(j.find('tmef').text)
            tmp.append(j.find('wf').text)
            tmp.append(j.find('tmn').text)
            tmp.append(j.find('tmx').text)
            weather[i.find('city').string].append(tmp)
# print(weather)

for i in weather:
    for j in weather[i]:
        cur = conn.cursor()
        cur.execute(insert_weather, (i, j[0], j[1], j[2], j[3]))
        conn.commit()
