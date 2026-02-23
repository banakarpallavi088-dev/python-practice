class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Teacher(person):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.__salary=salary
    # def set_salary(self,salary):# accesing the value
    #     self.__salary=salary
    def get_salary(self):
        return self.__salary

    def show(self):
        print("i am Teacher")
        print(f"name is {self.name} and id is {self.id} and salary is {self.__salary} ")
        
class staff(person):
    def __init__(self, name, id,dept):
        super().__init__(name, id)
        self.dept=dept
    def show(self):
        print("i am steff")
        print(f"name is {self.name} and id is {self.id} and dept is {self.dept}")
class Student(person):
    def __init__(self, name, id,marks):
        super().__init__(name, id)
        self.__marks=marks
    # def set_marks(self,marks):# accesing the value if we went change the mark on that time use it
    #     self.__marks=marks
    def get_marks(self):
        return self.__marks

    def show(self):
        print("i am student")
        print(f" name is {self.name} and id is {self.id} and marks is{self.__marks}")
ob1=staff("pallavi",55,"cse")
ob2=Student("deepu",1,100)
ob=Teacher("keerti",2,600000)
ob.show()
print("the salary is",ob.get_salary())

ob1.show()
ob2.show()
print("the marks",ob2.get_marks())