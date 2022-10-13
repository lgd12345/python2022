from bs4 import BeautifulSoup
import requests

# res = requests.get("https://finance.naver.com/item/main.naver?code=252670")
# soup = BeautifulSoup(res.content, 'html.parser')

# ko = soup.select_one(
#     '#middle > div.h_company > div.wrap_company > h2 > a').string
# print(ko)


# ko2 = soup.select_one(
#     '#chart_area > div.rate_info > div .blind').string
# print(ko2)
#################################################################################
codes = ['252670', '251340']
datas = []
for code in codes:
    url = 'https://finance.naver.com/item/main.naver?code='+code
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    # string 대신 get_text()써도 된다.
    title = soup.select_one(
        '#middle > div.h_company > div.wrap_company > h2 > a').get_text()

    price = soup.select_one(
        '#chart_area > div.rate_info > div .blind').string

    datas.append([title, price])
print(datas)
