#Write A Program to Find the Factorial of a Number

x=int(input("Enter the number:"))
fact=1
for i in range(1,x+1):
    fact*=i
print(fact,"is the factorial of",x)