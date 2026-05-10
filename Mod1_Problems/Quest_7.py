# Write a Python program that does all of the following:

# Take the user's first name and last name as input
# Create and print the full name using an f-string
# Convert the full name to uppercase and print it
# Store each character of the full name in a list using list()
# Print:
# First character
# Last character
# A slice of the first 4 characters
# Create a tuple containing:
# full name
# length of full name
# Iterate through the character list using a loop and print each character on a new line


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = (f"{first_name} {last_name}")
print("Full Name:", full_name)
print("Uppercase:", full_name.upper())
char_list = list(full_name)
print("Characters:", char_list)
print("First Character:", char_list[0])
print("last Character:", char_list[-1])
print("First Four Character:", char_list[:4])
name_tuple = (full_name, len(full_name))
print("Tuple:", name_tuple)
for i in char_list:
    print(i)