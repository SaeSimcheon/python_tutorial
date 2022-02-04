'''
isinstance 함수와 object 클래스

isinstance -> 객체의 클래스 유형을 확인하는 함수



'''

class Simple:
    pass

s = Simple()
print(isinstance(s,Simple))

print(isinstance([1,2],list)) # 이 객체는 저 클래스의 객체인가?