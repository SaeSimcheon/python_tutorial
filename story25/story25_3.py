'''

object 클래스


파이썬의 모든 클래스는 object 클래스를 직접 상속 혹은 간접 상속한다.

type 클래스도 obejct class를 상속한다. -> issubclass 함수를 통해서 확인할 수 있다.

'''

class simple:
    pass

print(isinstance(simple(),object))
print(isinstance([1,2],object))

print(issubclass(type,object))

print(issubclass(object,type))

print(dir(object))