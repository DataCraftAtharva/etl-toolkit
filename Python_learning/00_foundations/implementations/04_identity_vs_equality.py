# =========================================================

# 04_identity_vs_equality.py

# Purpose:

# Understand the difference between == and is

# =========================================================

print("CASE 1 -> Two separate objects with the same value")

list_a = [10, 20, 30]
list_b = [10, 20, 30]

print("list_a:", list_a)
print("list_b:", list_b)

print("Values are equal (==):", list_a == list_b)
print("Same object (is):", list_a is list_b)

print("id(list_a):", id(list_a))
print("id(list_b):", id(list_b))

print("\nCASE 2 -> Two variables pointing to the same object")

list_c = list_a

print("list_a:", list_a)
print("list_c:", list_c)

print("Values are equal (==):", list_a == list_c)
print("Same object (is):", list_a is list_c)

print("id(list_a):", id(list_a))
print("id(list_c):", id(list_c))

print("\nCASE 3 -> Modifying one reference")

list_c.append(40)

print("list_a:", list_a)
print("list_c:", list_c)

print("Both changed because they reference the same object")

print("\nCASE 4 -> Comparing with None")

result = None

print("result is None:", result is None)
print("result == None:", result == None)

# =========================================================

# Expected learning

# =========================================================

#

# == compares values.

# is compares object identity.

# Variables can point to the same object.

# Use 'is None' when checking for None.

# =========================================================
