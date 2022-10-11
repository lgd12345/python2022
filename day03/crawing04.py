from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# #exchangeList > li.on > a.head.usd > div

text = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(text)
