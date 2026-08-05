# =========================================================

# 04_dictionaries.py

# Purpose:

# Learn how dictionaries store and process key-value data.

# =========================================================

print("CASE 1 -> Creating a dictionary")

pipeline = {
"name": "daily_sales_etl",
"environment": "development",
"status": "SUCCESS"
}

print("Pipeline:", pipeline)

print("\nCASE 2 -> Accessing values")

print("Pipeline name:", pipeline["name"])

print("Status:", pipeline["status"])

print("\nCASE 3 -> Updating a value")

pipeline["status"] = "FAILED"

print("Updated status:", pipeline)

print("\nCASE 4 -> Adding a new key")

pipeline["processed_records"] = 1250

print("After adding processed_records:", pipeline)

print("\nCASE 5 -> Safe access with get()")

print("Owner:", pipeline.get("owner"))

print("Owner with default:", pipeline.get("owner", "Unknown"))

print("\nCASE 6 -> Checking if a key exists")

print("Contains 'status':", "status" in pipeline)

print("Contains 'retry_count':", "retry_count" in pipeline)

print("\nCASE 7 -> Iterating through a dictionary")

for key, value in pipeline.items():
    print(key, "->", value)

print("\nCASE 8 -> Updating multiple values")

pipeline.update({
"environment": "production",
"retry_count": 3
})

print("After update:", pipeline)

print("\nCASE 9 -> Nested dictionary")

pipeline["config"] = {
"batch_size": 1000,
"parallelism": 4
}

print("Batch size:", pipeline["config"]["batch_size"])

print("\nCASE 10 -> Shared reference demonstration")

original_config = {
"environment": "development",
"retry_count": 3
}

shared_config = original_config

shared_config["retry_count"] = 5

print("original_config:", original_config)

print("shared_config:", shared_config)

print("Both changed because they reference the same dictionary")

print("\nCASE 11 -> Additonal ETL case")
#  :
pipeline = {
    "name": "daily_sales",
    "owner": "data_team"
}

required_keys = ["owner", "schedule", "region"]

result = {
    key: pipeline.get(key, "Unknown")
    for key in required_keys
}

print(result)

# =========================================================

# Expected learning

# =========================================================

#

# Dictionaries store key-value pairs.

# Dictionaries are mutable.

# get() safely accesses missing keys.

# items() is the most useful iteration pattern.

# Nested dictionaries are extremely common.

# Assignment shares references.

# =========================================================
