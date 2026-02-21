# defaulte it is public _ ->it is protected __-> it is private
class fac:
    __a="karnataka"
    def show(self):
        print("i am from karnataka",self.__a)
class A(fac):
    def show1(self):
       pass   # print(super()._a)
ob=A()
ob.show()
ob.show1()