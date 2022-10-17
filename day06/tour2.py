
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

# https://tour.interpark.com/?mbn=tour&mln=tour

# 가격 평점 호텔
# 오류
path = "C:\\chromedriver_win32\\chromedriver.exe"
driver = wd.Chrome(path)

# 홈페이지 불러오는 것
driver.get('https://tour.interpark.com/?mbn=tour&mln=tour')

time.sleep(1)

driver.find_element(By.ID, 'SearchGNBText').send_keys('제주도')
driver.execute_script('searchBarModule.ClickForSearch()')

time.sleep(1)
# app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.searchAllBox.domesticHotel.col1 > div > button
# 국내 숙박 더보기
morebtn = driver.find_element(
    By.CSS_SELECTOR, 'div.searchAllBox.domesticHotel.col1 > div > button')
morebtn.click()
time.sleep(2)


pageNum = driver.find_elements(By.CSS_SELECTOR, 'div.pageNumBox > ul > li')
# boxList > li:nth-child(1)
# app > div > div:nth-child(1) > div.resultAtc > div.contentsZone > div.panelZone > div.pageNumBox > ul > li:nth-child(1)
list = []
for i in range(1, len(pageNum)+1):
    boxItem = driver.find_elements(By.CSS_SELECTOR, '#boxList > li')
    for item in boxItem:
        try:
            title = item.find_element(By.TAG_NAME, 'h5').text

            price = item.find_element(By.TAG_NAME, 'strong').text

            grade = item.find_element(
                By.CSS_SELECTOR, 'div.productInfo > div:nth-child(3) > div:nth-child(2) > p.info').text.split('평점')[1]

            print('순위 : ', title)
            print('제목 : ', price)
            print('좋아요 : ', grade)
            print()

            list.append([title, price, grade])

        except:
            continue
    if i == len(pageNum):
        break
    pageNum[i].click()
    time.sleep(1)
print(list)

# hotel.csv 호텔명, 가격, 평점
hotel_df = pd.DataFrame(list, columns=('호텔명', '가격', '평점'))

# 파일 만들기
hotel_df.to_csv('hotel_jeju2.csv', mode='w', encoding='utf-8-sig', index=True)
