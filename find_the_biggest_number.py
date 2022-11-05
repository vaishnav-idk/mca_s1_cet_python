a=int(input("first number "))
b=int(input("2nd number "))
c=int(input("3rd number "))

if a > b and a > c:
    print(a,"is the largest number")
elif b > a and b > c:
    print(b,"is the largest number")
elif c > a and c > b:
    #print(a,b,c)
    print(c,"is the largest number")
else:
    print("3 numbers are equal")

    