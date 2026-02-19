
# n=15
# while(n<50):
#     if(n == 25):
#         break
#     print(n)
#     n=n+5

# a=5
# b=3
# print(a & b)
# print(a | b)
# print(a << b)
# print(a >> b)

# digit=0
# num=0
# n=int(input("enter the number"))
# while(n>0):

#     digit=n%10
   
#     num=(num*10)+digit
#     n=int(n/10)


# print(num)   

# import random
# num=random.randint(1,100)
# attempts=0
# print("guess number in blw the 1 to 100")

# while True:
#     guess=int(input("enter your guess:"))
#     attempts+=1
#     if guess>num:
#         print("Too high")
#     elif guess<num:
#         print("Too low")
#     else:
#         print("correct! you guessed it in")


def hello():
    print("hello everyone")
hello()

def add(a,b,c):
    print(f"the add of two number={a+b+c}")
add(1,2,3)
add(4,4,4)
hello()
#keyworld argument
def student(name,age):
    print(f"name:{name} and age:{age}")
student(age=19,name="pallavi")

def add(name,age=21):
    print(f"the name is{name} and age{age}")
add("pallavi")
add("pallavi",19)
add(age=20,name="pallavi")

def valve(a):
    return a
print ("the valve is",valve(8))
#escape sequence
str="iit's my pen"
print(str)
# string function

print(len(str))
print(str.upper())
print(str.lower())
# only first letter will be capital
print(str.capitalize())
print(str.find("my pen"))
print(str.find("is"))
print(str.index("my"))
#index  give the error but the find 
# didnot give the error it give -1
# print(str.index("is"))
print(str.count("i"))
print(str.replace("pen","book"))
st="  hello i am pallavi   "
# it remove the edge space rstrip remove the right 
# side edge space only strip remove all the space

print(st.rstrip())
print(st.lstrip())

st1="apple,mango,banana"
print(st1.split(','))

print(st1.split("\t"))
#slicing method name[start,stop,step] stop=stop-1=5 
# the 1 to 5 index valve is return
name="pallavi"
print(name[1:6:1])
# it from the righthaand side so it start from -1 like 
# hello world d=-1 l=-2 r=-3 0=-4 w=-5  space=-6 it start from -6 end at -2
text="hello world"
print(text[-6:-1])
# it will reverse the string
print(text[:-12:-1])

text1="pallavi"
print(text1.isalnum())
print(text1.isdigit())
print(text1.isalnum())
print(text1.islower())
print(text1.isupper())

text2="paa1123#@%67"
dcount=0
scount=0
alcount=0

for i in text2:
    if(i.isdigit()):
         dcount=dcount+1
        
    elif(i.isalpha()):
        alcount=alcount+1
       
    else:
         scount=scount+1
        
print("the num of digit",dcount)
print("the alpha",alcount)
print("the scount",scount)


