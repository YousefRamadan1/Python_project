# Linux User & Group Management Script

## 📌 Description

This project is a simple **Python-based Linux administration tool** that helps manage users and groups from the terminal.
It provides a menu-driven interface to perform common system administration tasks such as adding users, deleting users, listing users, and managing groups.

The script uses **Python and Linux system commands** to interact with the operating system.

---

## ⚙️ Features

* Add a new Linux user
* Delete an existing user
* Modify user information
* List all system users
* Create a new group
* List all groups
* Simple interactive menu

---

## 🖥️ Technologies Used

* Python 3
* Linux commands (`useradd`, `userdel`, `groupadd`)
* OS module in Python

---

## 📂 Project Structure

```
project.py      # Main Python script
README.md       # Project documentation
```

---

## ▶️ How to Run the Script

1. Clone the repository:

```
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project directory:

```
cd your-repository-name
```

3. Run the script:

```
python3 project.py
```

---

## 🧾 Menu Options

When the script runs, the following menu will appear:

```
1. Add User
2. Modify User
3. Delete User
4. List Users
5. Add Group
6. List Groups
0. Exit
```

Each option allows you to perform a specific **user or group management task**.

---

## ⚠️ Requirements

* Linux Operating System
* Python 3 installed
* Root or sudo privileges (for user and group management)

Example:

```
sudo python3 project.py
```

---

## 🔐 Important Note

This script uses system commands such as:

* `useradd`
* `userdel`
* `groupadd`

These commands require **sudo privileges**, so make sure you run the script with the appropriate permissions.

---

## 👨‍💻 Author

**Yousef Ramadan**

IT / Linux Learner
