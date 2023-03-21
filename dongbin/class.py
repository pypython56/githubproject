#클래스(class): 반복되는 불필요한 소스코드를 최소화 하면서
#               현실 세계의 사물을 컴퓨터 프로그래밍 상에서 
#               쉽게 표현할수 있도록 해주는 프로그래밍 기술

#인스턴스: 클래스로 정의된 객체를 프로그램 상에서 이용할 수있게 만드 변수

#클래스의 맴버 : 클래스 내부에 포함되는 변수
#클래스의 함수: 클래스 내부에 포함되는 함수 메소드라고 부릅니다.

class Car:
    #클래스의 생성자
    def __init__(self, name,color):#Car의 인스턴스
        self.name=name #클래스의 멤버
        self.color=color #클래스의 멤버
    #클래스 소멸자
    def __del__(self):
        print("인스턴스를 소멸 시킵니다")
    #클래스의 메소드
    def show_info(self):
        print("이름:",self.name,"/ 색상:",self.color)
    #Setter 메소드
    def set_name(self,name):#특정한 속성의 값을 변경할때 사용할수있다.
        self.name=name 
    
car1=Car("소나타","빨간색")#Car라는 자료형을 만든것
car1.show_info()
print(car1.name,"을 구매했습니다!")

car2=Car("아반떼","검은색")
car2.set_name("벤츠")
car2.show_info()    

#너무 많은 데이터가 할당이 되면 프로그램이 오작동할수있기 때문에
#더이상 사용되지 않는 변수(객체)를 메모리상에서 할당을 해제해준다
del car1

