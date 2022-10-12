import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://news.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

links = soup.select('a[href]')
# print(links)
txt = soup.find_all(href=re.compile(r'^https://v.\w+'))
print('+'*50)
for e in txt:
    #  속성값만 출력됨!
    print(e.attrs['href'])
# . : 임의의 문자 1 개, \w : 숫자와 문자, +: 1회 이상
# 제목 출력
for t in links:
    if re.search('https://v.\w+', t['href']):
        print(t.get_text().strip())
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

#
lis = soup.find_all(href=re.compile(r'^https://v.\w+'))
for e in lis:
    print(e.get_text().strip())
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# 로또번호 추출
# #container > div > div.bx_lotto_winnum
res2 = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
soup2 = BeautifulSoup(res2.content, 'html.parser')

# 여러개는 스트링이 안되기때문에 다른 식으로 스트링을 붙여야함...
links2 = soup2.select('#container > div > div.bx_lotto_winnum .ball')
print(links2)
print()
for i in links2:
    print(i.string, end='\t')
print()
print()
# 선생님이랑 같이 find_all
ballNum = soup2.find_all('span', class_="ball")
print(ballNum)
print()
for i in ballNum:
    print(i.get_text(), end='\t')
print()
