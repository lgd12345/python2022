from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re
from bs4 import BeautifulSoup
import urllib.request
import datetime
import time


def CoffeeBean_store(result):
    path = "C:\\chromedriver_win32\\chromedriver.exe"
    options = wd.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = wd.Chrome(path, options=options)

    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"

    for i in range(1, 10):  # 매장 수 만큼 반복
        driver.get(CoffeeBean_URL)
        time.sleep(1)  # 웹페이지 연결할 동안 1초 대기
        try:
            driver.execute_script("storePop2(%d)" % i)
            time.sleep(1)
            html = driver.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            # 매장이름 출력
            print(store_name)
        except:
            continue


result = []
CoffeeBean_store(result)
