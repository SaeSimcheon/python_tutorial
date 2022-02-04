'''

객체에 변수를 추가하는 것처럼 '클래스'에도 변수를 추가할 수 있다.

어떻게 변수를 추가할 수 있는 것일까 ?

파이썬의 클래스는 클래스이자 객체이다.

프로그래머가 직접 정의하는 클래스들은 type이라는 클래스의 객체이다.

'''

class Simple:
    def __init__(self,i):
        self.i = i
    def geti(self):
        return self.i


Simple.n = 7
print(Simple.n)

s1 = Simple(3)
s2 = Simple(5)

print(s1.n,s1.geti(),sep = ",")
print(s2.n,s2.geti(),sep = ",")

'''
각 객체에서 n에 접근하게 되면 객체에서 일단 n을 찾는다. 그러나 두 객체에서 n이 없기 때문에 파이썬은 해당 객체의 클래스를 찾아가서 n을 찾는다.
->객체에 찾는 변수가 없으면 해당 객체의 클래스로 찾아가서 그 변수를 찾는다.

클래스에 속하는 변수를 만들 수 있다.


'''