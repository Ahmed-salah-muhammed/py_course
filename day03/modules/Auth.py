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
            print("Email already exists")
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
                print("Account not activated")
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


# if __name__ == "__main__":
#     pass
