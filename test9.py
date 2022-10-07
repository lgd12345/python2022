import csv
import re

f = open('popSeoul.csv', 'r')
reader = csv.reader(f)
# csv객체값 출력
# print(reader)
print()
# 하나하나 뜯어서
# for i in reader:
#     for j in i:
#         print(j)

# for i in reader:
#     print(i)

# 하나의 리스트에 담아서 보여줌 형태 : [[],[],[]]
output = []
# for i in reader:
#     output.append(i)
# print(output)
print()
# 숫자만 읽어와서 ,를 제거하고 float 형태로 변환하여 output 추가
# 문자는 그대로 output 추가
# float 실수형인데.. float는 4바이트(32bit)의 수까지 표현하고, double은 8바이트(64bit)
print('--------------------------')
for i in reader:
    tmp = []
    for j in i:
        try:
            if re.search('\d', j):
               # (,)를 제거하고 float 형태로 변환하여 output 추가
                tmp.append(float(re.sub(',', '', j)))
            else:
                tmp.append(j)
        except:
            pass
    output.append(tmp)
print(output[:3])
print()

# '구','한국인','외국인','외국인 비율(%)' = 외국인/(한국인+외국인)*100' i[2]/(i[1]+i[2])*100
print('---------------------------------------------')
ko_fo = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in output:
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 5:                             # 5 보다 큰 것 만 출력
            ko_fo.append([i[0], i[1], i[2], foreign])
    except:
        pass

print(ko_fo)
print(len(ko_fo))
