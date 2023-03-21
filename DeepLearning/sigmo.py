import numpy as np
import matplotlib.pylab as plt
from stepgraph import step_function

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__=="__main__":
    x=np.arange(-5.0,5.0,0.1)
    y=sigmoid(x)
    x2=np.arange(-5.0,5.0,0.1)
    y2=step_function(x2)

    plt.plot(x,y)
    plt.plot(x2,y2,linestyle="--")
    plt.ylim(-0.1,1.1)#y축 범위 지정
    plt.show()