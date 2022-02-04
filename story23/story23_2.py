'''

객체 생성시 자동으로 호출되는 생성자 __init__를 정의하고 그 안에 객체 내에 필요한
모든 변수를 초기화 해주면 초기화로 인한 문제를 방지할 수 있다.


설계도에 해당하는 클래스를 바탕으로 만들어진 객체에는 변수와 메소드가 담겨있다.
'''

class Simple:
    def __init__(self):
        self.i = 0
    
    def seti(self,i):
        self.i =i
    def geti(self):
        return self.i

s = Simple() # 생성 시에 생성자 __init__이 호출 되어서 attribute i를 0으로 초기화함.
print(s.geti()) # 이것도 이제 문제가 안 됨.
s.seti(200)
print(s.geti())