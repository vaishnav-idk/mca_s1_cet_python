a=input("Enter a List of Numbers : ")
a=a.split(" ")
b=[]
for i in a:
	b.append(int(i))
c=["Over" if x>100 else x for x in b]
print(c)

