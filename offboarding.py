import json
from security import log_action

def offboard_user(name):
    with open("users.json", "r") as f:
        data = json.load(f)

    for user in data["employees"]:
        if user["name"] == name and user["status"] == "active":
            user["status"] = "disabled"
            log_action(f"Offboarded user: {name}")
            print(f"User {name} has been disabled.")
            break

    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)

