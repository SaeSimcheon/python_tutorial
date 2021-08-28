# 인스턴스는 자유롭게 속성을 추가할 수 있지만
# 일부만 허용하고 일부는 제한하고 싶을 수 있음
# __slots__ 사용

class person:
    __slots__ = ["name","age"]
    
maria = person()
maria.name = "마리아"
print(maria.name)
maria.age = 20
print(maria.age)
maria.address = "any"
print(maria.address)
