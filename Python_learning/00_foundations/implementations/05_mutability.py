# =========================================================

# 05_mutability.py

# Purpose:

# Understand mutable and immutable objects.

# =========================================================

print("CASE 1 -> Mutable list")

original_list = [10, 20, 30]

shared_list = original_list

print("Before modification")

print("original_list:", original_list)

print("shared_list:", shared_list)

print("Same object:", original_list is shared_list)

print("\nAppending 40 to shared_list")

shared_list.append(40)

print("After modification")

print("original_list:", original_list)

print("shared_list:", shared_list)

print("Both changed because they reference the same list object")

print("\nCASE 2 -> Immutable string")

original_text = "ETL"

shared_text = original_text

print("Before reassignment")

print("original_text:", original_text)

print("shared_text:", shared_text)

print("Same object:", original_text is shared_text)

print("\nCreating a new string")

original_text = original_text + " Pipeline"

print("After reassignment")

print("original_text:", original_text)

print("shared_text:", shared_text)

print("shared_text did not change because strings are immutable")

print("\nCASE 3 -> Creating a real copy of a list")

list_a = [1, 2, 3]

list_b = list_a.copy()

print("Before modification")

print("list_a:", list_a)

print("list_b:", list_b)

print("Same object:", list_a is list_b)

print("\nAppending 4 to list_b")

list_b.append(4)

print("After modification")

print("list_a:", list_a)

print("list_b:", list_b)

print("list_a did not change because list_b is a separate copy")

# =========================================================

# Expected learning

# =========================================================

#

# Lists are mutable.

# Strings are immutable.

# Assignment shares references.

# copy() creates a new list object.

# =========================================================
