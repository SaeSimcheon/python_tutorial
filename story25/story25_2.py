'''

상속과 isinstance


'''


class fruit:
    pass

class apple(fruit):
    pass

class super_apple(apple):
    pass

sa = super_apple()

print(isinstance(sa,super_apple))

print(isinstance(sa,apple))
print(isinstance(sa,fruit))


'''

super_apple 클래스는 apple 클래스를 직접 상속한다.
super_apple 클래스는 apple 을 상속함으로써 fruit클래스를 간접 상속한다.

간접 상속도 상속이다.


'''
