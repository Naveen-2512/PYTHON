import os
import sys

def show_directory(path):
    print("\nContents of:", path)

    try:
        items = os.listdir(path)

        if not items:
            print("Directory is empty.")
        else:
            for item in items:
                full_path = os.path.join(path, item)

                if os.path.isdir(full_path):
                    print("[DIR] ", item)
                else:
                    print("[FILE]", item)

    except FileNotFoundError:
        print("Directory does not exist.")
    except PermissionError:
        print("Permission denied.")


def show_files_by_extension(path, extension):
    print("\nFiles with", extension, "extension:")

    try:
        files = os.listdir(path)

        found = False

        for file in files:
            full_path = os.path.join(path, file)

            if os.path.isfile(full_path) and file.endswith(extension):
                print(file)
                found = True

        if not found:
            print("No matching files found.")

    except FileNotFoundError:
        print("Directory does not exist.")


def create_workspace(path):
    folder_name = input("Enter workspace folder name: ")
    workspace = os.path.join(path, folder_name)

    try:
        os.makedirs(workspace, exist_ok=True)
        print("Workspace created:", workspace)
    except PermissionError:
        print("Permission denied.")


def create_log_file(path):
    file_name = input("Enter log file name: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    file_path = os.path.join(path, file_name)

    try:
        with open(file_path, "w") as file:
            file.write("Log file created successfully.\n")
            file.write("This file is created using Python.\n")

        print("Log file created:", file_path)

    except PermissionError:
        print("Permission denied.")


def read_log_file(path):
    file_name = input("Enter log file name: ")

    file_path = os.path.join(path, file_name)

    try:
        with open(file_path, "r") as file:
            print("\n--- Log File Content ---")
            print(file.read())

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")


def main():
    # Get directory from command-line argument
    if len(sys.argv) > 1:
        current_path = sys.argv[1]
    else:
        current_path = os.getcwd()

    print("Current Directory:", current_path)

    while True:
        print("\n===== FILE MANAGEMENT UTILITY =====")
        print("1. Show Directory Contents")
        print("2. List Files by Extension")
        print("3. Create Workspace Folder")
        print("4. Create Log File")
        print("5. Read Log File")
        print("6. Change Directory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_directory(current_path)

        elif choice == "2":
            extension = input("Enter extension (example: .py): ")
            show_files_by_extension(current_path, extension)

        elif choice == "3":
            create_workspace(current_path)

        elif choice == "4":
            create_log_file(current_path)

        elif choice == "5":
            read_log_file(current_path)

        elif choice == "6":
            new_path = input("Enter directory path: ")

            if os.path.isdir(new_path):
                current_path = new_path
                print("Directory changed successfully.")
            else:
                print("Invalid directory.")

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


main()