a=input("Enter A List of Firstnames : ")
a=a.split(" ")
b=[x for x in a if "a" in x]
print("No of Firstnames containing The letter A is : ",len(b))
