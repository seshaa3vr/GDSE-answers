a = input("Enter a password: ")
has_lower = False
has_upper = False
has_digit = False
for char in a:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
if has_lower and has_upper and has_digit:
    print("Password is valid.")
else:
    print("Password must contain at least one lowercase letter, one uppercase letter, and one number.")
