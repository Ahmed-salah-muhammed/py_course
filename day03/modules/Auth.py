users_db = []


def register(first_name, last_name, email, password, phone):
    user_data = {
        "name": f"{first_name} {last_name}",
        "email": email,
        "password": password,
        "phone": phone,
    }
    users_db.append(user_data)
    return True


def login(email, password):
    for user in users_db:
        if user["email"] == email and user["password"] == password:
            return True
    return False
