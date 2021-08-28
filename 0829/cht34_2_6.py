# __init__ 메서드가 아닌 다른 메서드에서도 속성 추가 가능.
# 단 메서드를 호출해야 속성이 됨

class person:
    def greeting(self):
        self.hello = "hello"
        print(self.hello)

        
maria = person()
# maria.hello attribute가 없다고 나옴
maria.greeting()
print(maria.hello)
# 이러면 에러 없음