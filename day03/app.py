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
        display_user_data(first_name_input, last_name_input, email_input, mobile_input)
        if success:
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
