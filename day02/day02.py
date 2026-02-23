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
