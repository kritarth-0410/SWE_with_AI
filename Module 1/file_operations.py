# #  File Handling in Python - Working with files in python program.
# #  Operations - Write, Read, Append, Delete ....

# #  Use-Case : Student Management System
# #  Student details - name, email, password, phone number, address, attendance, marks ..... 

# file = open('students.txt', "mode")

# # modes - r (read), w (write), a (append), x (create)

# #  Read a file.
# file = open('students.txt', 'r')

# print(type(file))
# print(file.read())

# file.close()   #Good practice

# x = file.readline()
# print(x)

# y = file.readline()
# print(y)

# lines = file.readlines()
# print(lines)

# #  strip() function - removes extra spaces and newline characters.

# for line in file:
#     print(line.strip())

# #  Why closing a file is important while handling files ?
# #  Frees system resources, and prevents file corruption, and it avoids memory leaks.

# with open('studentss.txt', 'r') as file:
#     file_content = file.read()
#     print(file_content)

# #  Using with open(...) => Python automatically closes the file after the with block finishes.

# #  Writing to a file
# with open('students.txt', 'w') as file:
#     file.write('Kritarth\n')
#     file.write('Deepak\n')

# with open('students.txt', 'r') as file:
#     file_content = file.read()
#     print(file_content)

# with open('students.txt', 'a') as file:
#     file.write('Harshvardhan\n')

# print("====================")

# with open('students.txt', 'r') as file:
#     file_content = file.read()
#     print(file_content)

# #  Difference between 'w' mode and 'a' mode
# #  w mode - Deletes the old content and writes the new content.
# #  a mode - Keeps the old content and adds/appends the new content at the end of the file.

# #  Opening the file in write mode, creates the file if file doesn't exist.
# with open('names.txt', 'w') as file:
#     file.write('Kritarth\n')
#     file.write('Deepak\n')

# #  Checking if a file exists or not.
# import os

# if os.path.exists('students.txt'):
#     print("File exists")
# else:
#     print("File doesn't exist")

# #  File Path - Absolute & Relative path

# #  Absolute Path - \Users\Kritarth\Desktop\IIT Roorkee/students.txt

# with open('students.txt', 'r') as file:
#     print(file.read())

# import os

# print(os.getcwd())

# if not os.path.exists("sample"):
#     os.mkdir("sample")

# #  pathlib
# from pathlib import Path

# file_path = Path('sdkfjh.txt')

# if file_path.exists():
#     print("File exists")
# else:
#     print("File doesn't exist")

# #  We can Read or Write using pathlib library.

# file_path = Path('students.txt')

# file_path.write_text("Deepak\nKritarth\nHarold\n")

# with open(file_path, "a") as file:
#     file.write("Tripti\n")

# print(file_path.read_text())

# #  Working with JSON files

# #  JSON - JavaScript Object Notation
# #  Key-Value pair
# {
#      "name" : "Kritarth",
#      "College" : "Masai",
#      "marks" : 90,
#      "attendance" : 94.5,
#      "city" : "Delhi"
#  }

import json

student = {
     "name" : "Kritarth",
     "College" : "Masai",
     "marks" : 90,
     "attendance" : 94.5,
     "city" : "Delhi"
 }

with open('student.json', 'w') as file:
    json.dump(student, file)

with open('student.json', 'r') as file:
    file_content = json.load(file)

    print(file)

print(file_content["name"])
print(file_content["marks"])

#  FileNotFoundError - If we try to read when file doesn't exists
#  If we try to write if file doesn't exist - Creates a new file 
#  Always remember to close the file or use 'with open()'
#  use 'w' and 'a' carefully

#  Exception Handling 