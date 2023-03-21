import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

print(np.ndim(A))#배열의 차원수
print(A.shape)
print(np.ndim(B))#배열의 차원수
print(B.shape)

print(np.dot(A,B))#A와B는 2x2행렬 이며 이들 두행렬의 내적은 np.dot()을 이용한다

