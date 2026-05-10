# Write a Python program that:

# Takes a list of integers as input
# Converts the list into a set to remove duplicates
# Sorts the unique elements
# Searches for a target element using Binary Search
# Prints whether the element is found or not


# Instructions:

# Use set for uniqueness
# Use sorting before binary search
# Implement binary search manually (not using built-in)
# Write clean and readable code
# Explain time complexity

nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = list(set(nums))
unique_nums.sort()
target = int(input("Enter your target element: "))

start = 0
end = len(unique_nums)-1
found = False

while start <= end:
    mid = (start + end) // 2
    if unique_nums[mid] == target:
        found = True
        break
    elif unique_nums[mid] < target:
        start = mid + 1
    else:
        end = mid - 1


if found:
    print("Element Found")
else:
    print("Element not Found")