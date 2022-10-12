import requests
from bs4 import BeautifulSoup
import re
import urllib.request as req


print()
# requests.get로 하기
req = requests.get(
    "https://movie.naver.com/movie/bi/mi/basic.naver?code=219812")
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# select방식
movie = soup.select_one(
    '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').string
# ex) 극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교 제목 출력됨
print("영화 제목 : ", movie)

movie2 = soup.select('#_MainPhotoArea > div.viewer > div img')
txt = soup.find_all(src=re.compile(r'^https://ssl.*TRAILER.*2022.*g'))
print('+'*50)
for e in txt:
    #  ex) https://ssl.pstatic.net/imgmovie/multimedia/MOVIECLIP/TRAILER/53210_20220921101745.jpg 속성값만 출력됨!
    print(e.attrs['src'])

print('+'*50)
