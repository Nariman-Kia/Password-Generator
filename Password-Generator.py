import random
import sys

# Define the character lists
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
special_characters = list('!@#$%^&*()-_+=<>?')

# Initialize the list to store selected characters
Mylist1 = []

# Get user input for password preferences
password_length = int(input("Enter the length of the password: "))
password_lowercase_letters = input("Do you want your password to include lowercase letters? (Y/N): ").strip().upper()
password_uppercase_letters = input("Do you want your password to include uppercase letters? (Y/N): ").strip().upper()
password_digits = input("Do you want your password to include digits? (Y/N): ").strip().upper()
password_special_characters = input("Do you want your password to include special characters? (Y/N): ").strip().upper()

# Add selected character types to the list
if password_lowercase_letters == "Y" or password_lowercase_letters == "YES":
    Mylist1 += lowercase_letters

if password_uppercase_letters == "Y" or password_uppercase_letters == "YES":
    Mylist1 += uppercase_letters

if password_digits == "Y" or password_digits == "YES":
    Mylist1 += digits

if password_special_characters == "Y" or password_special_characters == "YES":
    Mylist1 += special_characters

# Check if Mylist1 has any characters before generating a password
if Mylist1:
    password = ''.join(random.choices(Mylist1, k=password_length))
    print(f"Generated password: {password}")
else:
    print("You did not select any character types for your password. Exiting.")
    sys.exit()
