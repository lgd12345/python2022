from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 실행할 때 cmd 를 이용 한다.
# C:\Users\admin>cd C:\Python\day05
# C:\Python\day05>python selenium01.py

path = "C:\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
options.add_experimental_option("detach", True)
driver = wd.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

driver.get('https://google.com')
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
# driver.find_element_By.id('search_btn').click() #버전3에서 사용할 때

# 창 닫힘 방지(강제)
# while(True):
#     pass
