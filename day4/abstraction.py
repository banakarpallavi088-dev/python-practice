# method overloading not working in python by using another concept we can done
# using this we can done the method overloading
class ABC:
    def show(self,x=None,y=None):
        if x==None and y==None:
            print("this is python program")
        elif x !=None and y==None:
            print("Hello",x)
        else:
            print("addition",x+y)
ob=ABC()
ob.show()
ob.show(2)
ob.show(3,5)


# abstraction abc is packge import the ABC module  abc means abstract base class
from abc import ABC, abstractmethod # it is neccessry
class abstract(ABC):
    @abstractmethod
    def parameter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class square(abstract):# inheriting the abstract class the all declare method should be there in child class if not it gives an error
    def __init__(self,side):
        self.side=side
    def area(self):
        print("inside the square")
    def parameter(self):
        print("parametr inside the square")
class circle(abstract):
    def __init__(self,radius):
        self.radius=radius
    @property
    def area(self):
        print("area is abstract method")
    def parameter(self):
        print("parameter method is abstract method")

object=circle(3)
print(object.radius)
object.area # it is call without () this due to @ at the rate is used at the up af area method is called decoretion we create by your own
object.parameter()
object1=square(4)
print(object1.side)
object1.area()
object1.parameter()
# dunder method
# these are special method that start and end with double underscores
#like __init__,__add__
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "hello how are you"
    def __add__(a,b):
        return a.age + b.age

o1=Animal("lion",10)
o2=Animal("tiger",10)
print(o1.name)
print(o1+o2)
# more age to add using tuple 

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "hello how are you"
    def __add__(a,b):
        sum=0
        for i in b:
            sum=sum+i.age

        return a.age + sum

ob1=Animal("lion",10)
ob2=Animal("tiger",10)
ob3=Animal("dolphin",10)
ob4=Animal("cat",15)
print(ob1)
print("the tuple sum",ob1+(ob2,ob3,ob4))# in tuple
# decoreter method 
def my_decorate(param):# parameter is hello
    def wrapped(a,b):
        print("hello ")
        param(a,b)# hello()
        print("come join us")
    return wrapped
# @my_decorate
# def hello():
#     print("we are learning python")
@my_decorate
def add(a,b):
    print("i am pallavi",a+b) 

# hello# calling the hello method without ()
add(2,3)
# args and 
def addition(*args):# *args is the tuple name can change
    sum=0
    for i in args:
        sum+=i
    print(sum)
addition(1,2,3,4,5,6,7,8,3,5,6,2)

