import json
from datetime import datetime
from modules.Auth import generateId
from tabulate import tabulate

FILE_NAME = "users_project.json"


def load_projects():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        return []


def save_projects(projects):
    with open(FILE_NAME, "w") as file:
        json.dump(projects, file, indent=4)


def create_project(owner_email, title, details, target, start_date, end_date):

    try:
        s_d = datetime.strptime(start_date, "%y-%m-%d")
        e_d = datetime.strptime(end_date, "%y-%m-%d")
        if e_d <= s_d:
            return False, "End date must be after start date"
    except ValueError:
        return False, "Invalid date you must Use YYYY-MM-DD"

    projects = load_projects()
    new_project = {
        "id": generateId(),
        "owner_email": owner_email,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
    }

    projects.append(new_project)
    save_projects(projects)
    return True, "Project created successfully"


def view_projects():
    projects = load_projects()
    if not projects:
        print("\nNo projects found.")
        return

    table_data = []
    for p in projects:
        table_data.append(
            [
                p["id"],
                p["title"],
                f"{p['target']} EGP",
                p["start_date"],
                p["end_date"],
                p["owner_email"],
            ]
        )

    headers = ["ID", "Title", "Target", "Start Date", "End Date", "Owner"]

    print("\n" + tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def edit_project(project_id, user_email):
    projects = load_projects()
    project_found = False

    for p in projects:
        if str(p["id"]) == str(project_id):
            if p["owner_email"] != user_email:
                return (
                    False,
                    "You can only edit your own projects.",
                )

            project_found = True
            print(f"\n--- Editing Project: {p['title']} ---")

            new_title = input(f"New Title [{p['title']}]: ") or p["title"]
            new_details = input(f"New Details [{p['details']}]: ") or p["details"]
            new_target = input(f"New Target [{p['target']}]: ") or p["target"]
            new_start = (
                input(f"New Start Date [{p['start_date']}]: ") or p["start_date"]
            )
            new_end = input(f"New End Date [{p['end_date']}]: ") or p["end_date"]

            try:
                s_d = datetime.strptime(new_start, "%Y-%m-%d")
                e_d = datetime.strptime(new_end, "%Y-%m-%d")
                if e_d <= s_d:
                    return False, "Error: End date must be after start date"
            except ValueError:
                return False, "Error: Invalid date format"

            p["title"] = new_title
            p["details"] = new_details
            p["target"] = new_target
            p["start_date"] = new_start
            p["end_date"] = new_end
            break

    if not project_found:
        return False, "Project ID not found."

    save_projects(projects)
    return True, "Project updated successfully"


def delete_project(project_id, user_email):
    projects = load_projects()
    for p in projects:
        if str(p["id"]) == str(project_id):
            if p["owner_email"] == user_email:
                projects.remove(p)
                save_projects(projects)
                return True, "Project deleted successfully."
            else:
                return (
                    False,
                    "You can only delete your own projects.",
                )

    return False, "Project ID not found"


def search_by_date(date_str):
    try:
        search_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format"

    projects = load_projects()
    results = []

    for p in projects:
        s_date = datetime.strptime(p["start_date"], "%Y-%m-%d")
        e_date = datetime.strptime(p["end_date"], "%Y-%m-%d")

        if s_date <= search_date <= e_date:
            results.append(p)

    return results
