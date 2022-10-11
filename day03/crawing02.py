from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 접속해야함
# 그냥 (http) 객체
res0 = req.urlopen(url)
print(res0)

# 태그로 된 문장을 읽어온다.
res = req.urlopen(url)
print(res)
soup = BeautifulSoup(res, 'html.parser')
print(soup)

# 기상청 육상 중기 예보에서 title만 출력하기
title = soup.channel.title
print(title)
print(title.string)
title1 = soup.find('title').string
print(title1)

# wf태그 내용 출력하기
wf = soup.find('wf').string
print(wf)
