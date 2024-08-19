str=input("Enter a string containing a-z,A-Z,0-9,_ or combination of all:")
if str[0].isdigit():
    print(str,"is not a valid identifier")
else:
    print(str,"is a valid identifier")