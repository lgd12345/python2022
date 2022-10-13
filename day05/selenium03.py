from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

# 실행할 때 cmd 를 이용 한다.
# C:\Users\admin>cd C:\Python\day05
# C:\Python\day05>python selenium03.py

path = "C:\\chromedriver_win32\\chromedriver.exe"
# driver = wd.Chrome(path)
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = wd.Chrome(path, options=options)

# 구글 화면 실행
# driver.get('https://google.com')
# # 실행됬다는 것을 5000으로 표현
# r = driver.execute_script('return 100*50')
# print(r)

driver.get('https://www.youtube.com/c/paikscuisine/videos')
all_videos = driver.find_elements(By.ID, 'dismissible')
# print(all_videos)
print()

# 2초 기다린다.
time.sleep(2)

datas = []
# 제목, 재생시간, 조회수
# text
# <span id="text" class="style-scope ytd-thumbnail-overlay-time-status-renderer" aria-label="12분 50초">12:50</span>
# <span class="style-scope ytd-grid-video-renderer">조회수 27만회</span>

for video in all_videos:
    title = video.find_element(By.ID, 'video-title').text
    video_time = video.find_element(
        By.CLASS_NAME, 'style-scope ytd-thumbnail-overlay-time-status-renderer').text
    video_num = video.find_element(
        By.CSS_SELECTOR, 'span.ytd-grid-video-renderer').text

    print(title)
    print(video_time)
    print(video_num)
    datas.append([title, video_time, video_num])

print(datas)
