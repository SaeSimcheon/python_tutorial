# 비공개 속성 사용하기

class person:
    def __init__(self, name, age, address,wallet):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
        
maria = person("마리아", 20, "서울시 서초구 반포동",10000)
print(maria.hello)
#print(maria.__wallet) 접근하려고 하면 오류남
#비공개 속성은 클래스 안의 메서드에서만 접근 가능

