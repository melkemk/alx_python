def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False

    for char in password:
        if char.isspace():
            has_space = True
        elif char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    return not has_space and has_uppercase and has_lowercase and has_digit



# print(validate_password("Password123"))
# print(validate_password("abc123"))
# print(validate_password("Password 123"))
# print(validate_password("password123"))