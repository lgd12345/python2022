from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody
# li:nth-child(1) 여기서 매장 선택됨

# mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont

# 지역
# contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(2) > td.noline.center_t
# contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(3) > td.noline.center_t
# 매장명
# contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(2) > td:nth-child(2)

# 전화번호
# contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(2) > td:nth-child(6)

# codes = ['1', '2', '3', '4', '5']
# for code in codes:
#     url1 = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo='+code
#     response = requests.get(url1)
#     html = response.text
#     soup1 = BeautifulSoup(html, 'html.parser')
#     a = soup1.select(
#         '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr > td.noline.center_t')
#     b = soup1.select(
#         '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr > td:nth-child(2)')

# for i in range(len(a)):
#     print('주소 : ', a[i].string)
#     print('매장명', b[i].string)
#     print()
######################################################################

print('+++++++++++++++++++++++++++++++++++++++++++')
print()


def hollys_store(result):
    for page in range(1, 6):
        url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' % page
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        # print(url)

        tag_tbody = soup.select_one('tbody')
        # print(tag_tbody)

        for store in tag_tbody.select('tr'):
            tds = store.select('td')
            sido = tds[0].string
            name = tds[1].string
            address = tds[3].string
            phone = tds[-1].string
            # 지역, 매장명, 주소, 전화번호
            result.append([sido, name, address, phone])

    return


result = []
hollys_store(result)
# print(result)
hollys_df = pd.DataFrame(result, columns=(
    'sido', 'name', 'address', 'phone'))
print(hollys_df)
# pandas에서 지정해준 걸로 파일을 생성한다. 숫자가 붙음
hollys_df.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
