'''

    Name mangling
        - name -> __name
    when to use name mangling
    https://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private/70900#70900
    

    attribute vs property
        - Properties are a special kind of attribute. 
        - @property -> convert a method into an attribute. 
        - property_name.setter
    https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute/7377013

    Difference between attributes and properties in Python
    https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/


    property is class.

    https://docs.python.org/3/library/functions.html?highlight=property#property
    

    Everything is object in python    
    https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html

    



'''

class Member :
    __counter = 0
    def __init__(self,no,name,weight,height):
        self.__name = name
        self.__weight = weight
        Member.__counter +=1
        self.no = no

    @property
    def wweight(self):
        return self.__weight
    @wweight.setter
    def asd(self,value):
        self.__no = value
    def __str__(self) -> str:
        return self.__name + " " + str(self.no)

    @classmethod
    def max(cls) -> int:
        return cls.__counter 
class subMember(Member):
    def __init__(self,no,name,weight,height,age):
        super().__init__(no,name,weight,height)
        self.no = no
        self.__age = age





kim = Member(15,"kim",75,175)
lee = Member(15,"lee",75,175)
haek = Member(15,"haek",75,175)

print(Member.max())

park = subMember(20,"kim",75,175,10)

#print(kim.wweight)

kim.asd = 5
#print(kim.wweight)
#print(kim.__no)
#print(kim.no)
#print(kim.no)
print(kim)
print(park.no)
#print(kim._Member__no)
#print(park._subMember__no)
#print(park._Member__no)


