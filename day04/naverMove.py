from shutil import move
from matplotlib.pyplot import cla
import requests
from bs4 import BeautifulSoup

# crawing07.py 파일의 내용 requests.get로 하기
req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html = req.text

soup = BeautifulSoup(html, 'html.parser')
movie_ranking_list = soup.find_all('div', class_="tit3")
print(type(movie_ranking_list))
print("--------------------------")
# 제목만
for i in movie_ranking_list:
    print(i.get_text().strip())

print('+++++++++++++++++++++++++++')

for i in range(len(movie_ranking_list)):
    print((i+1), '위 :', movie_ranking_list[i].get_text().strip())
print()

# select방식
movie_ranking_list2 = soup.select('div.tit3')
print(type(movie_ranking_list2))
for i in movie_ranking_list2:
    print(i.get_text().strip())
