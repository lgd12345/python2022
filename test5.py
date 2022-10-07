import requests

URL = 'https://www.naver.com'
response = requests.get(URL)
# 코드 200 성공이 뜸 잘 접속 되었다는 뜻
html_text = response.text
print(response)
# print(html_text)

# 내가 찾는 글자가 나오는 위치값이 뜬다.
# 수집할 때 (크롤링) 이런 방식을 이용한다...
print(html_text.find('<h3 class="blind">'))
print(html_text.find('급'))
