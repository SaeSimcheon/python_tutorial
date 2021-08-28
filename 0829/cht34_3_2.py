class person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
    
    def pay(self,amount):
        if amount > self.__wallet:
            print("돈이 모자라네")
            return
        self.__wallet -= amount
        print(self.__wallet)
        #print(self.__wallet)
        
        
maria = person('maria',20,'주소',10000)
maria.pay(3000)
maria.pay(3000)
maria.pay(3000)
maria.pay(3000)
