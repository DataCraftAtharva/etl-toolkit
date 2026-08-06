# =========================================================
# 06_nested_data_structures.py
# Purpose:
# Learn how nested lists, dictionaries, tuples, and sets work,
# and understand how references behave inside nested objects.
# =========================================================

# =========================================================
# CASE 1
# Nested dictionary
# This is the most common real-world structure (JSON-like data).
# =========================================================

print("CASE 1 -> Nested dictionary")

pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS",
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}

print("Pipeline:", pipeline)
print("Batch size:", pipeline["config"]["batch_size"])

# =========================================================
# CASE 2
# Nested list
# Useful for matrix-like data or grouped records.
# =========================================================

print("\nCASE 2 -> Nested list")

daily_sales = [
    [120, 140, 160],
    [180, 200, 220],
    [240, 260, 280]
]

print("Daily sales:", daily_sales)
print("First day second sale:", daily_sales[0][1])

# =========================================================
# CASE 3
# Dictionary containing a list
# Very common in ETL and API responses.
# =========================================================

print("\nCASE 3 -> Dictionary containing a list")

asset_inventory = {
    "region": "Mumbai",
    "servers": [
        "server-101",
        "server-102",
        "server-103"
    ]
}

print("Inventory:", asset_inventory)
print("First server:", asset_inventory["servers"][0])

# =========================================================
# CASE 4
# List containing dictionaries
# This is one of the most important production patterns.
# =========================================================

print("\nCASE 4 -> List containing dictionaries")

assets = [
    {"id": "server-101", "status": "ACTIVE"},
    {"id": "server-102", "status": "FAILED"},
    {"id": "server-103", "status": "ACTIVE"}
]

print("Assets:", assets)
print("Second asset status:", assets[1]["status"])

# =========================================================
# CASE 5
# Modifying nested objects
# Nested mutable objects can be changed directly.
# =========================================================

print("\nCASE 5 -> Modifying nested objects")

pipeline["config"]["batch_size"] = 5000

print("Updated pipeline:", pipeline)

# =========================================================
# CASE 6
# Shared nested reference
# This is a very common production bug.
# =========================================================

print("\nCASE 6 -> Shared nested reference")

shared_config = {
    "batch_size": 1000,
    "parallelism": 4
}

pipeline_a = {
    "name": "pipeline_a",
    "config": shared_config
}

pipeline_b = {
    "name": "pipeline_b",
    "config": shared_config
}

pipeline_a["config"]["batch_size"] = 9999

print("Pipeline A:", pipeline_a)
print("Pipeline B:", pipeline_b)

print("Both changed because they share the same nested dictionary")

# =========================================================
# CASE 7
# Nested list shared reference
# Demonstrates why [[0] * 3] * 3 is dangerous.
# =========================================================

print("\nCASE 7 -> Shared nested list reference")

matrix = [[0] * 3] * 3

print("Original matrix:", matrix)

matrix[0][0] = 1

print("Modified matrix:", matrix)

print("All rows changed because they reference the same inner list")

# =========================================================
# CASE 8
# Correct way to create nested lists.
# =========================================================

print("\nCASE 8 -> Independent nested lists")

correct_matrix = [[0] * 3 for _ in range(3)]

print("Original matrix:", correct_matrix)

correct_matrix[0][0] = 1

print("Modified matrix:", correct_matrix)

print("Only one row changed because each inner list is independent")

# =========================================================
# CASE 9
# Iterating through nested structures.
# =========================================================

print("\nCASE 9 -> Iterating through nested structures")

for asset in assets:
    print(asset["id"], "->", asset["status"])

# =========================================================
# CASE 10
# Filtering nested data.
# Common ETL transformation pattern.
# =========================================================

print("\nCASE 10 -> Filtering nested data")

active_assets = []

for asset in assets:
    if asset["status"] == "ACTIVE":
        active_assets.append(asset["id"])

print("Active assets:", active_assets)

# =========================================================
# CASE 11
# Nested tuple containing mutable objects.
# Tuples are immutable, but they can contain mutable objects.
# =========================================================

print("\nCASE 11 -> Tuple containing a mutable object")

pipeline_tuple = (
    "daily_sales_etl",
    {
        "batch_size": 1000
    }
)

pipeline_tuple[1]["batch_size"] = 2000

print("Tuple after modification:", pipeline_tuple)

print("The tuple itself is immutable, but the nested dictionary is mutable")

# =========================================================
# CASE 12
# Practical production example.
# Processing nested JSON-like records.
# =========================================================

print("\nCASE 12 -> Production JSON example")

events = [
    {
        "asset_id": "server-101",
        "metrics": {
            "cpu": 78,
            "memory": 65
        }
    },
    {
        "asset_id": "server-102",
        "metrics": {
            "cpu": 92,
            "memory": 81
        }
    }
]

high_cpu_assets = []

for event in events:
    if event["metrics"]["cpu"] > 80:
        high_cpu_assets.append(event["asset_id"])

print("High CPU assets:", high_cpu_assets)

# =========================================================
# Expected learning
# =========================================================
#
# Real-world Python data is usually nested.
# Lists and dictionaries are commonly nested together.
# Nested mutable objects can be modified directly.
# Shared nested references cause unexpected changes.
# [[0] * 3] * 3 creates shared references.
# List comprehensions create independent nested lists.
# Iterating through nested structures is a core ETL skill.
# Nested JSON processing is a common production task.
# =========================================================