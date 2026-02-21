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
    def set_loc(self,location):# accesing the value
        self.__location=location
    def get_loc(self):
        return self.__location

o=B("karnataka")
print(o.get_loc())
class student:
    
    def __init__(self):
        self.__mark=0
    def set_mark(self,value):
        if 0<= value <=100:
            self.__mark=value
        else:
            print("invalid marks")
    def get_mark(self):
        return self.__mark
object1=student()
object1.set_mark(45)
print(object1.get_mark())
#print(o.__location) using getter and setter method we can access the private method 
class Animal:# it is method overriding at runtime
    
    def show(self):
        print("animal")
    def show(self,name): 
        
       print("hello......")
        
    def show(self,a):
        print("hi....")
class human(Animal):
    def show(self):
        print("hello how are you")

o1=Animal()
o1.show("pallavi")
o2=human()
o2.show()
#duck typing
class C:
    def show(self):
        print("hello")
  
class D(C):
    def show(self):
        print("hi...")
def write(person):
        person.show()
object=D()
object2=C()
write(object)# it does metter which object is useing if the methpod is there it print not give error
write(object2)