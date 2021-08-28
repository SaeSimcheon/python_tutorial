# 공개 속성과 비공개 속성
# 클래스 바깥에서 접근할 수 있는 속성을 공개 속성이라
# 부르고, 클래스 안에서만 접근할 수 있는 속성을 비공개 
# 속성이라 부름

## 비공개 메서드 사용하기

#속성뿐만 아니라 메서드도 이름이 __ 로 시작하면
#클래스 안에서만 호출할 수 있는
#비공개 메서드가 됨

class person:
    def __greeting(self):
        print("hello")
        
    def hello(self):
        self.__greeting()
        
james = person()
james.__greeting()


# 보통 클래스 바깥으로 드러내고 싶지 않을 경우 사용
# 내부에서만 호출되어야 하는 경우