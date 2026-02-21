class animal:# single inheritance
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name is {self.name}")
class human(animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def show1(self):
        print(f"name is {self.name} and age is {self.age}")

ani=animal("animal")
man=human("human",20)
ani.show()
man.show1()
#ani.show1() the parametre is different
# multiple inheritance#method resolution order

class Animal:
   name="tiger"
class human:
    name="pallavi"
class robots(human,Animal):# it is go to left to right first go to human check it is there ro not 
    pass

obj=robots()
#print(obj.name)
#multilevel inheritance the child direct access to grandparent property
class grandparent:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"  i am {self.name}")
class parent(grandparent):
    pass
    # def __init__(self,name,age):
    #     super().__init__(name)
    #     self.age=age
    # def show1(self):
    #     print(f"name is {self.name} and age is {self.age}")
class child(parent):
    pass
    # def __init__(self,name,age,marks):
    #     super().__init__(name,age)
    #     self.marks=marks
    # def show2(self):
    #     print(f"name is {self.name} and age is {self.age} and marks is {self.marks}")

obj1=child("pallavi")

obj1.show()
#obj1.show1()
#obj1.show2()
#hierarchical inheritance
class person:
    def __init__(self,name):
        self.name=name
        print("person constuctor")
    def show(self):
        print(f"i am {self.name}")
class employee(person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("employee constuctor")
    def show1(self):
        print(f" i am {self.name} and my age {self.age}")
class student(person):
    def __init__(self, name,fees):
        super().__init__(name)
        self.fees=fees
        print("student constuctor")
    def show2(self):
        print(f"i am {self.name} and fees is {self.fees}")

ob1=student("deepu",100000)
ob2=employee("pallavi",22)
ob1.show2()
ob2.show1()