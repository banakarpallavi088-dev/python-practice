# for i in range(1,4,1):
#     print("hello world",i)
# s="hello world"
# for i in range(len(s)):
#     print(s[i],i)


# for i in range(1,n,1):
#     print(i)

# for i  in range(10,1,-1):
#     print(i)

# n=4
# for i in range(1,50,1):
#         print(f"{n} * {i}= {n*i}")
# sum=0

# for i in range(1,5,1):
#     sum+=i
# print(sum)

# mul=1
# for i in range(1,5,1):
#   mul*=i
# print(mul)


# eve=0
# od=0
# for i in range(1,5,1):
#         if(i%2==0):
#                 eve+=i
#         else:
#                 od+=i
# print("even sum=",eve)
# print("odd sum=",od)

num=500
# for i in range(1,int(num/2),1): factos of number
#     if(num%i==0):
#         print(i)
# print(int(num/2),"\n",num)


# n=int(input("enter the number"))
# mul=0
# for i in range(1,n,1):
 
   
#    if(n%i==0):
#      mul+=i

# if(mul==n):
#       print("it is perfect number")
# else:
#        print("not perfact")

# n=int(input("enter the number"))
# count=0
# for i in range(1,n+1,1):
#     if(n%i==0):
#         count=count+1

# if(count==2):
#     print("prime number")
# else:
#     print("not prime")


# s="hello"
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

#     if(i==3):
#         print(s[i])


s="pallavi"
rev="" 
for i in range(len(s)-1,-1,-1):
     rev=rev+s[i]
print(rev)

if(rev.lower() == s.lower()):
     print("is palindrome")
else:
     print("not palindrome")