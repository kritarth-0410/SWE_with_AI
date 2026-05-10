# Problem Statement 2: Student Result Analyzer

# Create a Python program that:

# 1. Takes student name as input
# 2. Takes marks of 3 subjects as input
# 3. Calculates:
#    - Total marks
#    - Average marks
# 4. Determines:
#    - Pass or Fail (Pass if average >= 40)
# 5. Assigns grade based on average:
#    - >= 80 → Grade A
#    - >= 60 → Grade B
#    - >= 40 → Grade C
#    - < 40 → Fail

# The program should display:
# - Student name
# - Total marks
# - Average marks (rounded to 2 decimal places)
# - Result (Pass/Fail)
# - Grade

# Add basic validation:
# - Marks should be between 0 and 100


name = input("Enter Your Name: ")

mark1 = int(input("Enter marks of 1 subject: "))
mark2 = int(input("Enter marks of 2 subject: "))
mark3 = int(input("Enter marks of 3 subject: "))

total = mark1 + mark2 + mark3

average = total/3

print("\n-----Result-----")
print("Student name: ", name)
print("Total Marks: ", total)
print("Average Marks: " , round(average,2))

if average >= 40:
    print("Pass")

    if average >= 80:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
else:
    print("Fail")

