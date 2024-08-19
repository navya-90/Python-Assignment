str=input("Enter any string:")
n=len(str)
cnt=0
for i in range(int(n/2)):
    if(str[i]==str[n-i-1]):
        cnt+=1
        continue
    else:
        print(str," is not a palindrome")
if(cnt==int(n/2)):
    print(str,"is a palindrome")