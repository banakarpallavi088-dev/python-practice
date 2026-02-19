import random
choices=('rock','paper','scissor')
user_choice=input("enter your choice as per the give choice")
system_choice=random.choice(choices)
print(system_choice)
print(user_choice)

if(user_choice==system_choice):
    print("tie")


elif(user_choice=='rock'):
        if(system_choice=='paper'):
             print("paper win over the rock")
       
        elif(system_choice=='scissor'):
            print("rock win over the scissor")

elif(user_choice=='paper'):
        if(system_choice=='rock'):
            print("paper win paper will cover the rock")
        elif(system_choice=='scissor'):
            print("scissor win cut the paper")

elif(user_choice=='scissor'):
        if(system_choice=='paper'):
            print("scissor win it cut the paper")
        elif(system_choice=='rock'):
            print("rock win smash the scissor")
else:
     print("invalid choice")


     #coverting the list to tuple using bulit in fuction
list=[10,20,30]
t=tuple(list)
print(t)
 #coverting the list to tuple without using bulit in fuction
list=[10,20,30]
tu=(*list,)
print(tu)