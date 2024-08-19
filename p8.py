def swap_first_two_chars(s1, s2):
    if len(s1) < 2 or len(s2) < 2:
        return "Both strings must have at least two characters."
    
    swapped_s1 = s2[:2] + s1[2:]
    swapped_s2 = s1[:2] + s2[2:]
    
    return swapped_s1  +' '+ swapped_s2

str = input("Enter two strings separated by a space: ")
strings = str.split()

if len(strings) != 2:
    print("Please enter exactly two strings separated by a space.")
else:
    result = swap_first_two_chars(strings[0], strings[1])
    print(result)
