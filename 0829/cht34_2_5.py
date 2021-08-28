# 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용
# 했었음
# 클래스로 인스턴스를 만든 다음에도
# 인스턴스.속성 = 값 형식으로 속성을 계속 추가 가능

class person:
    pass


maria = person()
maria.name = "마리아"

print(maria.name)

