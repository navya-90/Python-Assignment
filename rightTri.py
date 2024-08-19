a=int(input("Enter length of first side:"))
b=int(input("Enter length of second side:"))
c=int(input("Enter length of third side:"))
if a**2 + b**2 == c**2 :
    print("Given triangle is right triangle.")
elif b**2 + c**2 == a**2 :
    print("Given triangle is right triangle.")
elif c**2 + a**2 == b**2 :
    print("Given trianle is right triangle.")
else :
    print("Give triangle is not a right triangle.")