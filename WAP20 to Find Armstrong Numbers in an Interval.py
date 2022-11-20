#Write A Program to Find Armstrong Numbers in an Interval
st=int(input("Enter Start of the Interval:"))
en=int(input("Enter End of the Interval:"))
for i in range(st,en+1):
    sum=0
    s=str(i)
    for j in range(len(s)):
        sum+=int(s[j])**len(s)
    if sum==i:
        print(i)