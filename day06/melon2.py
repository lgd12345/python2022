from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import re

# 순위 곡명 가수 앨범
#frm > div > table > tbody
# 순위
# lst50 > td:nth-child(2) > div > span.rank
# <span class="rank ">1</span>
# 곡명
# <a href="javascript:melon.play.playSong('19041301',35595136);" title="새삥 (Prod. ZICO) (Feat. 호미들) 재생">새삥 (Prod. ZICO) (Feat. 호미들)</a>
# 가수
# <a href="javascript:melon.link.goArtistDetail('602056');" title="지코 (ZICO) - 페이지 이동">지코 (ZICO)</a>
# 앨범
# <a href="javascript:melon.link.goAlbumDetail('11045985');" title="스트릿 맨 파이터(SMF) Original Vol.3 (계급미션) - 페이지 이동">스트릿 맨 파이터(SMF) Original Vol.3 (계급미션)</a>

# https://www.melon.com/chart/week/index.htm

path = "C:\\chromedriver_win32\\chromedriver.exe"
# driver = wd.Chrome(path)
options = wd.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = wd.Chrome(path, options=options)
# 2초 기다린다.(Time쓰듯이)
driver.implicitly_wait(2)
# 홈페이지 불러오는 것
driver.get('https://www.melon.com/chart/week/index.htm')
# //*[@id="frm"]/div/table/tbody

# 여기서 from selenium.webdriver.common.by import By이거 임폴트 시켰다
tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
# print(tbody)
trs = tbody.find_elements(By.TAG_NAME, 'tr')

# 순위 #lst50 > td:nth-child(2) > div > span.rank
datas = []
for i in trs:

    rank = i.find_element(
        By.CLASS_NAME, 'rank').text

    song = i.find_element(
        By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME, 'a').text

    name = i.find_element(
        By.CSS_SELECTOR, 'div.rank02').find_element(By.TAG_NAME, 'a').text

    album = i.find_element(
        By.CLASS_NAME, 'rank03').find_element(By.TAG_NAME, 'a').text
    likes = i.find_element(
        By.CLASS_NAME, 'like').find_element(By.CLASS_NAME, 'cnt').text

    # 좋아요 쉼표 제거
    likes = re.sub(',', '', likes)

    print('순위 : ', rank)
    print('제목 : ', song)
    print('가수 : ', name)
    print('앨범 : ', album)
    print('좋아요 : ', likes)
    print()

    datas.append([rank, song, name, album, likes])

print(datas)

melon_df = pd.DataFrame(datas, columns=('순위', '곡명', '가수명', '앨범', '좋아요'))

# 파일 만들기
# melon_df.to_csv('melon1.csv', mode='w', encoding='utf-8-sig', index=False)
