import numpy as np
X=np.array([[51,55],[14,19],[0,4]])

X=X.flatten()#X를 1차원 배열로 변환

print(X)

print(X[np.array([0,2,4])])#인덱스가 0,2,4인 원소 얻기

print(X>15)#X>15 결과는 bool배열 입니다
print(X[X>15])
