freq={}


n=input("enter a string ")

x=n.split()


for i in x:
	if i in freq:
		freq[i]+=1
	else:
		freq[i]=1


print(freq)



