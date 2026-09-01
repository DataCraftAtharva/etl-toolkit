# =========================================================
# 02_match_case.py
# Purpose:
# Learn Python structural pattern matching using match-case.
# =========================================================

# =========================================================
# CASE 1
# Basic value matching
# =========================================================

print("CASE 1 -> Basic value matching")

pipeline_status = "SUCCESS"

match pipeline_status:
    case "SUCCESS":
        print("Pipeline completed successfully")
    case "FAILED":
        print("Pipeline failed")
    case _:
        print("Unknown pipeline status")

# =========================================================
# CASE 2
# Multiple possible values
# =========================================================

print("\nCASE 2 -> Multiple values in one case")

pipeline_status = "TIMEOUT"

match pipeline_status:
    case "FAILED" | "TIMEOUT":
        print("Pipeline requires investigation")
    case "SUCCESS":
        print("Pipeline completed")
    case _:
        print("Other status")

# =========================================================
# CASE 3
# Matching numbers
# =========================================================

print("\nCASE 3 -> Matching numbers")

retry_count = 2

match retry_count:
    case 0:
        print("First attempt")
    case 1:
        print("First retry")
    case 2:
        print("Second retry")
    case _:
        print("Maximum retry threshold reached")

# =========================================================
# CASE 4
# Using a guard condition
# =========================================================

print("\nCASE 4 -> Guard conditions")

processed_records = 1500

match processed_records:
    case records if records > 1000:
        print("Large batch processed")
    case records if records > 0:
        print("Small batch processed")
    case _:
        print("No records processed")

# =========================================================
# CASE 5
# Matching a tuple
# =========================================================

print("\nCASE 5 -> Tuple matching")

pipeline_event = ("FAILED", 2)

match pipeline_event:
    case ("SUCCESS", _):
        print("Pipeline succeeded")
    case ("FAILED", retry) if retry < 3:
        print(f"Retry pipeline (attempt {retry})")
    case ("FAILED", _):
        print("Escalate pipeline failure")
    case _:
        print("Unknown event")

# =========================================================
# CASE 6
# Matching a list
# =========================================================

print("\nCASE 6 -> List matching")

asset_record = ["server-101", "ACTIVE"]

match asset_record:
    case [asset_id, "ACTIVE"]:
        print(f"Process active asset: {asset_id}")
    case [asset_id, "FAILED"]:
        print(f"Generate alert for asset: {asset_id}")
    case _:
        print("Unknown asset record")

# =========================================================
# CASE 7
# Matching dictionary structure
# =========================================================

print("\nCASE 7 -> Dictionary pattern matching")

pipeline = {
    "status": "FAILED",
    "retry_count": 2
}


match pipeline:
    case {"status": "SUCCESS"}:
        print("Pipeline completed")
    case {"status": "FAILED", "retry_count": retry} if retry < 3:
        print(f"Retry pipeline (attempt {retry})")
    case {"status": "FAILED"}:
        print("Escalate failure")
    case _:
        print("Unknown pipeline structure")

# =========================================================
# CASE 8
# Capturing values from patterns
# =========================================================

print("\nCASE 8 -> Capturing values")

event = {
    "asset_id": "server-102",
    "status": "FAILED"
}

match event:
    case {"asset_id": asset, "status": "FAILED"}:
        print(f"Alert generated for {asset}")
    case {"asset_id": asset, "status": "ACTIVE"}:
        print(f"Asset {asset} is healthy")
    case _:
        print("Unknown event")


# =========================================================
# CASE 9
# Matching nested dictionaries
# =========================================================

print("\nCASE 9 -> Nested dictionary matching")

event = {
    "asset_id": "server-201",
    "metrics": {
        "cpu": 92
    }
}

match event:
    case {
        "asset_id": asset,
        "metrics": {"cpu": cpu}
    } if cpu > 90:
        print(f"Critical CPU alert for {asset}: {cpu}%")
    case _:
        print("Normal metrics")

# =========================================================
# CASE 10
# Practical production example
# Event dispatcher
# =========================================================

print("\nCASE 10 -> Production event dispatcher")

event = {
    "type": "PIPELINE_FAILED",
    "pipeline": "daily_sales_etl"
}

match event:
    case {"type":"PIPELINE_STARTED","pipeline":pipeline_name}:
        print(f"Start monitoring {pipeline_name} ")
    case {"type":"PIPELINE_COMPLETED","pipeline":pipeline_name}:
        print(f"Generate Completion Report for {pipeline_name}")
    case {"type":"PIPELINE_FAILED","pipeline":pipeline_name}:
        print(f"Generate Alert for {pipeline_name}")
    case _:
        print("Ignore unknown event")

# =========================================================
# Expected learning
# =========================================================
#
# match-case is cleaner than long if-elif chains.
# Multiple values can be matched with |.
# Guards add conditional logic.
# Tuples, lists, and dictionaries can be matched directly.
# Values can be captured during matching.
# Nested structures can be matched elegantly.
# match-case is useful for event processing and dispatching.
# =========================================================


# =========================================================
# PRACTICE PROBLEMS
# =========================================================

# Problem 1
# Given:
# job = ("FAILED", 2)
#
# Use match-case to print:
# "Retry job"
# when retry_count < 3.
job = ("FAILED", 2)
match job:
    case("SUCCESS",_):
        print("Pipeline Created Successfully")
    case("FAILED",retry) if retry <3:
        print("Retry Pipeline")
    case("FAILED",retry) if retry > 3:
        print("Pipeline Retry Exhausted and pipeline failed")
    case _:
        print("Unknown Status")




# Problem 2
# Given:
# response = {
#     "status": 200,
#     "data": "success"
# }
#
# Handle:
# 200 -> Success
# 404 -> Not Found
# 500 -> Server Error
# anything else -> Unknown
response = {
   "status": 200,
  "data": "success"
}
match response:
    case{"status":200,"data":"success"}:
        print("Success")
    case {"status": 404}:
        print("Not Found")
    case {"status": 500}:
        print("Server Error")
    case _:
        print("Unknown")

# Problem 3
# Given:
# event = {
#     "type": "ORDER_CREATED",
#     "order_id": 101
# }
#
# Extract order_id and print:
# "Process order 101"

event = {
    "type": "ORDER_CREATED",
    "order_id": 101}

match event:
    case{"type":"ORDER_CREATED","order_id":order_id}:
        print(f"Order Created for order_id {order_id}")
    case _:
        print("Unknown Order")


# Problem 4
# Given:
# event = {
#     "type": "PIPELINE",
#     "details": {
#         "status": "FAILED",
#         "retry_count": 2
#     }
# }
#
# Print "Retry pipeline" when retry_count < 3.
event = {
    "type": "PIPELINE",
    "details": {
        "status": "FAILED",
        "retry_count": 2
    }}
match event:
    case{"type":"PIPELINE","details":{
        "status": "FAILED",
        "retry_count": retry
    }}if retry <3:
        print(f"Pipeline Retried for  {retry} times")
    case {"type": "PIPELINE", "details": {
        "status": "SUCCESS",
    }}:
        print(f" Pipeline created Successfully")
    case _:
        print("Unknown Order")

# Problem 5
# Given:
# records = [
#     "server-101",
#     "server-102",
#     "server-103"
# ]
#
# Capture:
# first_server
# remaining_servers
#
# using sequence pattern matching.

records = [
    "server-101",
    "server-102",
    "server-103"
]


match records:
    case [first_server, *remaining_servers]:
        print(f"First server: {first_server}")
        print(f"Remaining servers: {remaining_servers}")