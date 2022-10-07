import codecs
import re

# 같은 폴더라서 파일명으로 파일을 읽을 수 있다. 아니면 경로작성 읽기모드(r)
f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
# 100까지만 출력한다.
print(script101[:100])
# r''이스케이프문자(\) 생략 가능
lines = re.findall(r'Monica:.+', script101)
print(lines[:3])
print(type(lines))
# script101에서 All: 검색하세요. 모든 문자가 1번 이상 (.+)
print()
All = re.findall(r'All:.+', script101)
print(All)
# All에서 마지막 출력
print()
print(All[-1])
# 길이 (리스트 길이) All이 출력된 갯수
print(len(All))
print("+++++++++++++++++++++++++++++++")
# 첫글자는 대문자 소문자 + : 로 된 문자열들 출력
char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))
# 리스트 길이
names = re.findall(char, script101)
print(len(names))
print("---------------------------------")
# 중복 제거
names = (set(re.findall(char, script101)))
print(set(names))
print(len(names))
print()
# 타입을 알기
setType = set(re.findall(char, script101))
print("setType의 타입 : ", type(setType))
# 등장인물 이름이 7자 이상인 사람 출력
for i in setType:
    if len(i) > 7:
        print("=7글자 이상인 사람= : ", i)

# 리스트로 타입을 바꿨습니다.
character = list(setType)
print(type(character))
print(character)

# character에서 : 제거해서 출력 1
character_list = []

for i in character:
    character_list += [i[:-1]]
print('character_list : ', character_list)
print("+++++++++++++++++++++++++++++++++++++++++")
# character에서 : 제거해서 출력 2
character_list2 = []
for i in character:
    #character_list2 = re.sub(':', '', i)
    #print(character_list2, end=' ')
    character_list2.append(re.sub(':', '', i))
print('\n$$$', character_list2)
##############################################
ch = 'Scene:'
ch = re.sub(':', '', ch)
print('ch>> ', ch)

a = '제 이메일 주소는 ggg@naver.com'
a += '오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 메일을 사용합니다.'
# [ggg@naver.com today@naver.com apple@gmail.com life@abc.co.kr]
aa = re.findall(r'[a-z]+@[a-z.]+', a)
print(aa)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# ['apple','at','ave','ama','asise','at','above'] 출력 1
words_list = []
for i in words:
    words_list += re.findall(r'a[a-z]+', i)

print("```````", words_list)
# apple,at,ave,ama,asise,at,above 출력 2 search
# m이 있으면 출력 해줘라
for i in words:
    m = re.search(r'a[a-z]+', i)
    if m:
        print(m.group())
print()
#  ['apple','asise','above'] 출력 3 match 시작점에 a 가 있어야 찾는다.
for i in words:
    m = re.match(r'a[a-z]+', i)
    if m:
        print(m.group())
print()
#  ['apple','asise','above'] 출력 4 (\d : 숫자),(\D : 숫자가 아닌것들)
for i in words:
    m = re.match(r'a\D+', i)
    if m:
        print(m.group())
print()
exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년 입니다.'
# ['91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년']
print(re.findall(r'\d.+년', exam1))
# ['91년', '97년', '2022년']
print(re.findall(r'\d.+?년', exam1))
print(re.findall(r'\d+.년', exam1))
print(re.findall(r'\d+년', exam1))
