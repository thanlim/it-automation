from onboarding import onboard_user
from offboarding import offboard_user

def menu():
    print("\n1. Onboard User")
    print("2. Offboard User")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        name = input("Enter name: ")
        role = input("Enter role: ")
        onboard_user(name, role)

    elif choice == "2":
        name = input("Enter name: ")
        offboard_user(name)

    elif choice == "3":
        exit()

while True:
    menu()

