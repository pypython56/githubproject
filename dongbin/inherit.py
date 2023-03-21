#상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
#프로그램을 계층적으로 구성할수있고 불필요한 소스코드 작성을 줄일수 있다
#부모와 자식 관계가 존재합니다
#자식 클래스: 부모 클래스를 상속 받은 클래스

class Unit:
    def __init__(self,name,power):
        self.name=name
        self.power=power
    def attack(self):
        print(self.name,"이(가) 공격을 수행합니다.[전투력:",self.power,"]")

class Monster(Unit):#상속 표현법
    def __init__(self, name, power,type):
        self.name=name
        self.power=power
        self.type=type
    def show_info(self):
        print("몬스터 이름:",self.name,"/ 몬스터 종류:",self.type)


monster=Monster("슬라임",10,"초급")
monster.attack()#Monster 클래스에서는 attack함수가 존재하지 않지만 Unit클래스에서 상속 받았으므로 사용가능 하다
monster.show_info()

unit=Unit("홍길동",375)
unit.attack()    
        