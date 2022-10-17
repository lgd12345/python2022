import requests
from bs4 import BeautifulSoup

# 순위 곡명 가수 앨범
#frm > div > table > tbody
# 순위
# lst50 > td:nth-child(2) > div > span.rank
# <span class="rank ">1</span>
# 곡명
# #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01
# <a href="javascript:melon.play.playSong('19041301',35595136);" title="새삥 (Prod. ZICO) (Feat. 호미들) 재생">새삥 (Prod. ZICO) (Feat. 호미들)</a>
# 가수
# #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02
# <a href="javascript:melon.link.goArtistDetail('602056');" title="지코 (ZICO) - 페이지 이동">지코 (ZICO)</a>
# 앨범
# #lst50 > td:nth-child(7) > div > div > div
# <a href="javascript:melon.link.goAlbumDetail('11045985');" title="스트릿 맨 파이터(SMF) Original Vol.3 (계급미션) - 페이지 이동">스트릿 맨 파이터(SMF) Original Vol.3 (계급미션)</a>

# https://www.melon.com/chart/week/index.htm

header = {'User-Agent': 'Mozilla/5.0'}
req = requests.get(
    'https://www.melon.com/chart/week/index.htm', headers=header)

soup = BeautifulSoup(req.text, 'html.parser')

tbody = soup.select_one('#frm > div > table > tbody')
print(tbody)

ttbody = tbody.select('tr')

datas = []
for melon in ttbody:

    rank = melon.select_one('div > span').get_text()

    song = melon.select_one(
        'div > span > a').get_text()

    name = melon.select_one(
        'div.ellipsis.rank02 > a').get_text()

    album = melon.select_one(
        'td:nth-child(7) > div > div > div > a').get_text()

    print(rank)
    print(song)
    print(name)
    print(album)
    print()

    datas.append([rank, song, name, album])

print(datas)
