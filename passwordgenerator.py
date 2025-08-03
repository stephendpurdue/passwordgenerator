import random
import string

# Defining variables.

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Password criteria.
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Loop generating each part of the password & detects if it meets the minimum length.
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# User input and returns a boolean of True or False.
    
min_length = int(input("Enter the desired minimum length: "))
has_number = input("Would you like numbers (y/n)?").lower() == "y"
has_special = input("Would you like special characters (y/n)?").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is",pwd)

