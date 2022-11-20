# Write A Program to Solve Quadratic Equation

print("ax^2 + bx + c")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

print("The roots are:")
print("x=",(-b+(b**2-4*a*c)**0.5)/2*a)
print("x=",(-b-(b**2-4*a*c)**0.5)/2*a)