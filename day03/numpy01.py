import numpy as np

a = np.array([[2, 3], [5, 2]])
print(a)

d = np.array([2, 3, 4, 5, 6])
print(d)
print(d.shape)

e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)
print(e.shape)
print(e.dtype)
print("-------------------------------------------")
print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(np.arange(2, 10))  # 2이상 10미만의 원소로 구서오딘 1차원 배열

a = np.ones((2, 3))

# 행과 열이 바뀜
b = np.transpose(a)
print(b)

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 13, 14], [26, 27, 28]])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

######################################
d = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]])
print(d)
d_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 7, 8, 9, 9]]
print(d_list)
print(type(d_list))
# d_list[:2] = 0 #오류 발생 바꿀 수 없다.
d_list[2] = 0
print(d_list)
print("-------------------------")
print(d)
# 오류 안 남 numpy는 범위지정해 바꿀 수 있다.
d[:2] = 0
print(d)
print(np.arange(10))
