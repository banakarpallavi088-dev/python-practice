#comprehension means checking even or odd of many number using it we can determine in single line
l=[1,2,3,4,5,6,7,8,9,10]  # list ,set,dictionary
result=["Even" if i%2==0 else "odd" for i in l]
print(result)
# res={i:i**2 for i in range(1,11)}
# print(res)

res1={i:i*i if i%2==0  else i for i in range(1,20)}
print(res1)
res2={i:i*i for i in range(1,21) if i%2==0}
print(res2)

#lambda function:(ananymous)function without name

# def addition(a,b):
#     print(a+b)

# addition(3,2)

add1= lambda a,b : a+b
print(add1(3,4))
res3 = lambda a :"even" if a%2==0 else "odd" # lambda we can use with map,filter,reduce
print(res3(2))
#map reduce ,filter  map will perform the same operation on the each and very element
b=[1,2,4,5,6,7]
res4=map (lambda x:x*2 ,b)#map(function,itarator)
#map will perform the same operation on the each and very element
print(list(res4))
#filter filter the element base on the function
res5=filter(lambda x:x%2 ==0,b)#filter(function,itirator)
print(list(res5))
#reduce 
from functools import reduce
res6=reduce(lambda b,a:b+a,b)#reduce(function,itarator)
print(res6)

# list=[]
# for i in range(1,6,1):
#    item=int(input("enter the numbers"))
#    list.append(item)10,20,30,40,50

# print(list)

list1=eval(input("enter the values"))# using the eval we acn take input in single line but it is not correct way it isonly for string evaluation and it is treated as string
print(list1)
x=10
a=eval("x+5*4")
print(a)
#zip for making the pair  is uneqal run upto the pair
names=["pallavi","sita","rama"]
marks=[10,20,30]
course=["B.E","bca"]
res1=list(zip(names,marks,course))
print(res1)
for x,y in zip(names,marks):
    print(f"{x} scored {y}")

#take inout in single line
li=map(int,input("enter the number").split(","))#map will perform the same operation on the each and very element
print(list(li))
li1=list(map(int,input("enter the num").split(',')))
print(li1)


