# =========================================================
# 02_traversal_and_basic_problems.py
#
# Purpose:
# Practice array traversal patterns and basic interview
# problems.
#
# Topics:
# - Forward traversal
# - Value-based traversal
# - Index-based traversal
# - enumerate()
# - Reverse traversal
# - Conditional traversal
# - Accumulators
# - Find maximum
# - Find minimum
# - Count positive numbers
# - Count negative numbers
# - Find first occurrence
# - Find last occurrence
# - Check element existence
# =========================================================


# =========================================================
# CASE 1
# Forward / value-based traversal
# =========================================================

print("CASE 1 -> Forward traversal")

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# =========================================================
# CASE 2
# Index-based traversal
# =========================================================

print("\nCASE 2 -> Index-based traversal")

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers)):
    print(f"Index: {index}, Value: {numbers[index]}")


# =========================================================
# CASE 3
# enumerate()
# =========================================================

print("\nCASE 3 -> enumerate()")

numbers = [10, 20, 30, 40, 50]

for index, number in enumerate(numbers):
    print(f"Index: {index}, Value: {number}")


# =========================================================
# CASE 4
# Reverse traversal
# =========================================================

print("\nCASE 4 -> Reverse traversal")

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])


# =========================================================
# CASE 5
# Traversal with condition
# Find positive numbers
# =========================================================

print("\nCASE 5 -> Positive numbers")

numbers = [-5, 10, -2, 30, 0, 15]

for number in numbers:
    if number > 0:
        print(number)


# =========================================================
# CASE 6
# Count positive numbers
# =========================================================

print("\nCASE 6 -> Count positive numbers")

numbers = [-5, 10, -2, 30, 0, 15]

positive_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1

print("Positive number count:", positive_count)


# =========================================================
# CASE 7
# Count negative numbers
# =========================================================

print("\nCASE 7 -> Count negative numbers")

numbers = [-5, 10, -2, 30, 0, 15]

negative_count = 0

for number in numbers:
    if number < 0:
        negative_count += 1

print("Negative number count:", negative_count)


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
# Find first occurrence
# =========================================================

print("\nCASE 12 -> First occurrence")

numbers = [10, 20, 30, 20, 40]
target = 20

first_index = -1

for index, number in enumerate(numbers):
    if number == target:
        first_index = index
        break

print(f"First occurrence of {target}:", first_index)


# =========================================================
# CASE 13
# Find last occurrence
# =========================================================

print("\nCASE 13 -> Last occurrence")

numbers = [10, 20, 30, 20, 40]
target = 20

last_index = -1

for index, number in enumerate(numbers):
    if number == target:
        last_index = index

print(f"Last occurrence of {target}:", last_index)


# =========================================================
# CASE 14
# Check whether an element exists
# =========================================================

print("\nCASE 14 -> Element existence")

numbers = [10, 20, 30, 40]
target = 30

element_exists = False

for number in numbers:
    if number == target:
        element_exists = True
        break

print(f"Does {target} exist?:", element_exists)


# =========================================================
# CASE 15
# Check element that does not exist
# =========================================================

print("\nCASE 15 -> Element does not exist")

numbers = [10, 20, 30, 40]
target = 99

element_exists = False

for number in numbers:
    if number == target:
        element_exists = True
        break

print(f"Does {target} exist?:", element_exists)


# =========================================================
# CASE 16
# Combined traversal
#
# One traversal can maintain multiple pieces of state.
# =========================================================

print("\nCASE 16 -> Combined traversal")

numbers = [10, -5, 20, -2, 30, 0, 15]

max_element = numbers[0]
min_element = numbers[0]
positive_count = 0
negative_count = 0
total_sum = 0

for number in numbers:

    # Maximum
    if number > max_element:
        max_element = number

    # Minimum
    if number < min_element:
        min_element = number

    # Positive count
    if number > 0:
        positive_count += 1

    # Negative count
    if number < 0:
        negative_count += 1

    # Sum
    total_sum += number


print("Numbers:", numbers)
print("Maximum:", max_element)
print("Minimum:", min_element)
print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Sum:", total_sum)


# =========================================================
# CASE 17
# Reverse traversal with index and value
# =========================================================

print("\nCASE 17 -> Reverse traversal with index")

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers) - 1, -1, -1):
    print(f"Index: {index}, Value: {numbers[index]}")


# =========================================================
# EXPECTED LEARNING
# =========================================================
#
# Forward traversal:
#
#     for number in numbers:
#         ...
#
# Index-based traversal:
#
#     for index in range(len(numbers)):
#         ...
#
# Index + value:
#
#     for index, number in enumerate(numbers):
#         ...
#
# Reverse traversal:
#
#     for index in range(len(numbers) - 1, -1, -1):
#         ...
#
# Counting:
#
#     count = 0
#     for number in numbers:
#         if condition:
#             count += 1
#
# Maximum / minimum:
#
#     Track the best value while traversing.
#
# First occurrence:
#
#     Find → break
#
# Last occurrence:
#
#     Find → update → continue
#
# Existence:
#
#     Boolean flag → break
#
# Accumulator:
#
#     Maintain a result while traversing.
#
# =========================================================