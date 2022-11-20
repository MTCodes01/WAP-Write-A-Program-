#Write A Program to Print the Fibonacci sequence

n=int(input("How many terms:"))
a,b,count=0,1,0
while count<n:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count+=1