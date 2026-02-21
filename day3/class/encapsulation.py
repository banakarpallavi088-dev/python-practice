# defaulte it is public _ ->it is protected __-> it is private
class fac:
    __a="karnataka"
    def show(self):
        print("i am from karnataka",self.__a)
class A(fac):
    def show1(self):
       pass   # print(super().__a) we can't access it
ob=A()
ob.show()
ob.show1() # abstraction not show the internal working but encapsulation wrapping the attributes amd methods
# access the private attributes
class B:
    def __init__(self,location):
        self.__location=location
    def set_loc(self,location):
        self.__location=location
    def get_loc(self):
        return self.__location

o=B("karnataka")
print(o.get_loc())
print(o.__location)
