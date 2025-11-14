import random
import string
def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print(" Welcome to the Python Password Generator! ")
try:
    length = int(input("Enter the desired password length (e.g. 8, 12, 16): "))
    if length <= 0:
        print("Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
password = generate_password(length, use_upper, use_digits, use_symbols)
print("\n Your secure password is:")
print(password)

