# =========================================================

# 01_strings.py

# Purpose:

# Learn how strings are created, accessed, sliced, and processed.

# =========================================================

print("CASE 1 -> Creating strings")

pipeline = "daily_sales_etl"

environment = "development"

print("Pipeline:", pipeline)

print("Environment:", environment)

print("\nCASE 2 -> String length")

print("Length of pipeline:", len(pipeline))

print("\nCASE 3 -> Indexing")

print("First character:", pipeline[0])

print("Second character:", pipeline[1])

print("Last character:", pipeline[-1])

print("\nCASE 4 -> Slicing")

print("Pipeline type:", pipeline[-3:])

print("Pipeline name:", pipeline[0:11])

print("\nCASE 5 -> String methods")

print("Upper case:", pipeline.upper())

print("Lower case:", pipeline.lower())

print("Replace 'sales' with 'inventory':", pipeline.replace("sales", "inventory"))

print("\nCASE 6 -> Splitting a CSV record")

record = "101,Mumbai,1250"

fields = record.split(",")

print("Original record:", record)

print("Fields:", fields)

print("Customer ID:", fields[0])

print("City:", fields[1])

print("Revenue:", fields[2])

print("\nCASE 7 -> Joining values")

parts = ["daily", "sales", "etl"]

pipeline_name = "_".join(parts)

print("Joined pipeline name:", pipeline_name)

print("\nCASE 8 -> String formatting")

status = "SUCCESS"

print(f"Pipeline {pipeline_name} completed with status {status}")

print("\nCASE 9 -> Immutability")

text = "ETL"

print("Original text:", text)

text = text + " Pipeline"

print("After creating a new string:", text)

print("\nCASE 10 -> Useful checks")

file_name = "sales_2026.csv"

print("Ends with .csv:", file_name.endswith(".csv"))

print("Starts with sales:", file_name.startswith("sales"))

print("Contains 2026:", "2026" in file_name)

# =========================================================

# Expected learning

# =========================================================

#

# Strings are immutable.

# Indexing accesses characters.

# Slicing extracts substrings.

# split() separates data.

# join() combines data.

# f-strings create readable output.

# =========================================================
