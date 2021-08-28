# self의 의미
# self는 인스턴스 자기 자신
# __init__(self) 여기 self에 들어가는 값은
# person() 이라고 할 수 있음
# self가 완성된 뒤에 james에 할당
# 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self 에 들어옴

# 그래서 greeting 메서드에서 print(self.hello) 처럼 속성 출력 가능


# 인스턴스를 만들 때 값 받기


class person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name 
        self.age = age
        self.address = address
        
    def greeting(self):
        print("{0} 저는 {1}입니다.".format(self.hello,self.name))
        

maria = person('마리아', 20 , '서울시 서초구 반포동')
maria.greeting()


print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

# 클래스 바깥에서 속성에 접근할 때 인스턴스.속성으로 접근
# 인스턴스 속성