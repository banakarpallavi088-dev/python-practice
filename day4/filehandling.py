file=open("day4/filetext.txt","w")
# print(file.read(27))
# file.close()
# for i in range(1,11):
#     print(file.readline())
file.write("Dream is not what we see after sleeping")
file.close()

file=open("day4/filetext.txt","a")
file.write(" \n hello i am pallavi")
file.close()

file=open("day4/filetext.txt","r")
for i in range(1,3):
    print(file.readline())

file.close()
# write mood if file not there it create file and write in that file if the file is there it is overwrite on the  file
# in append mood the if file exit it not overwrite on it
import csv
with open("abc.csv","w") as f:
    x=csv.writer(f)
    for i in range(1,4):
      sr=int(input("enter the serial number"))
      data=input("enter the name")
      x.writerow([sr,data])
    f.close()


f=open("abc.csv","r")
x=csv.reader(f)
for i in x:
   print(i)
f.close()

# pickle
import pickle # inbulti modules
file=open("xyz.dat","wb")
dic={}
# pickle.dump({"name":"pallavi","age":20,"course":"cse"},file)
for i in range(1,5):
   key=input("enter name")
   course=input("enter the course")
   dic[key]=course
pickle.dump(dic,file)
file.close()


file=open("xyz.dat","rb")
dic=pickle.load(file)
print(dic)
file.close()