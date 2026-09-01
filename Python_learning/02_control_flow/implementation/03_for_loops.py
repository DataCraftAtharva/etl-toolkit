# =========================================================
# 02_for_loops.py
# Purpose:
# Learn Python for loops, iteration, enumerate(), zip(),
# unpacking, nested loops, and common loop patterns.
# =========================================================


# =========================================================
# CASE 1
# Basic list iteration
# =========================================================

print("CASE 1 -> Basic list iteration")

assets = [
    "server-101",
    "server-102",
    "server-103"
]

for asset in assets:
    print(asset)


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
# Keys, values, and key-value pairs
# =========================================================

print("\nCASE 4 -> Dictionary iteration")

pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS",
    "retry_count": 0
}

print("\nDictionary keys:")

for key in pipeline:
    print(key)

print("\nDictionary values:")

for value in pipeline.values():
    print(value)

print("\nDictionary key-value pairs:")

for key, value in pipeline.items():
    print(key, value)


# =========================================================
# CASE 5
# Iterating over a set
# =========================================================

print("\nCASE 5 -> Set iteration")

unique_assets = {
    "server-101",
    "server-102",
    "server-103"
}

for asset in unique_assets:
    print(asset)


# =========================================================
# CASE 6
# range()
# =========================================================

print("\nCASE 6 -> range()")

for number in range(5):
    print(number)


print("\nrange(start, stop):")

for day in range(1, 6):
    print(day)


print("\nrange(start, stop, step):")

for offset in range(0, 10, 2):
    print(offset)


print("\nrange() with negative step:")

for number in range(5, 0, -1):
    print(number)


# =========================================================
# CASE 7
# enumerate()
# =========================================================

print("\nCASE 7 -> enumerate()")

assets = [
    "server-101",
    "server-102",
    "server-103"
]

for index, asset in enumerate(assets):
    print(index, asset)


print("\nenumerate() with start=1:")

for index, asset in enumerate(assets, start=1):
    print(index, asset)


# =========================================================
# CASE 8
# Unpacking
# =========================================================

print("\nCASE 8 -> Unpacking")

records = [
    ("server-101", "ACTIVE"),
    ("server-102", "FAILED"),
    ("server-103", "ACTIVE")
]

for asset_id, status in records:
    print(asset_id, status)


# =========================================================
# CASE 9
# Lists of dictionaries
# =========================================================

print("\nCASE 9 -> Lists of dictionaries")

records = [
    {
        "asset_id": "server-101",
        "status": "ACTIVE"
    },
    {
        "asset_id": "server-102",
        "status": "FAILED"
    },
    {
        "asset_id": "server-103",
        "status": "ACTIVE"
    }
]

for record in records:
    print(
        record["asset_id"],
        record["status"]
    )


# =========================================================
# CASE 10
# zip()
# =========================================================

print("\nCASE 10 -> zip()")

asset_ids = [
    "server-101",
    "server-102",
    "server-103"
]

statuses = [
    "ACTIVE",
    "FAILED",
    "ACTIVE"
]

for asset_id, status in zip(asset_ids, statuses):
    print(asset_id, status)


# =========================================================
# CASE 11
# zip() with multiple iterables
# =========================================================

print("\nCASE 11 -> zip() with multiple iterables")

asset_ids = [
    "101",
    "102",
    "103"
]

statuses = [
    "ACTIVE",
    "FAILED",
    "ACTIVE"
]

regions = [
    "Mumbai",
    "Pune",
    "Delhi"
]

for asset_id, status, region in zip(
    asset_ids,
    statuses,
    regions
):
    print(asset_id, status, region)


# =========================================================
# CASE 12
# Conditional processing
# Filtering active assets
# =========================================================

print("\nCASE 12 -> Conditional processing")

for record in records:

    if record["status"] == "ACTIVE":
        print(record["asset_id"])


# =========================================================
# CASE 13
# Loop pattern -> Counting
# =========================================================

print("\nCASE 13 -> Counting")

statuses = [
    "SUCCESS",
    "FAILED",
    "SUCCESS",
    "SUCCESS"
]


success_count = 0

for status in statuses:
    if status == "SUCCESS":
        success_count+=1

print("Success Count",success_count)






# =========================================================
# CASE 14
# Loop pattern -> Summation
# =========================================================

print("\nCASE 14 -> Summation")

order_amounts = [
    1000,
    2500,
    5000
]
total_amount = 0

for amount in order_amounts:
    total_amount+=amount

print("Total Amount",total_amount)





# =========================================================
# CASE 15
# Loop pattern -> Searching
# =========================================================

print("\nCASE 15 -> Searching")

assets = [
    "server-101",
    "server-102",
    "server-103",
    "server-103"
]


target_asset = "server-103"

found = False

for asset in assets:
    if asset == target_asset:
        found = True
        break


print("Asset found:",found)




# =========================================================
# CASE 16
# Loop pattern -> Filtering
# =========================================================

print("\nCASE 16 -> Filtering")

records = [
    {
        "asset_id": "server-101",
        "status": "ACTIVE"
    },
    {
        "asset_id": "server-102",
        "status": "FAILED"
    },
    {
        "asset_id": "server-103",
        "status": "ACTIVE"
    }
]

active_assets = []


for record in records:
    if record["status"] =="ACTIVE":
        active_assets.append(record["asset_id"])


print("Active Assets",active_assets)



# =========================================================
# CASE 17
# Loop pattern -> Building result lists
# =========================================================

print("\nCASE 17 -> Building result lists")

prices = [
    100,
    200,
    300
]

discounted_prices = []

for price in prices:
    discounted_prices.append(price * 0.9)

print("Discounted prices:", discounted_prices)


# =========================================================
# CASE 18
# Nested loops
# =========================================================

print("\nCASE 18 -> Nested loops")

regions = [
    "Mumbai",
    "Pune"
]

technologies = [
    "Linux",
    "Windows"
]


for region in regions:
    for technology in technologies:
        print(region,technology)




# =========================================================
# CASE 19
# Nested loops with data
# =========================================================

print("\nCASE 19 -> Nested loops with data")

customers = [
    "customer-101",
    "customer-102"
]

orders = [
    "order-1001",
    "order-1002",
    "order-1003"
]

for customer in customers:

    for order in orders:
        print(customer, order)


# =========================================================
# CASE 20
# Practical ETL example
# Count successful pipelines and collect failures
# =========================================================

print("\nCASE 20 -> Practical ETL example")

events = [
    {
        "pipeline": "sales_etl",
        "status": "SUCCESS"
    },
    {
        "pipeline": "inventory_etl",
        "status": "FAILED"
    },
    {
        "pipeline": "customer_etl",
        "status": "SUCCESS"
    },
    {
        "pipeline": "payment_etl",
        "status": "FAILED"
    }
]

success_count = 0
failed_pipelines = []

for event in events:

    if event["status"] == "SUCCESS":
        success_count += 1

    else:
        failed_pipelines.append(
            event["pipeline"]
        )

print("Success count:", success_count)
print("Failed pipelines:", failed_pipelines)


# =========================================================
# CASE 21
# Practical ETL example
# enumerate() + dictionary records
# =========================================================

print("\nCASE 21 -> enumerate() with ETL records")

pipeline_events = [
    {
        "pipeline": "sales_etl",
        "status": "SUCCESS"
    },
    {
        "pipeline": "inventory_etl",
        "status": "FAILED"
    },
    {
        "pipeline": "customer_etl",
        "status": "RUNNING"
    }
]

for index,event in enumerate(pipeline_events,start=1):
    print(
        f"{index}."
        f"{event['pipeline']} -> "
        f"{event['status']}"
    )







# =========================================================
# CASE 22
# Practical ETL example
# zip() for related datasets
# =========================================================

print("\nCASE 22 -> zip() with ETL data")

pipeline_names = [
    "sales_etl",
    "inventory_etl",
    "customer_etl"
]

pipeline_statuses = [
    "SUCCESS",
    "FAILED",
    "RUNNING"
]

for pipeline_name, status in zip(pipeline_names,pipeline_statuses):
    print(f"{pipeline_name} -> {status}")


# ============================================================
# LIST CONCATENATION vs ZIP vs INDEX-BASED PAIRING
# ============================================================

# 1. LIST CONCATENATION
# Use + when you want to combine two lists into one list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
# [1, 2, 3, 4, 5, 6]


# 2. LIST CONCATENATION USING extend()
# extend() modifies the original list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)
# [1, 2, 3, 4, 5, 6]


# Difference:
#
# +       → creates a new list
# extend  → modifies the existing list


# ============================================================
# 3. ZIP() — PAIR CORRESPONDING ELEMENTS
# ============================================================

pipeline_names = [
    "sales_etl",
    "inventory_etl",
    "customer_etl"
]

pipeline_statuses = [
    "SUCCESS",
    "FAILED",
    "RUNNING"
]

for pipeline_name, status in zip(
    pipeline_names,
    pipeline_statuses
):
    print(f"{pipeline_name} -> {status}")

# Output:
# sales_etl -> SUCCESS
# inventory_etl -> FAILED
# customer_etl -> RUNNING


# zip() pairs elements by position:
#
# pipeline_names[0]    ↔ pipeline_statuses[0]
# pipeline_names[1]    ↔ pipeline_statuses[1]
# pipeline_names[2]    ↔ pipeline_statuses[2]


# ============================================================
# 4. PAIRING WITHOUT zip()
# ============================================================

# We can manually use indexes:

for index in range(len(pipeline_names)):
    print(
        f"{pipeline_names[index]} -> "
        f"{pipeline_statuses[index]}"
    )

# Output:
# sales_etl -> SUCCESS
# inventory_etl -> FAILED
# customer_etl -> RUNNING


# ============================================================
# QUICK MEMORY
# ============================================================

# +
# → Combine lists
# [1, 2] + [3, 4] → [1, 2, 3, 4]
#
# extend()
# → Add one list to another existing list
#
# zip()
# → Pair corresponding elements
# [1, 2] + ["A", "B"]
# → (1, "A"), (2, "B")
#
# range(len(...))
# → Useful when you need indexes explicitly
#
# For corresponding elements:
# Prefer zip() because it is cleaner and easier to read.


# =========================================================
# Expected learning
# =========================================================
#
# for loops iterate over iterables.
#
# Common iterables:
# list
# tuple
# string
# dictionary
# set
# range()
#
# Dictionary iteration:
# for key in dictionary
# for value in dictionary.values()
# for key, value in dictionary.items()
#
# range() creates a sequence of integers.
#
# enumerate() provides:
# index + value
#
# zip() combines multiple iterables by position.
#
# Unpacking assigns multiple values directly to variables.
#
# Common loop patterns:
# counting
# summation
# searching
# filtering
# building result lists
#
# Nested loops can result in O(n²) complexity.
#
# for loops are fundamental for Python data processing
# and ETL workloads.
# =========================================================