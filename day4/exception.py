# exception handling for resolving the problem or for use can easyly know the  problem
a=int(input("enter the number"))
try:
    print(10/a)
# except ZeroDivisionError:
#     print("sorry you cannot divide by a is",a)
except Exception as err:
    print("sorry there is an error as",err)


else:# if not exception it is run
     print("there is no error")

finally:# if excetion there or not if must be run
    print("inside the finally block")
print("program is executed")

#creating own error by using raise keyword
age=int(input("enter the age"))
try:
    if age<10 or age>18:
      raise ValueError("your must be blw the 10 and 18")
    else:
      print("welcome to club")

except Exception as e:
    print("an error occurred as",e)

# l=[13,12,11]
# print(l[5])

    
d={'a':1}
print(d['b'])