#Write A Program to Check Armstrong Number

num=int(input("Enter a number:"))
s=str(num)
sum=0
for i in range(len(s)):
    sum+=int(s[i])**len(s)
if num==sum:print("The given number is an Armstrong number!")
else:print("The given number is not an Armstrong number!")