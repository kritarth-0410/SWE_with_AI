# Problem Statement

# Imagine you are building a security system for a phone. The user gets 3 attempts to enter the correct password.

# Loop Requirement: Use a for loop to allow the user a maximum of 3 attempts.

# The Correct Password: Set a variable correct_password = "Python123".

# Inputs: In each attempt, ask the user to input a password.

# Logic:

# If the password is correct: Display "Access Granted!" and use the break statement to stop the loop immediately (because they are already inside).
# If the password is "Skip": Use the continue statement to skip the current attempt and move to the next one without displaying an error.
# If the password is wrong: Display "Wrong Password. Try again."
# Final Step: After the loop ends, print "System Locked" (this represents the end of the session).

attempt = 0
correct_password = "Python123"
max_attempts = 3

for attempt in range(1,max_attempts + 1):
    password = input("Enter your password: ")

    if password == "Skip":
        continue

    if password == correct_password:
        print("Access Granted!")
        break
    else:
        if attempt < max_attempts:
            print("Wrong Password. Try again.: ")

if password != correct_password:
    print("System Locked")
    