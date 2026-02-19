#data stucture data type collection
# list,tuple,set,dictionary
'''list instread  of array in python we use list but we can use array by 
importint the numpy librery
mutable,ordered,duplicate allowed,heterageneous, list can change '''

l=[3,5,6,7,"hello",True,"hi"]
print(l)



for i in range(len(l)):
    print(l[i])
if(l[i].isalpha() and l[i].isdigit ):
    print("the list is have both")
else:
    print("list is not having both")
#slicing methods
print(type(l))
print(len(l))
print(l[1:4:1])
print(l[:-8:-1])
print(l[1:7:2])
print(l[::])
print(l[-8:-1:1])
print(l[-1:-6:-1])

num=[10,20,30]
 # append is take only one argument and the append insert at last
num.append(65)
#insert we can insert at perticuler position
num.insert(1,40)
#the extend will take multiple argument
num.extend([70,"hi"])
print(num)
print(num.pop(3))
print(num)
print(num.index(70))
print(num.count(10))
n=[10,45,30,40,15,2,8,2,45,20]
n.sort()
print(n)
n.sort(reverse=True)
print(n)

n1=[10,20,50,60]
b=n1
b[1]=45
#we change in b it also change in
#  n1 also so we need use the copy of the n1 creating copy is called shallow copy
#both b and n1 is pointing to the same object so if anyone is change it apper another
print(b)
print(n1)
#shallow copy it change only in a not in n1
a=n1.copy()
a[2]=78
print("the a is",a)
print("the n1 is",n1)

# tuple =heterogenous valve ,ordered,duplicate,immutable tuple can't be change those are immutable
t=(10,20,30,"hello",True,60)
print(t)
print(type(t))
print(len(t))
print(t[3])
print(t.index("hello"))
# it is unpacking a=10 b=20 c=30 number of varible should be
#  same in number of valve in tuple
t1=(10,20,30)
a,b,c =t1
print(t1)
print(a)
print(c)

#membership operator

t2=(10,20,30)
print(10 in t2)
print(10 not in t2)
print(50 in t2)
print(10 not in t2)



sum=0
list1=[1,-1,4,6,7,8,-2,-5]
print("positive no")
for i in range(len(list1)):
    if(list1[i]>=0):
       
        print(list1[i])
        

print("negetive no")  
for i in range(len(list1)):
    if(list1[i]<0):
       
        print(list1[i])
 # mean of all the number       
list2=[10,20,30]
sum=0
for i in range(len(list2)):
    sum+=list2[i]
print(sum/len(list2))

#greater number

list3=[10,5,100,45]
large=list3[0]
index=0
for i in range(len(list3)):
    if(large<list3[i]):
        large=list3[i]
        index=i
    else:
        pass
print(large,index)

#second largest

list4=[10,5000,200,50,1000]
lar=0
sec=0
for i in range(len(list4)):
    if(lar<list4[i]):
        sec=lar
        lar=list4[i]
    elif(lar>list4[i] ):
        if(sec<list4[i]):
            sec=list4[i]  
        
print(sec)

# check the list is sort or not

list5=[9,10,3,4,2,1]
l=0
l1=list5[0]
count=0
count1=0
for i in range(len(list5)):
    if(list5[i]>l):
        count+=1
        l=list5[i]
       
    if(list5[i]<=l1):
       count1+=1
       l1=list5[i]
     
if(count==len(list5)):
      print("list is sort")
elif(count1==len(list5)):
      print("list is sorted")
else:
      print("the list is not sortred")


# sets
#sets are mutable,unorder,heterogenous  no indexing is there due to no order

set={10,20,30,40,"pallavi"}
print(set)
print(len(set))
print(set.remove(30))
# remove will give the error when the element is not there in the set
#set.remove(300)
print(set)
set.add("hello")
print(set)
#add multiple use the update
set.update(["pall",58,55])
print(set)

#discard not giv ethe error when the element is not there in the set
set.discard("pallavi")
print(set)
set.discard(500)
# print methods
print(dir(set))
help(set)
set.pop()
print(set)
set.clear()
print(set)