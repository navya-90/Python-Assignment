sentence=input("Enter a sentence:")
words = sentence.split()
num_words = len(words)
num_digits = sum(c.isdigit() for c in sentence)
num_uppercase = sum(c.isupper() for c in sentence)
num_lowercase = sum(c.islower() for c in sentence)
print("Number of words:", num_words)
print("Number of digits:", num_digits)
print("Number of uppercase letters:", num_uppercase)
print("Number of lowercase letters:", num_lowercase)