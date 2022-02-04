'''

파이썬에서는 클래스도 객체이다.

type은 사실 클래스의 이름이다. 함수처럼 사용할 수 있고, 이때 자료형의 종류를 알려준다.

클래스도 객체이다.

클래스는 type이라는 클래스의 객체이다.

'''

print(type) # type이 클래스인 사실을 알 수 있다. type이 그저 함수라면 function type at ~ 의 형태로 출력이 된다.

print(type([1,2])) # list의 객체임을 알려준다.

print(type(list)) # type 클래스의 객체임을 알려준다.

class Simple:
    pass

print(type(Simple)) # 사용자 지정 클래스도 type 클래스의 객체이다.

print(isinstance(list,type))
print(isinstance(object,type)) # 이 관계는 대체 뭘까 ?
print(isinstance(type,object)) # 이 관계는 대체 뭘까 ?
print(isinstance(type,Simple))
print(isinstance(Simple,object)) 
print(isinstance(Simple,type))