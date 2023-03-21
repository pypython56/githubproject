import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6,0.1)#0에서 6까지 0.1간격으로 생성
y1=np.sin(x)
y2=np.cos(x)


#그래프그리기
plt.plot(x,y1)
plt.plot(x,y2,linestyle="--",label="cos")#cos함수는 
plt.xlabel("x")#x축 이름
plt.ylabel("y")#y축 이름
plt.title("sin & cos")#제목
plt.legend()
plt.show()