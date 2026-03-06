#!/usr/bin/env python3
import os

def add_user():
    username = input("Enter the user name: ")
    os.system(f"sudo useradd {username}")
    print(f"user hasbeen added {username}")

def modify_user():
    username = input("Enter the User name you want to modify: ")
    print("Here you can modify user")

def delete_user():
    username = input("Enter the user name you want to delete: ")
    os.system(f"sudo userdel {username}")
    print(f"user hasbeen deleted{username}")

def list_users():
    os.system("cut -d: -f1 /etc/passwd")

def add_group():
    groupname = input("Enter The new group name: ")
    os.system(f"sudo groupadd {groupname}")
    print(f"Group has been added {groupname}")

def list_groups():
    os.system("cut -d: -f1 /etc/group")

def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Add User")
        print("2. Modify User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Add Group")
        print("6. List Groups")
        print("0. Exit")

        choice = input("اختر رقم: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            modify_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            list_users()
        elif choice == "5":
            add_group()
        elif choice == "6":
            list_groups()
        elif choice == "0":
            print("Exit...")
            break
        else:
            print("Wrong Choice!")

if __name__ == "__main__":
    main_menu()


