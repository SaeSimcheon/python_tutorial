'''

객체에 변수와 메소드를 붙였다 떼었다 할 수 있다.

객체에는 함수도 추가할 수 있다.

'''

class Simple:
    def geti(self):
        return self.i

s = Simple() # 생성 시에 생성자 __init__이 호출 되어서 attribute i를 0으로 초기화함.
s.i = 27 ## 이 순간 변수 s에 담긴 i라는 변수가 생긴다.

print(s.geti()) ## s에 담긴 i가 생겼으므로 geti 메소드 호출이 가능하다.

s.hello = lambda :print("hi")
s.hello()

del s.i
del s.hello

s.hello()