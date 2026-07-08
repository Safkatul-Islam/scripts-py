import numpy as np

array_1 = np.arange(10)

array_2 = np.zeros((3, 3))

array_3 = np.ones((2, 4))

array_4 = np.arange(2, 21, 2)

array_5 = np.arange(1, 13)

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)

print(array_5.reshape((3, 4)))

