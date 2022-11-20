#Write A Program to Print all Prime Numbers in an Interval

s=int(input("Enter Start of the Interval:"))
e=int(input("Enter End of the Interval:"))
for i in range(s,e+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)