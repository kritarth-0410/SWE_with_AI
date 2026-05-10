# Problem Statement 1: Bill Splitting System

# You are building a bill splitting system for a group of people.

# Write a Python program that:
# 1. Takes total bill amount as input
# 2. Takes number of people as input
# 3. Takes discount percentage as input
# 4. Calculates the discount amount
# 5. Applies discount to the total bill
# 6. Splits the final amount equally among all people

# The program should display:
# - Original bill amount
# - Discount amount
# - Final bill
# - Amount per person

# Add basic validation:
# - Bill amount should be greater than 0
# - Number of people should not be 0
# - Discount percentage should be between 0 and 100



total_amount = float(input("enter bill amount: "))
total_people = int(input("enter total number of people: "))
discount_percentage = float(input("enter discount percentage:"))

if total_amount <= 0:
    print("error in discount")

elif total_people == 0:
    print("no discount applied")

elif discount_percentage < 0 or discount_percentage > 100:
    print("recheck given discount")

else:
    discount_percentage = (total_amount * discount_percentage)/100
    final_bill = total_amount - discount_percentage
    amt_per_person = final_bill/ total_people


print("\n--------Bill Details---------")
print("Original Bill Amount: ", total_amount)
print("Discount Amount: ", discount_percentage)
print("Final Bill: ", final_bill)
print("amount per person: ", amt_per_person)

