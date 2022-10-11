import numpy as np
import pandas as pd

# print(np.__version__)

# 3행 2열로 바꿈
ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)
print(ar4)
print()
# 2행 3열짜리를 만들어줌
ar5 = np.zeros((2, 3))
print(ar5)
print()
# 더하기 곱하기
# [11 12 13 14 15 16]
# [ 5 10 15 20 25 30]
ar1 = np.array([1, 2, 3, 4, 5, 6])
ar8 = ar1+10
print(ar8)
ar9 = ar1*5
print(ar9)
###############################################
data1 = [10, 20, 30, 40, 50]
print(data1)
data2 = ['10!', '20!', '30!', '40!', '50!']
print(data2)
# 데이터 타입이 int
sr1 = pd.Series(data1)
print(sr1)
# 데이터 타입이 object
sr2 = pd.Series(data2)
print(sr2)

data_dic = {
    'year': [2018, 2019, 2020],
    'sales': [350, 600, 700]
}

print(data_dic)
df1 = pd.DataFrame(data_dic)
print(df1)
# 리스트 안에 리스트
#        국어    영어    수학
# 중간고사  89.2  92.5  90.8
# 기말고사  89.2  92.5  90.8
df2 = pd.DataFrame([
    [89.2, 92.5, 90.8], [89.2, 92.5, 90.8]
], index=['중간고사', '기말고사'], columns=['국어', '영어', '수학'])
print(df2)
print()
# 위
print(df2.head())
# 위에서 부터 하나만 출력
print(df2.head(1))
# 밑
print(df2.tail())
# 밑에서 부터 하나만 출력
print(df2.tail(1))
print()
# 국어에 대해서
print(df2['국어'])
print(df2.국어)  # 비추천

# 엑셀파일로 내보내기 후 주석
# ,encoding= 'euc-kr' 한글로 변환해서 내보내기

# df2.to_csv('c:/test/score.csv', header='False')

# 읽을때 내보낼 때,encoding= 'euc-kr'했으면 읽을 때도, encoding= 'euc-kr'
df3 = pd.read_csv('c:/test/score.csv', encoding='utf-8')
print(df3)
