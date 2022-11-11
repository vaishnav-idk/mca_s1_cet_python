v=['a','e','i','o','u']

n=input("Enter a word ")

ans=[ans for ans in n if ans in v]

print(ans)

if len(ans)==0:
	print("The words has no vowels")




