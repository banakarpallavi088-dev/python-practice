# s="hello"
# for i in range(len(s)):
#     print(s[i])

    # for i in range(50,30,-1):
    #     print(i)

    #     for i in range(2,100,2):
    #         print(i)

    #     for i in range(5,100,5):
    #         print(i)

# for i in range(1,25,1):
#                 print(i)
#                 if(i==15):
#                     break
# for i in range(1,2,1):
#                         print(i)
#                         if(i==2):
#                                 continue

for i in range(1,25,2):
        if(i==15):
                print("break is applied")
                print(i)
                break
        print(i)       
else:
        print("break is not there")
