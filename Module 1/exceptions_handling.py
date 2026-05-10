# Exception - Some unexpected behaviour that occurs while running the code. 

# num1 = int(input())
# num2 = int(input())

# output = num1 / num2

# print("Hello Everyone")

# print(output)

# print("Hello Everyone")

# Exceptions - Runtime errors.

# x = int(input())

# print(x)

# Why exception handling is important ? 
# If we don't handle exceptions, program crashes.
# Ideally, if an exception occurs, we should handle the exception properly and give a proper message to the user on what went wrong.

# try-except
# try - write the code that can potentially throw an exception
# numbers = [1, 2, 3, 4]
# try:
#     num1 = int(input("Please enter 1st number: "))
#     num2 = int(input("Please enter 2nd number: "))
#     # print(numbers[10])
#     output = num1 / num2
# except ValueError as error:
#     # Code to handle the exception - What we are going to do in case an exception happens.
#     # print("Please provide input only in number format.")
#     print(error)
# except ZeroDivisionError as error:
#     # print("We can not divide a number by Zero, please give a non zero denominator")
#     print(error)
# except:
#     print("Something went wrong.")
# else:
#     print("Division successful")
#     print("Result: ", output)
# finally:
#     print("Program completed.")

# Handling specific exceptions - Instead of using general except block, it's better to catch specific exception so that we can share a specific message with the user.

# else block only runs where there NO exception occurs.

# finally block - Runs every time, whether the exception occurs or not.
# Generally clean up operations like closing a file, closing a DB connection etc are performed in finally block

# age = int(input("Please enter your age: "))

# if age < 18:
#     raise ValueError('For driving license, age must be greater than 18.')

# print("You are eligible for driving license.")

class InsufficientBalanceException(Exception):
    pass

class AmountLessThanZeroException(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise AmountLessThanZeroException("Amount must be greater than zero.")

    if amount > balance:
        raise InsufficientBalanceException("Insufficient balance.")

except InsufficientBalanceException as error:
    print("Transaction failed: ", error)
except AmountLessThanZeroException as error:
    print("Transaction failed:", error)

else:
    balance = balance - amount
    print("Transaction successful.")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using our ATM.")

# Custom Exceptions