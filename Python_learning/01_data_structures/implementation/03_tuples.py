# =========================================================

# 03_tuples.py

# Purpose:

# Learn how tuples are created and why immutability matters.

# =========================================================

print("CASE 1 -> Creating a tuple")

pipeline = ("daily_sales_etl", "development", 2026)

print("Pipeline tuple:", pipeline)

print("\nCASE 2 -> Indexing")

print("Pipeline name:", pipeline[0])

print("Environment:", pipeline[1])

print("Year:", pipeline[2])

print("\nCASE 3 -> Slicing")

print("First two values:", pipeline[0:2])

print("Last value:", pipeline[-1:])

print("\nCASE 4 -> Tuple unpacking")

name, environment, year = pipeline

print("Name:", name)

print("Environment:", environment)

print("Year:", year)

print("\nCASE 5 -> Returning multiple values")

def get_pipeline_summary():
    return "SUCCESS", 1250

status, processed_records = get_pipeline_summary()

print("Status:", status)

print("Processed records:", processed_records)

print("\nCASE 6 -> Single-element tuple")

value = (10,)

print("Tuple:", value)

print("Type:", type(value))

print("\nCASE 7 -> Tuple methods")

numbers = (10, 20, 20, 30)

print("Count of 20:", numbers.count(20))

print("Index of 30:", numbers.index(30))

print("\nCASE 8 -> Tuple as dictionary key")

locations = {
(19.0760, 72.8777): "Mumbai",
(28.6139, 77.2090): "Delhi"
}

print("Location lookup:", locations[(19.0760, 72.8777)])

print("\nCASE 9 -> Immutability demonstration")

original = (1, 2, 3)

copy_reference = original
print(id(original))
print(id(copy_reference))
print("Same object:", original is copy_reference)

print("Tuples cannot be modified in place")

# =========================================================

# Expected learning

# =========================================================

#

# Tuples are ordered.

# Tuples are immutable.

# Tuple unpacking is extremely useful.

# Functions often return tuples.

# Tuples can be dictionary keys.

# =========================================================
