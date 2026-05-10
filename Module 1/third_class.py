
# Loops and Iterations in Python.

# While loops
# While loop keeps running till the time the condition is TRUE.
# while condition:
#     print("Hello")

# attempts = 0
# max_attempts = 5

# while attempts < max_attempts:
#     attempts += 1
#     print(f"Attempt number: {attempts}")

# print("Loop Completed")

# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# print("Loop Completed")

# While loop can also be used to take user input.
# age = int(input('PLease enter your age: '))

# # age > 0 and age <= 110
# while age < 0 or age > 110:
#     print("Invalid age, age must be between 0 to 110")
#     age = int(input('Please try again: '))

# print(f"Valid age: {age}")

# Example - Build a number guessing game.
# secret_number = 49
# guess = int(input("Please guess your number (1-100): "))

# while guess != secret_number:
#     if guess < secret_number:
#         print("please guess some higher number.")
#     else:
#         print("please guess some smaller number.")
#     guess = int(input("Please try again with a number (1-100): "))

# print("You have guessed the correct number.")

# Break Statement - Early termination. Exit loop before it's natural completion.

# attempts = 0
# max_attempts = 5
# correct_password = "masai"
# password = input("please enter your password: ")

# while attempts < max_attempts:
#     attempts += 1
#     print(f"Attempt number: {attempts}")    
    
#     if password == correct_password:
#         # no need to go to the next attempt, rather break the loop
#         print("Password is correct")
#         break

#     password = input("please try again: ")

# count = 0

# while count < 10:
#     print(count)
#     if count == 5:
#         print("Breaking the loop....")
#         break # Exit the loop from here.

#     count += 1

# print("After loop.")

# Break - terminates the loop immediately and skips the remaining code in the loop.

# while True: 
#     password = input("Please enter your password:")
#     if password == 'secret':
#         print("Access granted")
#         break
#     print("Wrong password, please try again")

# while True:
#     age = int(input("Please enter your age: "))

#     if age < 0:
#         print("age can't be negative")
#     elif age > 120:
#         print("age can't be more than 120")
#     else:
#         #valid age
#         print(f"Valid age: {age}")
#         break

# continue - skips to the next iteration.
# while True:
#     age = int(input("Please enter your age: "))

#     if age < 0:
#         print("age can't be negative")
#         continue
    
#     if age > 120:
#         print("age can't be more than 120")
#         continue
    
#     #valid age
#     print(f"Valid age: {age}")
#     break
    

# Else Clause with loops - gets executed if break was never called
# Else part after loop gets called if loop was terminated without break statement.

# count = 0

# while count < 10:
#     print(count)
#     if count == 11:
#         print("Breaking the loop....")
#         break # Exit the loop from here.

#     count += 1
# else:
#     print("While-Else loop")

# Continue - Skips the current iteration and jumps to the next one.

# Continue vs Break 
# Continue - Skips to the next iteration
# Break - EXITS the loop

# scores = [85, 90, 0, 100, 120, 0, 17, 89, 10]

# total_score = 0
# i = 0

# while i < len(scores):
#     total_score += scores[i]
#     i += 1

# for x in scores:
#     total_score += x

# # print(f"Total matches: {i}")
# print(total_score)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# just iterate over the even indexes. 0 2 4 6 8 
# i = 0

# while i < len(numbers):
#     if i % 2 == 0: # even
#         print(numbers[i])
#     i += 1

# words = ["cat", "elephant", "dog", "giraffe", "ant", "bear", "as", "in", "ab"]

# # only print the words with length >= 3

# for word in words: 
#     if len(word) >= 3:
#         print(word)

# i = 0

# while i < len(words):
#     if len(words[i]) >= 3:
#         print(words[i])

# for loop automatically iterates through each item in the sequence.

# Dictionaries in Python

# student = {
#     'name' : 'Pooja',
#     'age' : 20,
#     'grade' : 'A',
#     'country' : 'India',
# }

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(f"{key} : {value}")

# print(student.get('name'))

# colors = ['red', 'blue', 'green', 'black']

# #Enumerates - if we want to get the indexes also

# for index, color in enumerate(colors):
#     print(f"Index: {index}, Color: {color}")

# Range Function in python

# find the sum of numbers from 1 to 100.

# range(1, 10) => [1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(x, y) from x to < y

# for i in range(1, 101):
#     print(i, end=' ')

# for i in range(1, 101, 2):
#     print(i, end=' ')

# for i in range(10):
#     print(i, end=" ")
    
# range(x, y, z) x = starting point, y = ending point, z = jump
# default start = 0
# default jump = 1

# for i in range(5, 0, -1): 
#     print(i, end=" ")

# start = 0
# end = 5
# jump = -1

# range(x, y, z) 
# i = x
# i < y
# i += z

# for i in range(0, 14, 2):
#     print(i)

# for i in range(10):
#     print("Hello", end=' ')

# n = 5
# for i in range(1, n+1):
#     print(i, end=" ")

# colors = ['red', 'blue', 'green', 'black']

# for i in range(len(colors)):
#     print(colors[i])

# Break and Continue statement in FOR loop - exactly same as while loop.

# colors = ['red', 'blue', 'green', 'black']

# for color in colors:
#     if color == 'green':
#         print("Green Color")
#         break

# numbers = [1, 3, 5, 8, 9, 11, 13, 20, 10]

# # task is to find out the first even number in the list.
# for number in numbers:
#     if number % 2 == 0:
#         print(f"First even number in the list {number}")
#         break
# else:
#     print("Loop terminated without break statement.")


# numbers = [1, 3, 5, 8, 9, 11, 13, 20, 10]
# target = 200

# for num in numbers:
#     if num == target:
#         print("Target found")
#         break
# else:
#     print("Target not found in the list.")
