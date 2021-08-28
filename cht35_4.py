# 클래스의 위치 인수, 키워드 인수

# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수 사용 가능

# 2. 키워드 인수와 딕셔너리 언패킹을 사용하려면 **kwargs 사용

class person:
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.address = kwargs["address"]
        
        
maria1 = person(**{'name':'마리아','age':20,'address':'서울시 서초구 반포동'})
maria2 = person(name = '마리아', age = 20, address = '서울시 서초구 반포동')

print(maria1.name, maria1.age, maria1.address)
print(maria2.name, maria2.age, maria2.address)

