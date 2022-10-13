from selenium import webdriver as wd
from selenium.webdriver.common.by import By

# 실행할 때 cmd 를 이용 한다.
# C:\Users\admin>cd C:\Python\day05
# C:\Python\day05>python selenium02.py

path = "C:\\chromedriver_win32\\chromedriver.exe"
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = wd.Chrome(path, options=options)

driver.get('https://naver.com')
driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
