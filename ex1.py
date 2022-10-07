import numpy as np
import pandas as pd
import csv
import re


# 1 문제
# 1-1 2020
print(" 문제 1번 ")
str = '20201231Thursday'
print(str[0:4])
#  print(str[:4])
# 1-2 1231
print(str[4:8])
# 1-3 Thursday
# str[8:]
str2 = re.search('\D+', str)
# print(str2)
str2 = str2.group()
print(str2)

# 2 문제
print(" 문제 2번 ")
a = ['쓰', '레', '기', '통']
a.reverse()
print(a)
# ['통', '기', '레', '쓰']

# 3 문제
print(" 문제 3번 ")
dic = {
    'year': 2020,
    'mm': 12,
    'dd': 31,
    'day': 'Thursday',
    'weather': 'snow'
}
# dict_keys(['year','mm','dd','day','weather'])
print(dic.keys())
# dixt_values(['2020','12','31','Thursday','snow'])
print(dic.values())

# 5 문제
print(" 문제 5번 ")
for i in range(1, 6):
    for j in range(i):
        print('*', end=' ')
    print()

# 6 문제
print(" 문제 6번 ")


def avg(*args):
    x = 0
    for i in args:
        x += i
    return x/len(args)


print(avg(5, 3, 12, 9))
print(avg(2.4, 3.2, 7.3))
print(avg(10, 5))


# 7 문제
print(" 문제 7번 ")
data = pd.DataFrame([
    [500, 450, 520, 610], [690, 700, 820, 900], [1100, 1030, 1200, 1350], [
        1100, 1030, 1200, 1350], [1100, 1030, 1200, 1350], [1100, 1030, 1200, 1350]
], index=['2015', '2016', '2017', '2018', '2019', '2020'], columns=['1분기', '2분기', '3분기', '4분기'])

# ,encoding= 'euc-kr' 한글로 변환해서 내보내기
# data.to_csv('c:/test/data.csv', header='False', encoding='euc-kr')
data2 = pd.read_csv('c:/test/data.csv', encoding='euc-kr')
print(data2)
