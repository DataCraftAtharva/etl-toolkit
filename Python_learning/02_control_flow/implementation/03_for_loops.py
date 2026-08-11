# =========================================================
# 03_for_loops.py
# Purpose:
# Learn how Python for loops iterate over different data
# structures and how they are used in data processing.
# =========================================================

# =========================================================
# CASE 1
# Basic iteration over a list
# =========================================================

print("CASE 1 -> Iterating over a list")

assets = [
    "server-101",
    "server-102",
    "server-103"
]

for asset in assets:
    print("Processing", asset)

# =========================================================
# CASE 2
# Iterating over a string
# =========================================================

print("\nCASE 2 -> Iterating over a string")

pipeline_name = "ETL"


for character in pipeline_name:
    print(character)

# =========================================================
# CASE 3
# Iterating over a tuple
# =========================================================

print("\nCASE 3 -> Iterating over a tuple")

pipeline = (
    "daily_sales_etl",
    "SUCCESS"
)

for value in pipeline:
    print(value)

# =========================================================
# CASE 4
# Iterating over a dictionary
# =========================================================

print("\nCASE 4 -> Iterating over a dictionary")

pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS",
    "retry_count": 2
}

for key, value in pipeline.items():
    print(key, "->", value)

# =========================================================
# CASE 5
# Iterating over a set
# =========================================================

print("\nCASE 5 -> Iterating over a set")

unique_assets = {
    "server-101",
    "server-102",
    "server-103"
}

for asset in unique_assets:
    print(asset)

# =========================================================
# CASE 6
# Using range()
# =========================================================

print("\nCASE 6 -> range()")

for attempt in range(3):
    print("Retry attempt", attempt)

# =========================================================
# CASE 7
# range(start, stop)
# =========================================================

print("\nCASE 7 -> range(start, stop)")

for day in range(1, 6):
    print("Day", day)

# =========================================================
# CASE 8
# range(start, stop, step)
# =========================================================

print("\nCASE 8 -> range(start, stop, step)")

for batch in range(0, 10, 2):
    print("Batch offset", batch)

# =========================================================
# CASE 9
# enumerate()
# =========================================================

print("\nCASE 9 -> enumerate()")

assets = [
    "server-101",
    "server-102",
    "server-103"
]

for index, asset in enumerate(assets):
    print(index, asset)

# =========================================================
# CASE 10
# enumerate(start=1)
# =========================================================

print("\nCASE 10 -> enumerate(start=1)")

for index, asset in enumerate(assets, start=1):
    print(index, asset)

# =========================================================
# CASE 11
# Iterating over a list of dictionaries
# This is one of the most important ETL patterns.
# =========================================================

print("\nCASE 11 -> List of dictionaries")

records = [
    {"asset_id": "server-101", "status": "ACTIVE"},
    {"asset_id": "server-102", "status": "FAILED"},
    {"asset_id": "server-103", "status": "ACTIVE"}
]

for record in records:
    print(record["asset_id"], record["status"])

# =========================================================
# CASE 12
# Conditional processing inside a loop
# =========================================================

print("\nCASE 12 -> Conditional processing")

for record in records:
    if record["status"] == "ACTIVE":
        print("Processing", record["asset_id"])

# =========================================================
# CASE 13
# Accumulating results
# =========================================================

print("\nCASE 13 -> Accumulating results")

active_assets = []

for record in records:
    if record["status"] == "ACTIVE":
        active_assets.append(record["asset_id"])

print("Active assets:", active_assets)

# =========================================================
# CASE 14
# Nested loops
# =========================================================

print("\nCASE 14 -> Nested loops")

regions = ["Mumbai", "Pune"]
technologies = ["Linux", "Windows"]

for region in regions:
    for technology in technologies:
        print(region, technology)

# =========================================================
# CASE 15
# Practical production example
# Processing pipeline events
# =========================================================

print("\nCASE 15 -> Production event processing")

events = [
    {"pipeline": "sales_etl", "status": "SUCCESS"},
    {"pipeline": "inventory_etl", "status": "FAILED"},
    {"pipeline": "security_etl", "status": "SUCCESS"}
]

success_count = 0
failed_pipelines = []

for event in events:
    if event["status"] == "SUCCESS":
        success_count += 1
    else:
        failed_pipelines.append(event["pipeline"])

print("Successful pipelines:", success_count)
print("Failed pipelines:", failed_pipelines)

# =========================================================
# Expected learning
# =========================================================
#
# for loops iterate over any iterable.
# range() generates numeric sequences.
# enumerate() provides indexes.
# Dictionary iteration uses items().
# Loops commonly process lists of dictionaries.
# Conditions inside loops filter records.
# Accumulators collect transformed data.
# Nested loops process combinations of data.
# =========================================================