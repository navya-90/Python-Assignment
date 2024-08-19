temp=float(input("Enter temperature:"))
if temp>=273 and temp<=373 :
    temp=( 5 * (temp -32)) / 9
    print("Temperature in degree celcius is:",temp)
else :
    temp=( 9 * temp / 5 ) + 32
    print("Temperature in farenhiet is:",temp)