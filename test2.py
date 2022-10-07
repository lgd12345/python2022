# 조건문 파이썬은 중괄호 안 씀, 들여쓰기가 같은 것 까지 묶임
from numpy import number


a = 2
if (a == 1):
    print(1)
else:
    print("1 아님")
print("=========================")
if (a == 1):
    print(1)
elif(a == 2):
    print(2)
else:
    print(3)
# False True로 나옴
x = 3
y = 2
print(x == y)
print(x != y)

money = 1300
if money >= 1200 and money < 3500:
    print('버스 탈 수 있다.')

print(1 in [1, 2, 3])
print(x in [1, 2, 3])
# ?
print(x not in [1, 2, 3])
# 없으면 트루
print('i' not in 'python')

if money < 10:
    pass
else:
    print('저금!!')
print("반복문-----------------------------")
# 반복문
for i in [1, 2, 3]:
    print(i)
# 투플 반복문
for i in (1, 2, 3):
    print("투플 반복문", i)

for i in 'Hello':
    print(i, end=' ')

print()

# test_list라는 리스트 생성 one, two, three
test_list = ['one', 'two', 'three']
# test_list의 값을 반복문을 이용해서 하나씩 출력 one! two! three!
for i in test_list:
    # print(i+'!')
    x = i+'!'
    print(x)

number = 0
for score in [90, 25, 67, 45, 93]:
    number += 1
    if score >= 60:
        print("%d 학생은 합격입니다." % number)
    else:
        print("%d 학생은 불합격입니다." % number)
# while
print("while===========================")
num = 5
while(num > 0):
    print(num)
    num -= 1

# while 문 이용하고 num = 10
# 10 9 8 7 ====end====
num = 10
while(num > 0):
    if(num == 6):
        print('---end---')
        break
    print(num, end=' ')
    num -= 1

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')

# 100까지 수 중 7의 배수와 합계 출력
sum = 0
for i in range(101):
    if(i % 7 == 0):
        sum += i
        print(i, end=' ')

print()
print(sum)
# 한칸 띄우고 적기
print("\nsum : ", sum)

# for i in range(100):
#     if(i != 0 | i % 7 == 0):
#         sum += i
#         print(i, end=' ')
# print("\nsum : ", sum)
print()
# * * *
# * * *
# * * *  만들기
for i in range(3):
    for j in range(3):
        print('*', end=' ')
    print()

print("++++++++++++++++++++++++++++++++++++++")

i = 0
while i < 5:
    i += 1
    print('*'*i)
