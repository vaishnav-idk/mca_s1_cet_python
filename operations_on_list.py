from email.policy import default
from tkinter import N


len_1=int(input("enter the length of the first list: "))
len_2=int(input("enter the length of the 2nd list:"))
l1=[]
l2=[]


for i in range(1,len_1+1):
    l1.append(input("enter the "+str(i)+"element of the list : "))

for j in range(1,len_2+1):
    l2.append(input("enter the "+str(j)+"element of the 2nd list"))

flag=1

while flag:
    op=int(input("""select operation: 

    1.Check whether 2 list are same length \n 
    2.Check whether 2 list of the same value \n 
    3.Check whether any values occurs in both list \n """))

    match op:
        case 1:
            if l1==l2:
                print("Both list of same length")
            else:
                print("They are not of the same length")
        case 2:
            l1.sort()
            l2.sort()
            if l1==l2:
                print("the list are identical")
            else:
                print("they are not identical")
        case 3:
            a,b=set(l1),set(l2)
            if(a&b):
                print("There are commen elements between ")
            else:
                print("No commen member between them")
    flag=int(input("Do you want to continue enter 1 for yes and 0 for no"))
    if flag>1:
        flag=0
