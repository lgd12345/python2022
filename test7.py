# w 쓰기 모드
# f = open('c:/test/새파일.txt', 'w')
# print(f)
# f.close()

# f = open('c:/test/새파일.txt', 'w')
# for i in range(1, 6):
#     data = '%d번째 줄 입니다. \n' % i
#     f.write(data)
# f.close()

# a : append 추가하는 거
# f = open('c:/test/새파일.txt', 'a')
# for i in range(6, 11):
#     data = '%d번째 줄 입니다. \n' % i
#     f.write(data)
# f.close()

# r : read
# 한줄 읽기
f = open('c:/test/새파일.txt', 'r')
line = f.readline()
print(line)

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# 여러줄 읽기
print()
f = open('c:/test/새파일.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

print('================================')
f = open('c:/test/새파일.txt', 'r')
data = f.read()
print(data)

f.close()

# close 포함
with open('c:/test/새파일.txt', 'w') as f:
    f.write('aa bb cc')

# 오류발생 : f 가 close된 상태라서
# data = f.read()
