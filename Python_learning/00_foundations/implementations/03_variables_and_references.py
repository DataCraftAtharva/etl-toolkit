# =========================================================

# 03_variables_and_references.py

# Purpose:

# Understand that variables are references to objects.

# =========================================================

print("STEP 1 -> Creating a variable")

pipeline = "daily_sales_etl"

print("pipeline =", pipeline)

print("Memory id of pipeline:", id(pipeline))

print("\nSTEP 2 -> Creating another variable that points to the same object")

backup_pipeline = pipeline

print("backup_pipeline =", backup_pipeline)

print("Memory id of backup_pipeline:", id(backup_pipeline))

print("Both variables point to the same object:", id(pipeline) == id(backup_pipeline))

print("\nSTEP 3 -> Reassigning the original variable")

pipeline = "customer_etl"

print("pipeline =", pipeline)

print("Memory id of pipeline:", id(pipeline))

print("backup_pipeline =", backup_pipeline)

print("Memory id of backup_pipeline:", id(backup_pipeline))

print("\nSTEP 4 -> Observing the result")

print("pipeline points to a new object")

print("backup_pipeline still points to the original object")

# =========================================================

# Expected learning

# =========================================================

#

# 1. Variables do not store objects directly.

# 2. Variables store references to objects.

# 3. Assignment creates a new reference.

# 4. Reassignment changes where a variable points.

# =========================================================
