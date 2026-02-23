#comprehension means checking even or odd of many number using it we can determine in single line
l=[1,2,3,4,5,6,7,8,9,10]
result=["Even" if i%2==0 else "odd" for i in l]
print(result)
# res={i:i**2 for i in range(1,11)}
# print(res)

res1={i:i*i if i%2==0  else i for i in range(1,20)}
print(res1)
res2={i:i*i for i in range(1,21) if i%2==0}
print(res2)



