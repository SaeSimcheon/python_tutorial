'''

다중상속

둘 이상의 클래스를 상속하는 것도 가능하지만, 둘 이상의 클래스를 동시에 상속하면 구조가 복잡해지고 주의해야할 사항들이 늘어나기 때문에 유의해야한다.

일단 단일 상속에만 관심을 두도록하자.


'''

class Father :
    def run(self):
        print("so fast!!")

class Mother :
    def dive(self):
        print("So deep!!")

class Son(Father,Mother): # 상속을 하는 방법
    def jump(self):
        print("so high !!")
        
def main():
    s = Son()
    s.run() # Father를 상속하는 Son의 객체를 대상으로 run 호출이 가능하다.
    s.dive() # Mother을 상속하는 Son의 객체를 대상으로 dive 호출이 가능하다.
    s.jump() 

main()