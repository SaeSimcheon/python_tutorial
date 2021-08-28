'''
특정 클래스의 인스턴스인지 확인하기

현재 인스턴스가 특정 클래스의 인스턴스인지 확인 할때는 isinstance함수를
사용함. T/F
'''


class person:
    pass


james = person()
print(isinstance(james, person))
