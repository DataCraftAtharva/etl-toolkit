# =========================================================

# 06_memory_model.py

# Purpose:

# Visualize how Python creates objects and references in memory.

# =========================================================

print("CASE 1 -> Creating an object")

pipeline = "daily_sales_etl"

print("pipeline:", pipeline)

print("id(pipeline):", id(pipeline))

print("\nCASE 2 -> Creating another reference")

backup_pipeline = pipeline

print("backup_pipeline:", backup_pipeline)

print("id(backup_pipeline):", id(backup_pipeline))

print("Same object:", pipeline is backup_pipeline)

print("\nCASE 3 -> Reassigning the variable")

pipeline = "customer_etl"

print("pipeline:", pipeline)

print("id(pipeline):", id(pipeline))

print("backup_pipeline:", backup_pipeline)

print("id(backup_pipeline):", id(backup_pipeline))

print("pipeline now points to a different object")

print("\nCASE 4 -> Mutable object")

numbers = [10, 20]

shared_numbers = numbers

print("Before modification")

print("numbers:", numbers)

print("shared_numbers:", shared_numbers)

print("Same object:", numbers is shared_numbers)

numbers.append(30)

print("After modification")

print("numbers:", numbers)

print("shared_numbers:", shared_numbers)

print("Both changed because the same list object was modified")

print("\nCASE 5 -> Immutable object")

text = "ETL"

shared_text = text

print("Before reassignment")

print("text:", text)

print("shared_text:", shared_text)

text = text + " Pipeline"

print("After reassignment")

print("text:", text)

print("shared_text:", shared_text)

print("A new string object was created")

# =========================================================

# Expected learning

# =========================================================

#

# Variables reference objects.

# Multiple variables can share the same object.

# Reassignment changes the reference.

# Mutable objects change in place.

# Immutable objects create new objects.

# =========================================================
