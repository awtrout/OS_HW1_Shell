import os

def list_directory_contents():      #list directory contents
    try:
        os.system('dir')
    except Exception as e:
        print(f"Error executing 'dir' command: {e}")

def print_working_directory():      #cd print directory 
    try:
        os.system('cd')
    except Exception as e:
        print(f"Error executing 'cd' command: {e}")

def create_new_directory():     #mkdir make a new directory
    directory_name = input("Enter the name of the new directory: ")
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def display_message():      #echo display message from user input 
    message = input("Enter the message to display: ")
    try:
        os.system(f'echo {message}')
    except Exception as e:
        print(f"Error displaying message: {e}")

def concatenate_and_display_content():      #type 
    filename = input("Enter the name of the file: ")
    try:
        os.system(f'type {filename}')
    except Exception as e:
        print(f"Error displaying content of '{filename}': {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. List directory contents")
        print("2. Print working directory")
        print("3. Create a new directory")
        print("4. Display a message")
        print("5. Concatenate and display content of a file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_directory_contents()
        elif choice == '2':
            print_working_directory()
        elif choice == '3':
            create_new_directory()
        elif choice == '4':
            display_message()
        elif choice == '5':
            concatenate_and_display_content()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
