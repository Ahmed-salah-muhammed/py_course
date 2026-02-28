# Directory Structure
```
day01/
  day01.py
  Python Day01.pdf
  PythonGIS46.drawio.pdf
day02/
  day02.py
day03/
  modules/
    __init__.py
    Auth.py
    auto_id.txt
    valid.py
  app.py
  PythonLab03.pdf
  structure.txt
id.txt
users.json
```

# Files

## File: day01/day01.py
```python
'''   Time for practice   ''' '''  ahmed salah muhammed   '''


'''   Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string. '''

# word = input("Enter your string: ").lower()
# count = 0
# for char in word:
#   if char in "aeiou":
#     count = count + 1 
    
# print(count)
    

'''    Write a program that prints the number of times the string 'iti'occurs in anystring.    '''

# times_of_iti_Words= "iti iti iti adasdas iti".lower()

# print(times_of_iti_Words.count("iti"))

'''  Write a program that remove all vowels from the input word and generate a brief version of it.  '''


# word = input("Enter your string: ").lower()

# word2 = ""

# for v in word:
#   if v not in "aeoui":
#     word2 += v

# print(word2)

'''  Write a program that prints the locations of "i" character in any string you added.  '''

# word = input("Enter ur text here: ")

# word_Enum = enumerate(word)

# for index, char in word_Enum:
#   char.lower()
#   if char == "i":
#     print(index)



'''   Write a program that build a Mario pyramid like below:  '''

# mario_pyramid = input("Enter ur number here: ")

# if mario_pyramid.isdigit():
#   mario_pyramid = int(mario_pyramid)
#   count = 1
#   while count <= mario_pyramid:
#     white_spaces = " " * (mario_pyramid - count)
#     stars = "*" * count
#     print(f"{white_spaces}{stars}" )
#     count +=1









# ---------------- try with my self ------------------
# number = int(input("enter any number from 1 to 10: "))

# if number <=10 and number >=1 :
#   count = 1
#   while count <= 10:
#     result = number * count
#     print (f" {number} * {count} = {result}")
#     count+= 1
```

## File: day02/day02.py
```python
"""day02 ----> list - tuple - set - dictionary - function"""

#  Fill an array of 5 elements from the user, Sort it in descending
#  and ascending orders then display the output.

myl = []
count = 5
num = 1

while len(myl) < count:
    x = input(f"Enter element no-{num}:")
    myl.append(x)
    myl.sort()
    num += 1
print(f"sort ascending list = {myl}")
myl.sort(reverse=True)
# we can use  myl.reverse()
print(f"sort descending list = {myl}")


# --------------------------------------


# Write a program that generate a multiplication table from 1 to the
# number passed.

num = input("Enter the number: ")
myl = []

if num.isdigit():
    num = int(num)
    for count in range(1, num + 1):
        row = []
        for i in range(1, count + 1):
            row.append(count * i)
        myl.append(row)

print(myl)

# --------------------------------------

# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# # increased by one from start.


def myl(length, start):
    ls = []
    for i in range(start, start + length):
        ls.append(i)
    print(ls)


myl(2, 5)

# --------------------------------------

# write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"


def isFizzBuzz(num):
    if isinstance(num, int):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num
    else:
        return "Invalid Input bcs it must be integer"


print(isFizzBuzz(11))


# ----------------------------------------

# Write a function which has an input of a string from user then it
# will return the same string reversed.


def reverseWord(word):
    lst = list(word)
    lst.reverse()
    word = "".join(lst)
    return word


# -----or-----

# def reverseWord(word):
#     return word[::-1]


print(reverseWord("ahmed Salah"))

# ----------------------------------------

# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers).
# then proceed to ask him for his email and print all this data.
# (Bonus) check if it is a valid email or not.


name = input("Enter Your first Name: ")

if name.isalpha() and name:
    email = input("please Enter Your Email: ")
    if "@" in email and "." in email:
        if email.index("@") < email.index("."):
            print(f"Your Name is {name} and Your Email is {email}")
        else:
            print("please enter Valid email")
else:
    print("please enter Valid name")


# ----------------------------------------
# Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu

user_input = input("Enter the name: ")


def longestPart(text):
    max = text[0]
    temp = text[0]

    for index in range(1, len(text)):
        if text[index] <= text[index + 1]:
            temp += text[index]
        else:
            if len(temp) > len(max):
                max = temp
            temp_part = text[index]

    if len(temp_part) > len(max):
        max = temp

    return max


print(f"Longest substring is: {longestPart(user_input)}")

# ----------------------------------------

# Write a program which repeatedly reads numbers until the user
# enters “done”.
# ○ Once “done” is entered, print out the total, count, and
# average of the numbers.
# ○ If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.


total = 0
count = 0

while True:
    user_input = input("Enter the Number or done: ").lower()

    if user_input == "done":
        break

    if user_input.isdigit():
        num = int(user_input)
        total += num
        count += 1
    else:
        print("Error: please enter a valid number.")
        continue

    avg = total / count

print(f"The Total numbers = {total}, Count = {count}, Average = {avg}")

# ----------------------------------------
# ● Word guessing game (hangman)

words = ["python", "engineer", "planning", "gis", "developer"]

player = input("What is your name? ")
print(f"Hello {player} let's play!")

choice = int(input("Pick a number from 0 to 4 to choose a word: "))
secret = words[choice]

history = ""
tries = 7


while tries > 0:
    missing = 0

    for char in secret:
        if char in history:
            print(char, end=" ")
        else:
            print("_", end=" ")
            missing = missing + 1

    if missing == 0:
        print("\nYou won")
        break

    guess = input("\nGuess a letter: ").lower()
    history = history + guess

    if guess not in secret:
        tries -= 1
        print(f"Wrong Turns left:  {str(tries)}")

        if tries == 0:
            print(f"Game Over The word was: {secret}")
```

## File: day03/modules/__init__.py
```python
def display_user_data(f_name, l_name, email, phone):
    print("\n--- User data ---")
    print(f"Full Name : {f_name} {l_name}")
    print(f"Email     : {email}")
    print(f"Mobile    : {phone}")
    print("----------------------------")
```

## File: day03/modules/Auth.py
```python
import uuid
import json


def generateId():
    try:
        with open("id.txt", "r") as f:
            id = f.read()
            id = int(id)
            id += 1

        with open("id.txt", "w") as f:
            f.write(str(id))
    except Exception as e:
        return False, e

    return id


# if __name__ == "__main__":
#     print(generateId())
# users_db = []
# def register(first_name, last_name, email, password, phone):
#     user_data = {
#         "name": f"{first_name} {last_name}",
#         "email": email,
#         "password": password,
#         "phone": phone,
#     }
#     users_db.append(user_data)
#     return True


FILE_NAME = "users.json"


def load_users():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)


def register(first_name, last_name, email, password, mobile):
    users = load_users()

    for user in users:
        if user["email"] == email:
            print("Email already exists!")
            return False

    activation_code = str(uuid.uuid4())

    users.append(
        {
            "id": generateId(),
            "first_name": first_name,
            "last_name": last_name,
            "email": email.strip(),
            "password": password,
            "mobile": mobile,
            "is_active": False,
            "activation_code": activation_code,
        }
    )

    save_users(users)

    print("Your activation code:", activation_code)
    return True


# def login(email, password):
#     for user in users_db:
#         if user["email"] == email and user["password"] == password:
#             return True
#     return False


def login(email, password):
    users = load_users()

    for user in users:
        if user["email"] == email.strip():

            if not user["is_active"]:
                print("Account not activated!")
                return False

            if user["password"] == password:
                return True

            print("Wrong password!")
            return False

    print("User not found!")
    return False


def activate(email, code):
    users = load_users()

    for user in users:
        if user["email"] == email and user["activation_code"] == code:
            user["is_active"] = True
            save_users(users)
            print("Account activated successfully!")
            return True

    print("Invalid activation code")
    return False


if __name__ == "__main__":
    pass
```

## File: day03/modules/auto_id.txt
```
0
```

## File: day03/modules/valid.py
```python
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
    return "Invalid Email format! (ex: user@example.com)\n"


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
```

## File: day03/app.py
```python
from modules import valid, Auth, display_user_data

while True:
    print("\nplease choice your log:\n log in: l\n sign up: p\n quit: q")
    print("--------------")
    choice = input("Enter your choice: ").lower()

    if choice == "p":
        # First Name
        while True:
            first_name_input = input("enter your first name: ")
            result = valid.validName(first_name_input)
            if result is True:
                break
            print(result)

        # Last Name
        while True:
            last_name_input = input("enter your last name: ")
            result = valid.validName(last_name_input)
            if result is True:
                break
            print(result)

        # Email
        while True:
            email_input = input("enter your Email: ")
            result = valid.validEmail(email_input)
            if result is True:
                break
            print(result)

        # Password
        while True:
            password_input = input("enter your Password: ")
            password_result = valid.checkPassword(password_input)

            if password_result is True:
                confirm_p = input("confirm password: ")
                confirm_result = valid.confirmPassword(password_input, confirm_p)
                if confirm_result is True:
                    break
                else:
                    print("Passwords do not match!")
            else:
                print(password_result)

        # Mobile
        while True:
            mobile_input = input("enter your mobile phone: ")
            result = valid.validatePhone(mobile_input)
            if result is True:
                break
            print("Invalid Egyptian mobile number!")
        success = Auth.register(
            first_name_input, last_name_input, email_input, password_input, mobile_input
        )
        if success:
            code = input("Enter activation code: ")
            Auth.activate(email_input, code)
            display_user_data(
                first_name_input, last_name_input, email_input, mobile_input
            )
            print(f"Success! Account created for {first_name_input}")
        continue

    elif choice == "l":
        email = input("enter your Email: ")
        password = input("enter your Password: ")
        if Auth.login(email, password):
            print("log in successfully")
        else:
            print("Wrong email or password")
        break

    elif choice == "q":
        print("Goodbye")
        break

    else:
        print("Wrong choice, please enter l, p, or q.")
```

## File: day03/structure.txt
```
1- __init__
2- entry point 
3- authentication
4- validation
```

## File: id.txt
```
1
```

## File: users.json
```json
[
    {
        "id": 1,
        "first_name": "ahmed",
        "last_name": "salah",
        "email": "ahmed@gmail.com",
        "password": "A@213123123123123@@@@adsadasd",
        "mobile": "01225246488",
        "is_active": true,
        "activation_code": "498cbd79-f3b1-4212-9ab1-7c1ffe2709bc"
    }
]
```
