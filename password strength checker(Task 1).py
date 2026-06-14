"""This is a python program which checks the strength of a user's password."""
print("Welcome to the password strength checker")
print("Password must be at least 8 characters long and it should contain uppercase letters, lowercase letters, digits and special characters")
password = input("Please enter your password: ")
if len(password) < 8 or password.islower() or password.isupper() or password.isdigit():
    print("Weak Password")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_digit = True
        if not i.isalnum():
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    else:
        print("Medium Password")
