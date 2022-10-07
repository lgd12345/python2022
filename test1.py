from tkinter.tix import DirTree
from regex import P
from sympy import li


print('Hello')

a = 0
print(a)
# 컨트롤 + / : (주석)
# 쉬프트 + 알트 + 화살표 한줄 복사
# 쉬프트 + 알트 + F 정렬

# 타입 알고 싶으면 이렇게
print(type(a))

b = 'Hello World'
print(b)
print(type(b))
# 따옴표 포함
c = "'안녕하세요'"
print(c)
d = "\'안녕하세요!\'"
print(d)
# 문자 연결
print(b+d)
# 계산
print(3*2)
# 문자의 반복
print('2'*3)
print(c*3)
# 오류발생 문자열의 내용을 바꿀 수 없음
# b[1] = 'c'
print('-------------------------------------')
print(b)
# 문자 추출 : 문자열 첫번째 [0]
print(b[0])
# 문자 추출 : 문자열 끝 [-1]
print(b[-1])
print(b[-2])

# 0~2까지 문자 추출
e = '반갑습니다.'
print(e)
print(e[0:2])
print(e[1:3])
# 전체
print(e[:])
print(e[0:6])
# 2개씩 증가해서 나온다. 반 습 다
print(e[0:6:2])

# 해당 문자의 위치값 find
print(e.find('반'))
print(e.find('니'))
# 없으면 -1 반환
print(e.find('안'))

# 해당 문자의 위치값 index
print(e.index('반'))
# index는 없으면 오류발생됨
# print(e.index('안'))

# join : 사이에 넣어준다. bb가 바뀌는 것이 아님
bb = ','
print(bb.join('ABCD'))
print(bb)
# upper : 대문자, lower : 소문자 바꾸기
print(b.upper())
print(b.lower())
print(b)

# 공백제거 lstrip : 왼쪽, rstrip : 오른쪽, strip : 양쪽
dd = '          py           '
print(dd.lstrip())
print(dd.rstrip())
print(dd.strip())

# split : 대괄호로 해서 나누어짐
aa = 'Now is aa bb cc'
print(aa.split())

# 리스트 (list)
l = list()
print(l, type(l))

lst = [1, 2, 3]
print(lst, type(lst))
# 리스트 l2 ==> 1 부터 11 까지로 이루어진 리스트 l2 생성
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100]
# l2의 유형 확인
print(l2, type(l2))
# l2의 첫번째 값 (1)
print(l2[0])
# l2의 길이 (11)
print(len(l2))

# l2의 마지막 값 출력 (100)
print(l2[-1])
print(l2[len(l2)-1])  # l2에 마지막 원소(l2의 길이-1)

# l2의 첫번째 값을 99로 수정
l2[0] = 99
print(l2)
# list 안에 list 들어갈 수 있다. 길이수는 변화 없다.
l2[1] = [1, 2, 3]
print(l2)
print(len(l2))

# 리스트에 문자넣기
l2[2] = '문자'
print(l2)
# 추가 999추가
l2.append(999)
print(l2)
# 삭제 5
l2.remove(5)
print(l2)

print('-a1-b1-c1-d1----------------------')
# 1,2,3이루어진 a1 리스트 생성
# 'life','is','too','short'로 이루어진 b1 리스트 생성
# 1,2,'life','is' 로 이루어진 c1 리스트 생성
# 1,2,(3,4)('life','is') 로 이루어진 d1 리스트 생성
a1 = [1, 2, 3]
b1 = ['life', 'is', 'too', 'short']
c1 = [1, 2, 'life', 'is']
d1 = [1, 2, [3, 4], ['life', 'is']]
# d1의 첫번째 값 출력
print(d1[0])
print(d1[3])
print(d1[3][-1])
print(d1[0:3])
# insert는 자리 지정후 입력
d1.insert(2, 'aa')
# append 무조건 맨뒤
d1.append('dd')
print(d1)
# aa,dd 더해 져서 6이 출력
print(len(d1))
# 맨마지막에 추가된 것 제거
d1.pop()
print(d1)
# 2가 몇번 들어갔느지 센다
a2 = [2, 1, 0, 2, 3, 2, 4, 2]
print(a2.count(2))

#################################
# 튜플(tuple)
print('튜플  ======================')
t = tuple()
print(t, type(t))

t1 = (1, 2, 3)
print(t1, type(t1))
# t1의 0번째, 0에서 2까지
print(t1[0], t1[0:2])
print(t1, t1)
# 오류 발생
# t[0] = 5 튜플은 수정불가 오류 발생
t4 = (1, 2, (3, 4), ('life', 'is'))
print(t4)

# dict 클래스 키값을 넣으면 벨류값을 리턴한다. 자바의 map과 유사
print('딕  ======================')
d = dict()
print(d, type(d))
d1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(d1, type(d1))
print(d1['a'])
# 키 값에 d 없어서 오류남
#  print(d1['d'])

# 변경가능!
d1['c'] = 33
print(d1)

# 키 값 만 알고 싶을 때
print("keys : ", d1.keys)
print("keys() : ", d1.keys())
# 밸류 값만 알고 싶을 때
print("valuse : ", d1.values)
print("valuse() : ", d1.values())
# 키값 밸류 값 같이 알고 싶을 때
print("items : ", d1.items)
print("items() : ", d1.items())
# 타입 확인
print("type keys() :", type(d1.keys()))
print("type values() :", type(d1.values()))
print("type items() :", type(d1.items()))
# (자료형)타입을 list로 바꾸기
print("type list", type(list(d1.keys())))
#  name은 Hong, pnone 은 01011112222, birth는 0814로 이루어진 dict이라는 dictionary 생성
dict = {
    'name': 'Hong',
    'pnone': '01011112222',
    'birth': '0814'
}
print(dict)
print("dict items() : ", dict.items())
# dict 에 key 값이 1, value 가 'a'추가
dict[1] = 'a'
print(dict)
# dict 에 key 값이 pet, value 가 'dog'추가
dict['pet'] = 'dog'
print(dict)
# key가 pet인 value 값 출력
print(dict['pet'])
# dict의 키 값만 출력
print("dick keys() :", dict.keys())
# dict의 키 값만 출력 리스트 형태로 전환 출력
print("dick keys() list :", list(dict.keys()))
# 담아서 출력
lst = list(dict.keys())
print(lst)
# 삭제하기 (키값으로 삭제)/////////////
del dict[1]
print('dict : ', dict)
# 전부 삭제//////////////////////////
dict.clear()
print(dict)

# set 중복 허용 하지 않음, 키 값만 가지고 있음
print('set=================')
s1 = {1, 2, 3, 4}
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 5])
print(s2, type(s2))
# 교집합
print(s1 & s2)
# 합집합
print(s1 | s2)
# 차집합
print(s1 - s2)
print(s2 - s1)
print(s2.difference(s1))
