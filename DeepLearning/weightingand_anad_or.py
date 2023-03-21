import numpy as np
# x=np.array([0,1])#입력
# w=np.array([0.5,0.5])#가중치
# b=-0.7#편향

# print(x*w)
# print(np.sum(w*x)) #sum() 메서드는 입력한 배열에 담긴 모든원소의 총합을 계산
# print(np.sum(w*x)+b)

def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp <=0:
        return 0
    else:
        return 1
##다른 파일에서 import weightingand_anad_or 한경우 밑 코드는 실행하지 않음
if __name__=="__main__":

    print(AND(0,0))
    print(AND(0,1))
    print(AND(1,0))
    print(AND(1,1))

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(w*x)+b
    if tmp <=0:
        return 0
    else:
        return 1
    
if __name__=="__main__":
    print(NAND(0,0))
    print(NAND(0,1))
    print(NAND(1,0))
    print(NAND(1,1))

def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
if __name__=="__main__":    
    print(OR(0,0))
    print(OR(0,1))
    print(OR(1,0))
    print(OR(1,1))