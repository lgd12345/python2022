from bs4 import BeautifulSoup
import requests

#mainContent > div > div.box_ranking > ol
# li:nth-child(1) 여기서 영화 선택됨

# mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont

# 영화 제목
# mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a

# 영화 평점
# mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span

res1 = requests.get('https://movie.daum.net/ranking/reservation')
soup1 = BeautifulSoup(res1.content, 'html.parser')

a = soup1.select(
    '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > strong > a')
b = soup1.select(
    '#mainContent > div > div.box_ranking > ol > li > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span')

print(a)
print(b)
for i in range(len(a)):
    print('영화 제목 : ', a[i].string)
    print('평점', b[i].string)
    print()
######################################################################
res = requests.get('https://movie.daum.net/ranking/reservation')
html = res.text
soup = BeautifulSoup(html, 'html.parser')

ols = soup.find('ol', class_="list_movieranking")
rankcont = ols.find_all('div', class_='thumb_cont')

for i in rankcont:
    title = i.find('a', class_='link_txt').get_text()
    grade = i.find('span', class_='txt_grade').get_text()
    reser = i.find('span', class_='txt_num').get_text()

    print('영화 제목 : ', title)
    print('평점 : ', grade)
    print('예매율 :', reser)
