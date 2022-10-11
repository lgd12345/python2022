import imp
from turtle import pd


import pandas as pd
# name ==> 'Mark','Jane','aaa','rr'
# age ==> 33,44,55,11
# score ==> 91.2,88.5,55.6,88.9
data = {
    'name': ['Mark', 'Jane', 'aaa', 'rr'],
    'age': [33, 44, 55, 11],
    'score': [91.2, 88.5, 55.6, 88.9]
}
print(data)
print(type(data))
# data 를 데이터 프레임으로 생성
df = pd.DataFrame(data)
# <class 'pandas.core.frame.DataFrame'>로 타입이 변경됨 (쉽게 이용할 수 있는 형태로 변경)
print(df)
print(type(df))
print()
print(df.sum())
print(df.mean())
# age
print()
print(df.age)
print(df['age'])
# year sales
# 2018 350
# 2019 400
# 2020 1050
# 2021 2000
# 2022 1000
data_dic = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [350, 400, 1050, 2000, 1000]
}
# 데이터프레임으로
df2 = pd.DataFrame(data_dic)
print("="*30)
#          1반 2반 3반
# 중간고사 89.2,92.5,90.8
# 기말고사 92.8,89.9,95.2

df3 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   columns=['1반', '2반', '3반'],
                   index=['중간고사', '기말고사'])
print(df3)
# 인덱스 없으면
#      1반    2반    3반
# 0   89.2  92.5  90.8
# 1   92.8  89.9  95.2
df0 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   columns=['1반', '2반', '3반'])
print(df0)
# 중간에 추가 가능
df4 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   columns=['1반', '2반', '3반'])
df4.index = ['중간인덱스', '기말인덱스']
print(df4)
# 중간에 추가
df5 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]])
df5.index = ['중간인덱스', '기말인덱스']
df5.columns = ['ㄱ', 'ㄴ', 'ㄷ']
print(df5)

# df3 sum() 출력
print()
print(df3.sum())
# 1반의 합계 출력
print(df3['1반'].sum())
# 1반의
print(df3.mean())
print(df3['1반'].mean())
print("===============================")
# df5 를 df5.csc내보내기
df5.to_csv('day03/df5.csv', header='False')
df_read = pd.read_csv('day03/df5.csv', encoding='utf-8')
print(df_read)
