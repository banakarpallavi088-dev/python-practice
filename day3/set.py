s1={1,2,3}
s2={5,6,7}
print(s1.issuperset(s2))#all the element of s2 is ther in the s1
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))# no commen element are there
print(s2.issubset(s1))

#dictionary

#mutable
#heterogenous
#ordered
#duplicate(values() keys cannot be duplicate
#dictionary
student={
    "name":"pallavi",
    "age":20,
    "branch":"cse"
}
print(student)
print(type(student))
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student["branch"])
print(student.get("marks"))# the key not thre in th dic it give none
#print(student["marks"]) if not there key it give keyerror
# if the key thre in the set the value is update if not the add the key to the set
student["name"]="sita"
print(student)
student["marks"]=90
print(student)
student.update({"age":19})
print(student)
student.update({"fees":15000})
print(student)
student.pop("marks")
print(student)
student.popitem()
print(student)

for i in student:
    print(i,student[i])

for i in student.values():
    print(i)

for i in student.items():
    print(i)
s5={1,2,3,4}
s=set()
print(type(s))
for i in s5:
    print(i)

s1={
    "name":"pallavi",
    "age":20
}
s2={
    "name1":"deeepu",
    "age1":17
}
#print(s1|s2)
for i in s2:
    s1[i]=s2[i]
print(s1)
# sum of the values
s3={"a":1,"b":2,"c":3}
sum=0
for i in  s3.values():
    sum+=i
print(sum)

#freaquency of the element
l=[1,2,3,4,1,2,3,5,6,3,1,3,4]
dic={}

for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
   
d1={1:2,2:2,3:3,4:4}
d2={5:5,6:6,7:7}
for i in d1.values():
   print(i)
   



