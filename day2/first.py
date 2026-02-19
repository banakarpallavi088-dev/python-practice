age=int(input("enter the age of student"))
marks=int(input("enter the marks"))
attendence=int(input("enter the attendence"))
trainingfee=20000
discount=0
if(age>=18 and marks>=60 and attendence>=75):
    print("eligible for placement")
else:
    print("not eligible")

if(marks>=85):
        discount=0.3*trainingfee
       
elif(marks>=70):
        discount=0.1*trainingfee
       
        
else:
          discount=0
    
finalfee=(trainingfee-discount)
print(finalfee)

if(finalfee<=16000):
    print("special approval required")
else:
    print("not have any special requirement")

hostel=input("enter do you want  hostel y/n:")
if(hostel=="y"):
      finalfee+=50000
else:
     pass

weekend_class=input("do you want weekend class y/n:")
if(weekend_class=="y"): 
      finalfee+=2000
else:
      pass

print("the final fee is",finalfee)


