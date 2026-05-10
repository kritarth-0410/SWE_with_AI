# Problem Statement

# Write a Python program that performs the following tasks:

# Take student name as input.
# Take student marks (integer) as input.
# Take attendance percentage as input.
# Assign grade using conditionals:
# Marks ≥ 90 → Grade A
# Marks ≥ 75 → Grade B
# Marks ≥ 50 → Grade C
# Otherwise → Fail
# Determine scholarship eligibility using nested conditionals:
# Student must NOT fail.
# Attendance must be greater than 80.
# Display output in this format:

# Hello name

# Grade: grade

# Scholarship Eligible: True/False


name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
attendance_percentage = float(input("Enter your attendance percentage: "))

# Grading Conditions
if marks >= 90:
    Grade = "A"
elif marks >= 75:
    Grade = "B"
elif marks >= 50:
    Grade = "C"
else:
    Grade = "Fail"

# Scholarship Eligibility
if Grade != "Fail":
    if attendance_percentage > 80:
        scholarship = True
    else:
        scholarship = False
else:
    scholarship = False

# Display 
print(f"\nHello {name}")
print(f"Grade: {Grade}")
print(f"Scholarship Eligible: {scholarship}")