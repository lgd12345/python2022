from bs4 import BeautifulSoup
import re
import urllib.request as req
import requests

r = requests.get("https://api.aoikujira.com/time/get.php")

# 텍스트 형식으로 추출
txt0 = r.text
print(txt0)


# 바이너리 형식으로 데이터 추출
bin = r.content
print(bin)
##########################################################
print('###################################################')
html = """
    <ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://exaple.com/fuga">fuga</li>
    <li><a href="https://exaple.com/foo">foo</li>
    <li><a href="shttps://exaple.com/foobbb">foobbb</li>
    <li><a href="http://exaple.com/aaa">aaa</li>
    </ul>
"""
# 파씽하기
soup = BeautifulSoup(html, 'html.parser')

# compile 찾고자하는 것 패턴형식으로
# https://포함되어있는 모든 걸 찾아줌
txt = soup.find_all(href=re.compile(r'https://'))
print(txt)

# https 로 시작하는 거 출력 (^)쓴다.
txt1 = soup.find_all(href=re.compile(r'^https://'))
print(txt1)
print()
for e in txt1:
    # <a href="https://exaple.com/fuga">fuga</a> <a href="https://exaple.com/foo">foo</a>
    # print(e)

    # https://exaple.com/fuga https://exaple.com/foo 속성값만 출력됨!
    print(e.attrs['href'])
print('='*30)
# 영화 랭킹
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
r0 = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

a = soup.select('#old_content > table > tbody > tr .tit3 a')
num = 0
for i in a:
    num += 1
    print(num, ":", i.string)
print()
