'''

__init__ 메소드의 오버라이딩

메소드 오버라이딩을 할 수 밖에 없으면서 동시에 가려진 메소드를 호출해야만 하는 상황

자식 클래스의 __init__ 메소드 내에서는 부모 클래스의 __init__ 메소드를 호출해야한다. 객체 생성 시 객체 내에서
필요로 하는 모든 변수들을 적절히 초기화할 수 있다.

물론 이를 위해서는 다음 사실도 잘 기억해야한다.

지삭 클래스의 __init__은 부모의 변수를 초기화할 값도 함께 전달 받아야한다.


__init__은 오버라이딩 해야하는 메소드이면서 동시에 가려진 부모의 __init__을 반드시 호출해야하는 메소드이다.

'''


class Car:
    def __init__(self,id,f):
        self.id = id
        self.fuel = f
        
    def drive(self):
        self.fuel -=10
    
    def add_fuel(self,f):
        self.fuel+=f
    def show_info(self):
        print("id : " , self.id)
        print("fuel : ", self.fuel)
        
        
class Truck(Car):
    def __init__(self, id, f , c):
        super().__init__(id,f)
        #print(super().f)
        print(self.fuel)
        print(self.__dict__)
        #print(super().__dict__) 여기에는 있는데
        #print(super().id) 이건 왜 안될까? 
        #print(super().fuel) # 이게 맞음.
        # self.f -> 이거 호출 안 됨. -> 잘못한 것임.
        self.cargo = c
        print(self.__dict__)
        
        
    def add_cargo(self,c):
        self.cargo+=c
        print(self.__dict__)
    def show_info(self):
        super().show_info()
        
        print("cargo : ", self.cargo)
        

def main():
    c = Car("32러5234",0)
    c.add_fuel(100)
    c.drive()
    c.show_info()
    
    t = Truck("42럭5959",0,0)
    #print(t.fuel) 
    
    
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()
    
main()


'''
self.f와 t.f 가 호출되지 않는 것으로 미루어 보았을때, 상속받은 attribute는 다른 방식으로 관리되는 것 같다.
-> 아님 fuel을 호출했어야함.
super().__init__ 호출 후에는 자식 객체의 attribute로 호출할 수 있음.


'''