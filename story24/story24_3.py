'''

메소드 오버라이딩과 super

상속 관계에 있어서 부모 클래스가 갖는 메소드와 동일한 이름의 메소드를 자식 클래스가 정의하는 경우도 있음.
이 경우 클래스의 메소드는 보이지 않는 상태가 됨. (지워진 상태가 아니라 호출이 불가능한 상태를 의미함.)


'''

class Father :
    def run(self):
        print("so fast!!,dad st")


class Son(Father): # 상속을 하는 방법
    def run(self,i):
        super().run()
        print(str(i)+" so fast!!,son st")
        
    def run2(self):# 이런 방식으로 호출할 수 있음.
        super().run()
    
        
def main():
    s = Son()
    s.run(10) # Son의 run 메소드가 호출된다. 가려져서 Son에서 정의된 run으로 작동된다.
    s.run2()
    

main()


'''
son 객체에는 두 개의 run 메소드가 있는 상태인가 ?

맞다. Son 객체에는 Father의 run 과 Son의 run이 모두 존재한다. 다만 Father 의 run이 가려졌을 뿐이다. 

'''

