# #  Python Assignment Question

# 1. Write a function `format_name(name)` that takes a student's name as input and returns it in title case (first letter capital of each word).
# 2. Write a function `calculate_average(marks)` that takes a list of marks and returns the average.
# 3. Write a function `get_grade(avg)` that returns:
#    * "A" if average ≥ 90
#    * "B" if average ≥ 75
#    * "C" if average ≥ 50
#    * "Fail" otherwise
# 4. Write a function `student_summary(name, marks, course="Python Basics")` that:
#    * Uses the above functions
#    * Returns a formatted string using f-strings showing:
#    * Student Name
#    * Course Name
#    * Grade
# 5. Take input from the user:
#    * Student name
#    * Number of subjects
#    * Marks for each subject (store in a list)
# 6. Perform the following list operations:
#    * Print the first mark
#    * Print the middle portion of the list (excluding first and last elements)
#    * Print all marks using a loop
# 7. Create a tuple `(name, course, grade)` and print it.
# 8. Add a comment explaining why tuple values cannot be changed.
# 9. Display the final output including:
#    * Greeting with formatted name
#    * Marks list
#    * Average marks
#    * Grade
#    * Student summary


# Function to format name
def format_name(name):
    return name.title()

# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to get grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

# Function to create student summary
def student_summary(name, marks, course="Python Basics"):
    formatted_name = format_name(name)
    avg = calculate_average(marks)
    grade = get_grade(avg)
    
    return f"Student: {formatted_name}\nCourse: {course}\nGrade: {grade}"

# ---------------- MAIN PROGRAM ----------------

# Input
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

marks = []
for i in range(n):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

# Formatting name
formatted_name = format_name(name)

# Output
print(f"\nHello {formatted_name}")

print("\nMarks List:", marks)

# First mark
print("First Mark:", marks[0])

# Middle marks (excluding first and last)
print("Middle Marks:", marks[1:-1])

# Print marks one by one
print("\nMarks one by one:")
for m in marks:
    print(m)

# Calculate average and grade
avg = calculate_average(marks)
grade = get_grade(avg)

print(f"\nAverage Marks: {avg}")
print(f"Grade: {grade}")

# Create tuple
student_info = (formatted_name, "Python Basics", grade)
print("\nStudent Info:", student_info)

# Tuple is immutable (cannot be changed after creation)

# Final summary
print("\nStudent Summary:")
print(student_summary(name, marks))