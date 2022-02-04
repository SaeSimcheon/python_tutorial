'''

상속

부모 클래스가 갖는 모든 메소드가 자식 클래스에도 담긴다.

자식 클래스에는 별도의 메소드를 추가할 수 있다.



'''

class Father :
    def run(self):
        print("so fast!!")
    

class Son(Father): # 상속을 하는 방법
    def jump(self):
        print("so high !!")
        
def main():
    s = Son()
    s.run() # Father를 상속하는 Son의 객체를 대상으로 run 호출이 가능하다.
    s.jump() 

main()