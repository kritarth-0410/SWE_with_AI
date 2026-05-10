# String datatype in python.

# Strings are immutable sequence of characters.

# 10000

# name = "Reetu"

# name1 = "Reetu"

# name2 = "Reetu"

# name3 = "Reetu"

# indexing 0    1    2    3    4 
# name = ['R', 'e', 'e', 't', 'u']
#         -5    -4   -3   -2   -1

# print(name)

# Strings are immutable - Once a string is created, it can not be changed.
# Modification in the string, creates a new string.

# name = "Tripti"

# print(name)

# Why immutable ? =>  Safety

# multi-line strings
# paragraph = """

# """

# String Operations

# Concatenation (+)
# first = "Hello"
# second = "World"

# result = first + " " + second

# print(result)

# age = 25

# value = first + age

# print(value)

# Repitition (*)

# print("ha" * 10)

# length

# print(len(first))

# Case conversion 
# print(first.upper())
# print(first.lower())

# strip - removes extra spaces.
# value = "  hell o   \n"
# print(value)
# value = value.strip()
# print(value)

# email1 = "deepak@gmail.com"
# email2 = "kalpesh@gmail.com"

# check if the email starts with deepak
# print(email1.startswith("deepak"))
# print(email2.startswith("deepak"))

# name = "Alice"
# age = 25
# message = f"Hello, {name}! You are {age} years old."
# print(message)

# price = 10
# quantity = 3
# print(f"Total: ${price * quantity}")

# pi = 3.14159927489728947239847
# print(f"Pi value: {pi:.4f}")

# item = "Coffee"
# price = 4.50
# quantity = 2
# total = price * quantity

# print(type(price))
# print(f"Item: {item}")
# print(f"Price: ${price:.2f}")
# print(f"Quantity: {quantity}")
# print(f"Total: ${total:.2f}")

# List - Ordered collection

# students = ["Deepak", "kalpesh", "Harold", "Tripti", "Reetu"]

cities = [] # empty list.
# cities = list() # empty list.

# cities.append("Delhi")

# # Check if list is empty of not
# if not cities:
#     print("List is empty")

# range(start, end, jump) : >= start and < end
# default start = 0
# default jump = 1

# numbers = list(range(100)) # st = 0, end = 100, jump = 1
# print(numbers)

# n = 100
# nums = []
# for i in range(0, 100):
#     x = input("please enter a number")
#     nums.append(x)

# message = "thanks,this,makes,a,lot,sense"

# words = message.split(',')

# print(words)

# Nested List 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print(matrix)

# Indexing in list.
# left to right =  0 to n-1
# right to left = starts with -1


# Positive Indexing
# n = len(list)
# Indices start at 0.
# First element: list[0]
# Last element: list[n - 1]
# Accessing an index out of bounds raises an IndexError.

# Negative Indexing
# Starts from right side of the list.
# -1 refers to the last element of the list.
# -2 refers to the second last element of the list.

# Finding an element inside the list.
# numbers = [10, 20, 40, 7, 90, 1, 5, 4, 2, 3]

# if 100 in numbers:
#     print("10 is present in the numbers list.")
# else:
#     print("10 is not present in the numbers list.")

# matrix = [ [1, 2, 3], [4, 5, 6], [10, 20, 30]]

# print(matrix[2][0])

# Slicing : extracting a part of the list.
# [start:stop:step]
# start: starting index of slicing (included & default = 0)
# end: ending index of slicing (excluded)
# step: Jump (default = 1)

# numbers = [10, 20, 40, 7, 90, 1, 5, 4, 2, 3]

# print(numbers[3:7:2])

# print(numbers[:7]) # No start value, means default value of start which is ZERO
# print(numbers[4:])
# print(numbers[:])
# print(numbers[-3:])
# print(numbers[:-5])
# print(numbers[3:-3])

# print(numbers[:7:2])

# numbers = [10, 20, 40, 7, 90, 1, 5, 4, 2, 3]

#Q: Split this list of numbers into 2 halves.
# size = len(numbers)
# middle = size // 2

# first_half = numbers[0:middle]
# second_half = numbers[middle:]
# print(first_half)
# print(second_half)

# Built-In functions

# numbers = [10, 20, 40, 7, 90, 1, 5, 4, 2, 3, 90]

# print(numbers)
# numbers.sort() # Changing the original list => In-Place & returns None
# print(numbers)

#in-place functions are memory efficient, as they don't unnecessary copies.
#Original data is getting lost.

# List functions - append, extend, insert
# remove(value) -> removes the first occurence of value in the list.
# pop(x) => removes and return the element at index = x
# clear() => removes all the elements.

# sort -> sorts in ascending order.
# sort(reverse=True) => sorts in descending order.

# numbers.reverse() -> reverses in-place.

# print(numbers)

# Custom Sorting

# words = ['apple', 'delhi', 'goa', 'gurgaon', 'orange', 'chennai', 'bangalore']

# words.sort() # sorts the list in alphabetical order.

# Sort based on length of each word.
# words.sort(key=len)

# print(words)

# Searching
# items = ['a', 'b', 'c', 'b', 'd']

# position = items.index('x') # Returns the position of the first occurrence, else it raise ValueError exception.

# print(position)

# original = [4, 1, 3, 2] 
# # copy = original 
# copy = original.copy()

# print(original)
# print(copy)

# original.sort()

# print("=========")

# print(original)
# print(copy)

# sorted function -> doesn't change the original list.

# numbers = [10, 20, 40, 7, 90, 1, 5, 4, 2, 3, 90]

# print(numbers)
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)

# Iterate through the list via loops.

# words = ['apple', 'delhi', 'goa', 'gurgaon', 'orange', 'chennai', 'bangalore']

# foreach loop - most common and frequenly used way
# for word in words: 
#     print(word)

# for i in range(len(words)): # 0 to 6
#     print(words[i])

# enumerate()

# words = ['apple', 'delhi', 'goa', 'gurgaon', 'orange', 'chennai', 'bangalore']

# we can use enumerate() if we want index and value both.
# for i, word in enumerate(words):
#     print(f"{i} : {word}")

# i = 0
# while i < len(words):
#     print(words[i])
#     i += 1

# zip()
# names = ["Kalpesh", "Harold", "Tripti", "Reetu"]
# marks = [90, 92, 89, 85]
# cities = ["Ahemdabad", "Gurgaon", "Kota", "Delhi"]

# for name, mark, city in zip(names, marks, cities):
#     print(f"{name} : {mark} : {city}")

# student_marks = dict(zip(names, marks))
# print(student_marks)


# Don't update the list while iterating.
# If we want to update the list while iterating, create a copy
# nums = [10, 7, 6, 4, 2]
# for num in nums:
#     if num % 2 == 0:
#         nums.remove(num)

# print(nums)

# Tuples - Immutability in sequences

# pin_code = ("deepak", 122101)
# print(pin_code)
# print(type(pin_code))

# pin_code.append('Gurgaon')

# print(pin_code)

# empty = ()

# pin_code = "deepak", 122101

# print(pin_code)
# print(type(pin_code))


# words = ('apple', 'orange', 'banana', 'delhi', 'apple')
# print(words)
# print(words[0])
# print(words[-1])
# print(type(words))
# print(words.count('apple'))
# print(words.index('delhi'))

# Why Tuples ? Immutability, faster than list.

nums = (10, 2, 5, 6, 100, 56, 34, 1, 7, 1000)

print(len(nums))
print(1000 in nums)
print(max(nums))
print(min(nums))
print(sum(nums))

# def get_coordinates():
#     return 10, 3, "100"

# x, y, z = get_coordinates() # unpacking

# print(x)
# print(y)
# print(z)
# print(type(x))
# print(type(y))
# print(type(z))