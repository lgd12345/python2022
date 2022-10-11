from bs4 import BeautifulSoup
import urllib.request as req

html = """
<html><body>
        <div id= "meigen">
        <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
        <h1>위키북스 도서2</h1>
</body></html>
"""
# 위키북스 도서만 추출해서 출력
soup = BeautifulSoup(html, 'html.parser')
# 방법1
h1 = soup.find('h1').string
print(h1)
# 방법2
h1_1 = soup.select_one('h1').string
print(h1_1)
# div태그 안에 있는 애만 뽑은 것
h1_2 = soup.select_one('div>h1').string
print(h1_2)
# div 태그의 아이디로 지정해서 뽑은 것
h1_3 = soup.select_one('div#meigen>h1').string
print(h1_3)

# select 여러개 가져와서 쓸 때
li_list = soup.select('div#meigen > ul.items > li')
print(li_list)

for i in li_list:
    print(i.string)

print()

lis = soup.select('li')
print(lis)

for li in lis:
    print(li.string)
print()
