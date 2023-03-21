#82p 밑바닥 부터 시작하는 딥러닝

import numpy as np
from sigmo import sigmoid

X=np.array([1.0,0.5])
W1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1=np.array([0.1,0.2,0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1=np.dot(X,W1)+B1

Z1=sigmoid(A1)
print(Z1)
#1층에서 2층오로의 신호전달
W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2=np.array([0.1,0.2])
#1층의 출력Z1이 2층의 입력이 된다는 것만 제외하면 앞 구현과 똑같다
A2=np.dot(Z1,W2)+B2
Z2=sigmoid(A2)

def identity_function(x):
    return x

W3=np.array([[0.1,0.3],[0.2,0.4]])
B3=np.array([0.1,0.2])

A3=np.dot(Z2,W3)+B3
Y=identity_function(A3) 