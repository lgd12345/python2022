from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# #exchangeList > li.on > a.head.usd > div

# F12 . copy . copy selector
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)

print("value : ", soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value'))

#exchangeList > li.on > a.head.usd > div
txt1 = soup.select_one('div.head_info')
print()
print("txt1 ::::: ", txt1)
print(txt1.select('span')[0].string)
print(txt1.select('span')[1].string)
print(txt1.select('span')[2].string)
print(txt1.select('span')[3].string)

# txt2 = 리스트형태
txt2 = txt.select('span')
print(txt2)
# 리스트 풀기
for i in txt2:
    print(i.string)

print()
# 가격
price = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value').string
print(price)
# 상승 하락
updown = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.blind').string
print(updown)
