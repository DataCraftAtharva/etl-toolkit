# =========================================================
# 01_array_fundamentals.py
#
# Purpose:
# Practice basic array/list operations and traversal patterns.
#
# Topics:
# - Access
# - Update
# - Insert
# - Delete
# - Append
# - Remove
# - Traversal
# - Find maximum
# - Find minimum
# - Count occurrences
# - Calculate sum
# =========================================================


# =========================================================
# CASE 1
# Access an element
# =========================================================

print("CASE 1 -> Access")

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Last element:", numbers[-1])


# =========================================================
# CASE 2
# Update an element
# =========================================================

print("\nCASE 2 -> Update")

numbers = [10, 20, 30, 40, 50]

print("Before update:", numbers)

numbers[2] = 45

print("After update:", numbers)


# =========================================================
# CASE 3
# Insert an element
# =========================================================

print("\nCASE 3 -> Insert")

numbers = [10, 20, 30, 40, 50]

print("Before insert:", numbers)

numbers.insert(3, 66)

print("After insert:", numbers)


# =========================================================
# CASE 4
# Delete an element by index
# =========================================================

print("\nCASE 4 -> Delete by index")

numbers = [10, 20, 30, 40, 50]

print("Before delete:", numbers)

del numbers[4]

print("After delete:", numbers)


# =========================================================
# CASE 5
# Append an element
# =========================================================

print("\nCASE 5 -> Append")

numbers = [10, 20, 30, 40]

print("Before append:", numbers)

numbers.append(50)

print("After append:", numbers)


# =========================================================
# CASE 6
# Remove an element by value
# =========================================================

print("\nCASE 6 -> Remove by value")

numbers = [10, 20, 30, 40, 50]

print("Before remove:", numbers)

numbers.remove(30)

print("After remove:", numbers)


# =========================================================
# CASE 7
# Forward traversal
# =========================================================

print("\nCASE 7 -> Traversal")

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# =========================================================
# CASE 8
# Find maximum
# =========================================================

print("\nCASE 8 -> Find maximum")

numbers = [10, 20, 30, 40, 50]

max_element = numbers[0]

for number in numbers:
    if number > max_element:
        max_element = number

print("Maximum element:", max_element)


# =========================================================
# CASE 9
# Find minimum
# =========================================================

print("\nCASE 9 -> Find minimum")

numbers = [10, 20, 30, 40, 50]

min_element = numbers[0]

for number in numbers:
    if number < min_element:
        min_element = number

print("Minimum element:", min_element)


# =========================================================
# CASE 10
# Count occurrences
# =========================================================

print("\nCASE 10 -> Count occurrences")

numbers = [10, 20, 10, 30, 10, 40]

target = 10
count = 0

for number in numbers:
    if number == target:
        count += 1

print(f"Occurrences of {target}:", count)


# =========================================================
# CASE 11
# Calculate sum
# =========================================================

print("\nCASE 11 -> Calculate sum")

numbers = [10, 20, 30, 40, 50]

total_sum = 0

for number in numbers:
    total_sum += number

print("Total sum:", total_sum)


# =========================================================
# CASE 12
# Combined practical example
# =========================================================

print("\nCASE 12 -> Combined array processing")

numbers = [10, 20, 10, 40, 50, 20]

max_element = numbers[0]
min_element = numbers[0]
total_sum = 0
target = 20
target_count = 0

for number in numbers:

    # Maximum
    if number > max_element:
        max_element = number

    # Minimum
    if number < min_element:
        min_element = number

    # Sum
    total_sum += number

    # Count target
    if number == target:
        target_count += 1


print("Numbers:", numbers)
print("Maximum:", max_element)
print("Minimum:", min_element)
print("Sum:", total_sum)
print(f"Count of {target}:", target_count)


# =========================================================
# EXPECTED LEARNING
# =========================================================
#
# Access:
#     numbers[index]
#
# Update:
#     numbers[index] = value
#
# Insert:
#     numbers.insert(index, value)
#
# Delete:
#     del numbers[index]
#
# Append:
#     numbers.append(value)
#
# Remove:
#     numbers.remove(value)
#
# Traversal:
#     for number in numbers
#
# Maximum:
#     Track the largest value while traversing.
#
# Minimum:
#     Track the smallest value while traversing.
#
# Count:
#     Use an accumulator and a condition.
#
# Sum:
#     Use an accumulator.
#
# Core pattern:
#
#     Traverse
#         ↓
#     Inspect each element
#         ↓
#     Apply condition / update state
#         ↓
#     Produce result
#
# =========================================================