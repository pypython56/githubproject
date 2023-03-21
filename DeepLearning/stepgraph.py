import numpy as np
import matplotlib.pylab as plt


# x1=np.array([-1.0,1.0,2.0])
# y1=x1>0
# print(y1)#bool형 출력함

def step_function(x):
    return np.array(x>0,dtype=np.int64)  #bool형 대신 int 0,1로 반환 int64로 작성하여야 오류 안남

if __name__=="__main__":
    x=np.arange(-5,5,0.1)#x의 범위 -5~5까지 0.1씩 변화
    y=step_function(x)
    plt.plot(x,y)
    plt.ylim(-0.1,1.1)#y축의 범위 지정
    plt.show()
