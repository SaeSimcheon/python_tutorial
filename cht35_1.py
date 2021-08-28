# 클래스에서 속성을 만들고 사용
# __init__ 메서드 안에서 self.속성에 값을 할당

class person:
    def __init__(self):
        self.hello = '안녕하세요'
    
    def greeting(self):
        print(self.hello)
        

james = person()
james.greeting()

# 앞뒤로 __가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드로
# 스페셜 메서드 혹은 매직메서드라고 부름.