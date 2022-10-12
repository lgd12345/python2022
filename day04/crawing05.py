from bs4 import BeautifulSoup
import urllib.request as req

# https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# #mw-content-text > div.mw-parser-output > ul:nth-child(6) > li
# mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(1) > a

# F12 . copy . copy selector

# ex) s1 s2 후손 (li a)
# ex) s1>s2 직계자식 (b > a)
txt = soup.select_one(
    '#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a')
print(txt)

a_list = soup.select('#mw-content-text > div > ul > li a')
print(a_list)

for a in a_list:
    name = a.string
    print('-', name)
