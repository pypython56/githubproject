import numpy as np#numpy를 np로 바꾸어 쓸수 있다 간단하게 사용 가능
##호출한 모듈명과 파일명이 같으면 AttributeError: 가 뜬다
x=np.array([1,2,3])
y=np.array([2,4,5])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

print(x/2.0)