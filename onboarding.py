import json
from security import generate_password, hash_password, log_action

def onboard_user(name, role):
    with open("users.json", "r") as f:
        data = json.load(f)

    password = generate_password()
    hashed_pw = hash_password(password)

    user = {
        "name": name,
        "role": role,
        "password_hash": hashed_pw,
        "status": "active"
    }

    data["employees"].append(user)

    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)

    log_action(f"Onboarded user: {name} with role: {role}")

    print(f"User {name} created successfully.")
    print(f"Temporary password: {password}")

