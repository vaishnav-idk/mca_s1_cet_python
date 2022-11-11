num=int(input("enter the number "))
fac=1
print(num)
print
if num<0:
    print("number undefined")
elif num==0:
    print("the factorial is ",fac)
else:
    for i in range(1,num+1):
        fac=fac*i
print("Factorial is ",fac)
