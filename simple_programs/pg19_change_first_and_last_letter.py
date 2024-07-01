n=input("Enter the string ")
s=list(n)
len=len(n)
temp1,temp2=s[0],s[1]
s[0],s[1]=s[len-1],s[len-2]
s[len-1],s[len-2]=temp1,temp2
m=''.join(s)

print(m)

