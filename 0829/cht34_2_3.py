# 클래스의 위치 인수, 키워드 인수

# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수 사용 가능

# 1. 위치 인수와 리스트 언패킹

class person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
        

maria = person(*["마리아", 20, "서울시 서초구 반포동"])
print(maria.name, maria.age, maria. address)
