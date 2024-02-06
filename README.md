# OS_HW1_Shell

This is a python program utilizing shell or system functions ro execute various shell commands. A menu allows users to select a number assigned to a specific shell command for execution. 
This program repeats the process until the user chooses to exit. 

## Menu

### 1. List directory

Uses the shell command **dir** to list directory contents. Windows equivalent to **ls**

### 2. Print working directory

Uses the shell command **cd** to print directory. 

### 3. Create a new directory

Uses the shell command **mkdir** to create a new directory. User input is accepted for new directory name. 

### 4. Display a message

Uses the shell command **echo** to display a message. User input is accepted for the message contents. 

### 5. Concatenate and display content of a file

Uses the shell command **type** to concatenate and display content of files. User input is accepted for the target file. Windows equiavlent to **cat**

### 6. Exit

Terminates the program 

## Notes

Validation of user input and proper handling of potential security risks are critical when working with system functions (like 'os.system') that execute shell commands. With imporper validation,
command injection attacks are possible. 
