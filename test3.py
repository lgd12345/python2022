
def seperate():
    a = int(input('수 입력 : '))
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')

# return 필요 a+b니까


def addResult(a, b):
    return a+b
# seperate()


print(addResult(3, 5))

ret = addResult(10, 20)
print(ret)

# range은 끝은 포함 안 됨

print("----------------------------")

# 1부터 10까지 합 구하기


def sum(num):  # 1+2+3+4+5+ ... 10
    hap = 0
    for i in range(1, num+1):
        print(i)
        hap += i
    return hap


print("sum : ", sum(10))  # 1부터 10까지의 합 출력

# dict이용해 있음 없음
dict = {1: 4, 2: 4, 3: 5}
if 1 in dict:
    print('있음')
else:
    print('없음')

print("++++++++++++++++++++++++++++++++++++")
# {1:4,2:4,3:5} 이렇게 나오도록 해보세요
nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

# 이건 그냥 합계구하는 걸 해버림
# def max_count(a, b, c):
#     return a+b+c
# counts = max_count(nums.count(1), nums.count(2), nums.count(3))
# print(counts)  # {1:4,2:4,3:5}

# print("nums keys() dict :", dict(nums.items()))


def max_count(nums):
    counts = {}  # {1:3, 2:2, 3:2}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


counts = max_count(nums)
print(counts)      # {1:4,2:4,3:5}
print(counts.values())
# counts의 벨류의 최대값
print(max(counts.values()))
print("++++++++++++++++++++++++++++++++++++")
# 다른 식으로 출력
# 최대 밸류 값 구하기
first = []  # list형
maxValue = max(counts.values())
for name, count in counts.items():
    print(name, ":", count)

    if(count == maxValue):
        first.append(count)
print("first :", first)
