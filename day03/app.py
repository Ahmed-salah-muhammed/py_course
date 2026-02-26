from modules import valid, Auth, display_user_data, projects
from tabulate import tabulate

while True:
    print("\nplease choice your log:\n log in: l\n sign up: p\n quit: q")
    print("------------------------")
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
                    print("Passwords do not match")
            else:
                print(password_result)

        # Mobile
        while True:
            mobile_input = input("enter your mobile phone: ")
            result = valid.validatePhone(mobile_input)
            if result is True:
                break
            print("Invalid Egyptian mobile number")
        success = Auth.register(
            first_name_input, last_name_input, email_input, password_input, mobile_input
        )
        if success:
            code = input("Enter activation code: ")
            Auth.activate(email_input, code)
            display_user_data(
                first_name_input, last_name_input, email_input, mobile_input
            )
            print(f"Account has been created for {first_name_input}")
        continue

    elif choice == "l":
        email = input("enter your Email: ")
        password = input("enter your Password: ")
        if Auth.login(email, password):
            print(f" Welcome back, {email}")

            while True:
                print("\n--- Project Management Menu ---")
                print("1- Create Project")
                print("2- View All Projects")
                print("3- Edit My Project")
                print("4- Delete My Project")
                print("5- Search Projects by Date")
                print("6- Log-out")

                choice = input("Select an option: ")

                if choice == "1":
                    while True:
                        title = input("Project Title: ")
                        details = input("Details: ")
                        target = input("Total Target (EGP): ")
                        start_date = input("Start Date (YYYY-MM-DD): ")
                        end_date = input("End Date (YYYY-MM-DD): ")

                        success, message = projects.create_project(
                            email, title, details, target, start_date, end_date
                        )
                        print(message)
                        if success:
                            break

                elif choice == "2":
                    projects.view_projects()

                elif choice == "3":
                    projects.view_projects()
                    p_id = input("Enter Project ID to edit: ")
                    success, message = projects.edit_project(p_id, email)
                    print(message)

                elif choice == "4":
                    projects.view_projects()
                    p_id = input("Enter Project ID to delete: ")
                    success, message = projects.delete_project(p_id, email)
                    print(message)

                elif choice == "5":
                    date_to_search = input("Enter date (YYYY-MM-DD): ")
                    results = projects.search_by_date(date_to_search)

                    if isinstance(results, list) and results:
                        table_data = [
                            [p["id"], p["title"], p["target"], p["end_date"]]
                            for p in results
                        ]
                        headers = ["ID", "Title", "Target", "End Date"]
                        print(tabulate(table_data, headers=headers, tablefmt="presto"))
                    elif not results:
                        print("No active projects found.")
                    else:
                        print(results)

                elif choice == "6":
                    print("Logging out...")
                    break
    elif choice == "q":
        print("Goodbye...")
        break

    else:
        print("Wrong choice, please enter l, p, or q")
