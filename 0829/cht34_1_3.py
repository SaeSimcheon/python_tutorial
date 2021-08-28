# 메서드 안에서 메서드를 호출할때는 다음과 같이 self.method
# 형식으로 호출해야함.
# self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다


class person:
    def greeting(self):
        print("hell")

    def hello(self):
        self.greeting()


james = person()
james.hello()
