#Write A Program to Check if a Number is Positive, Negative or 0

n=int(input("Enter any number:"))
if n>0:
    print("The given number is Positive!")
elif n<0:
    print("The given number is Negative!")
elif n==0:
    print("The given number is 0!")
else:
    print("The given number is neither Positive nor Negative nor 0!")