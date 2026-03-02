l=[5,1,3,9,4,8]
for i in l:
    print(i)
# item=int(input("enetr the element"))
# l.append(item)
# print(l)
# l.remove(10)# removel element
# print(l)
# l.pop()
# print(l)
# l.insert(0,20)
# print(l)
# l.pop(2)# index value
# print(l)
# print(l[:-5:-1]) reverseing the list using slicing method
# l1=l.copy()# it is shallow copy it not change in
print(l) 
start=0
end=len(l)-1
while start<=end:
     temp=l[start]
     l[start]=l[end]
     l[end]=temp
     start=start+1
     end=end-1
print(l)

min=l[0]
max=l[0]
for i in l:
     if(min>i):
          min=i
     elif(max<i):
          max=i

print(max)
print(min)

list=[1,4,5,6,7]
sum=list[0]
for i in range(1,len(list),1):
     sum+=list[i]
     list[i]=sum
print(list)
     
l1=[1,2,3,5]
pr=[0]*len(l1)
pr[0]=l1[0]
for i in range(1,len(l1),1):
     pr[i]=pr[i-1]+l1[i]
print(pr)


l2=[0,1,0,3,12]
j=0
for i in range(0,len(l2),1):
     if l2[i]!=0:
          temp=l2[i]
          l2[i]=l2[j]
          l2[j]=temp
          j=j+1
print(l2)
