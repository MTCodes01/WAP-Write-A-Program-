#Write A Program to Check Leap Year

y=int(input("Enter a year:"))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print(y,"is a Leap Year!")
        else:print(y,"is not a Leap Year!")
    else:print(y,"is a Leap Year!")
else:print(y,"is not a Leap Year!")