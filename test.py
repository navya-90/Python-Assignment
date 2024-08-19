a=float(input("Enter marks of test1:"))
b=float(input("Enter marks of test2:"))
c=float(input("Enter marks of test3:"))
avg1=(a + b)/2
avg2=(b + c)/2
avg3=(c + a)/2
best=max(avg1,avg2,avg3)
print("Average of best two test marks out of three test’s marks is ",best)