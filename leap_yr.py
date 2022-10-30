n=int(input("enter the start year "))
m=int(input("enter the end year "))
l=[]

if m>n:
    for i in range(n,m+1):
        if(i%4==0):
            l.append(i)
else:
    print("check for your input ")

if len(l)!=0:
    print(l)
