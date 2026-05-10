# Create a Python program using functions to perform the following tasks:

# 1. Create a function show_menu() that prints:
#    1. Add Numbers
#    2. Greet User
#    3. Check Number Type

# 2. Create a function add_numbers(a, b) that:
#    - takes two numbers as parameters
#    - returns their sum

# 3. Create a function greet_user(name, greeting="Hello") that:
#    - uses a default parameter
#    - returns a greeting message using an f-string

# 4. Create a function check_number(num) that:
#    - returns "Positive" if number > 0
#    - returns "Negative" if number < 0
#    - returns "Zero" otherwise

# 5. Call all the functions in your program and print meaningful outputs.

# Example Output:
# 1. Add Numbers
# 2. Greet User
# 3. Check Number Type

# Sum: 15
# Hello, Ayaz!
# Positive

# Submission Instructions:
# - Use proper function definitions
# - Use parameters
# - Use return statements
# - Use at least one default parameter
# - Keep the code clean and readable

# Optional Challenge:
# Add one more function of your own choice, such as:
# - square_number(n)
# - is_even(n)
# - make_email(username, domain="gmail.com")



def show_menu():
    print("1. Add Numbers")
    print("2. Greet User")
    print("3. Check Number Type")
    
def add_numbers(a, b):
    return a+b

def greet_user(name, greeting = "Hey"):
    return f"{greeting}, {name}"

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
def is_even(n):
    return n % 2 == 0


## Calling Functions

# show menu
show_menu()

# adding numbers
sum_result = add_numbers(10, 5)
print("Sum:", sum_result)

# greeting user
greet = greet_user("Kritarth")
print(greet)

#check number
result = check_number(10)
print(result)

# optional function
even_check = is_even(4)
print("Is Even:", even_check)