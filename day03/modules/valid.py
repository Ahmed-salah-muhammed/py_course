import re


def validName(e):
    name = e.strip()
    if name.isalpha() and name:
        return True
    return "Invalid name! Please enter letters only and do not leave it empty.\n"


def validEmail(e):
    pattern = r"^[a-zA-Z0-9]([\w\.-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([\w\.-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,6}$"
    if re.match(pattern, e.strip()):
        return True
    return "Invalid Email format! (e.g., user@example.com)\n"


def confirmPassword(p1, p2):
    if p1 == p2:
        return True
    return "Passwords do not match!\n"


def checkPassword(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if re.match(pattern, password):
        return True
    return "Weak password! Must contain: 8+ chars, Uppercase, Lowercase, Number, and Symbol.\n"


def validatePhone(phone):
    pattern = r"^01[0125][0-9]{8}$"
    if re.match(pattern, phone.strip()):
        return True
    return "Invalid Egyptian phone number! (Must start with 010, 011, 012, or 015 and be 11 digits).\n"
