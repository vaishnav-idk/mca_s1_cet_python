a=input("Enter A String : ")
b=""
for i in a:
    if i==a[0] and i not in b:
        b=b+i
    elif i==a[0] and i in b:
        b=b+"$"
    else:
        b=b+i
print(b)
