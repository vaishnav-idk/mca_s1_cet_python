dic1={}
n=int(input("No of items in 1st Dictionary : "))
for i in range(n):
	key=input("Enter Key : ")
	value=input("Enter Value : ")
	dic1[key]=value
dic2={}
m=int(input("No of items in 2nd Dictionary : "))
for i in range(m):
	key=input("Enter Key : ")
	value=input("Enter Value : ")
	dic2[key]=value

print(dic1)
print(dic2)

dic3={**dic1,**dic2} #creates a new dic by merging prev 2

for i,j in dic3.items():
	if i in dic1 and i in dic2:
		dic3[i]=[dic1[i],j]

#dic1.update(dic2) #updates dic1 - destructive

print("After Merging Dic1 with Dic2")
print(dic3)
