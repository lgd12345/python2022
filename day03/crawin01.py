from bs4 import BeautifulSoup

html = """
<html><body>
<h1>스크레이핑이란?</h1>
<p>웹 페이지를 분석하는 것</p>
<p>원하는 부분을 추출하는 것</p>
</body><html>
"""
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print()
# 원하는 정보 찾기
h1 = soup.html.body.h1
print(h1)
# 가장위에 있는 p 출력됨
p = soup.html.body.p
print(p)
# 비어진 값.있는 값
p1 = p.next_sibling.next_sibling
print(p1)
# (태그 제거된) 값만 불러오는 것
print("h1 : ", h1.string)
print("p : ", p.string)
print("p1 : ", p1.string)
