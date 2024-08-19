num= input("Enter a number: ")
if num == num[::-1]:
    print(num," is a palindrome.")
else:
    print(num," is not a palindrome.")

digit_count = {}
for digit in num:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1

for digit, count in digit_count.items():
    print(digit," appears ",count," times") 