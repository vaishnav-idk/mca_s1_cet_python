from re import A


a=int(input("enter the first integer "))
b=int(input("enter the 2nd integer "))


def gcf_2_nums(a,b):
    if (b==0):
        return a 
    else:
        return gcf_2_nums(b,a%b)

c=gcf_2_nums(a,b)
print(c,"is the gcd of the numbers")