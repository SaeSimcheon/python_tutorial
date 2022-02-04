'''
파이썬에 의해 호출되는 메소드를 가리켜 스페셜 메소드라고 함.

__name__

__init__ -> 객체 생성시 자동으로 호출되는 메소드

__len__ -> len 함수가 호출 되었을때 호출됨

__iter__ -> iter 함수가 호출되었을때 호출됨.

__str__

직접 그 이름을 명시하지 않고 다른 경로를 통해서 혹은 상황에 따라 자동으로 호출되는 메소드를 가리켜 스페셜 메소드라고 함.


__iter__ 객체는 iterator 객체를 반환해야한다. -> iterable 객체

'''

class car:
    def __init__(self,id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        print("__str__")
        return "Vehicle num" + self.id
    
    def __iter__(self):
        return iter(self.id) # 변수 id의 iterator 객체를 반환함.
    # 

def main():
    c = car("32러5243")
    print(len(c))
    print(str(c))
    
    for i in c:
        print(i,end = " ")
main()



