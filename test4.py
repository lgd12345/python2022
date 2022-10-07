import re
# re 문자열에 관련된 정규식을 편하게 활용

text = "<title>지금은 문자열 연습입니다.</title>"
# 1. 0~7 사이 추출
print(text[0:7])
# 2. 문 있으며 위치값 출력
print(text.find('문'))
print(text.index('문'))
# 3. 파 있으면 위치값 출력 없으며 -1 출력
print(text.find("파"))
# 4. 파 있으며 위치값 출력 없으며 오류
# print(text.index('파'))

text1 = "    <title>지금은 문자열 연습입니다.</title>    "
text2 = ";"
# 1. test1 공백 제거하고 test2 연결
print(text1.strip()+text2)
# 2. test1 왼쪽 공백 제거하고 test2 연결
print(text1.lstrip()+text2)
# 3. test1 오른쪽 공백 제거하고 test2 연결
print(text1.rstrip()+text2)
# 4. test1 <title>을 <div>로 변경
print(text1.replace("<title>", "<div>"))
print(text1.replace("</title>", "</div>"))

# 정규식 표현법으로 사용 (상위에 임폴트 했음)
# 시작은 . 인듯
text3 = ("111<head>안녕하세요</head>22")
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)
# [0~9], [a~z]
# ab*c : abc, abbc, abbbbbc
# (*) = 0 이상 , (+) : 1 이상 , (?) : 0 이상 1 이하

print()
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
# search 사용 : <title>지금은 문자열 연습</title>
head = re.search('<title>.*</title>', text4)
head = head.group()
# <title>지금은 문자열 연습</title>
print(head)
#      안녕하세요... 지금은 문자열 연습
head = re.sub('<.+?>', '     ', text4)
print(head)
