# class is the blueprint  for creating the object it is having propeties(attributes) and behavior(method)
# the class not exist in realworld  
# object is realworld entity

class Bottle:
    t='plastic' #attribute

    def drink(self):
        print("drinking bottle")
    print("intial")# globle space

# without creating the object
# print(Bottle().t)
# Bottle.drink()
# print(Bottle().t)
# with creating the object
object=Bottle()# object
object.drink()
print(object.t)

class student:#type of attribute
    branch="cse"# class attribute
    sec="c"
    def __init__(self,name,course):# init is the constructer this is dunder method
        self.name = name# self is the location of the object so that it is nessacery to pass this self
        self.course = course# instance attribute(is releted to each and every object)

    def Show(self):
            print(f"student name is {self.name} and course is {self.course}")
            #print(branch) cannot access the classsattribute without object inside the intance method
            print("inside the instance method",self.branch)
    # classmethod only access the class attribute not instance attribute direct 
    # not access the class attribute in the intance method
    @classmethod # decorator  at the rate
    def print1(cls,new_branch):
         print(cls.sec)
         cls.branch=new_branch
         print(cls.sec)
    @staticmethod
    def add(a,b):
         print(a+b)
         
s1=student("pallavi","python")
print(s1.name)
print(s1.course)
s1.Show()
s2=student("deepu","java")
s2.Show()
#classmethod calling
student.print1("ece")
print(student.branch)
#static method
s1.add(4,4)
#inheritance
class Animal:
     def eat(self):
          print("Animal eat food")
class dog(Animal):
     def sound(self):# it is neccessary to pass the self
          print("dog barks")
d1=dog()
d1.sound()
d1.eat()

class Bag:
    def __init__(self,material,pocket,zap):
         self.material=material
         self.pocket=pocket
         self.zap=zap
    def show(self):
         print(f"the material name is {self.material} the zap is {self.zap} the pocket name is {self.pocket}")

   
     
   
rebook=Bag("jute",5,2)
rebook.show()
campus=Bag("cotton",6,4)
campus.show()

class Human:
     def __init__(self,name):
          self.name=name
     def display(self):
          print(self.name)
class female(Human):
     def __init__(self,name,age):
          super().__init__(name)
          self.age=age
     def display(self):
           print(self.name,self.age)
ob=Human("pallavi")
ob1=female("deepu",15)
ob.display()

ob1.display()

class animal:
     def __init__(self,sound):
          self.sound=sound

     def voice(self):
          print(self.sound)
           
class pet:
     def __init__(self,breed):
          self.breed=breed

     def species(self):
          print(self.breed)
class Dog(animal,pet):
     def __init__(self, sound, breed):
        super().__init__(sound)
        pet.__init__(self,breed)

ob2=Dog("Barks","Golden Retrives")
ob2.voice()
ob2.species()
