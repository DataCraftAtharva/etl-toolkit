# =========================================================
# 01_if_else.py
# Purpose:
# Learn how Python makes decisions using if, elif, and else.
# =========================================================

# =========================================================
# CASE 1
# Basic if statement
# =========================================================

print("CASE 1 -> Basic if statement")

pipeline_status = "SUCCESS"

if pipeline_status == "SUCCESS":
    print("Pipeline is created Successfully")



# =========================================================
# CASE 2
# if-else statement
# =========================================================

print("\nCASE 2 -> if-else statement")

pipeline_status = "FAILED"


if pipeline_status == "SUCCESS":
    print("Generate Success Report")
else:
    print("Generate Failure Report")



# =========================================================
# CASE 3
# if-elif-else statement
# Multiple conditions
# =========================================================

print("\nCASE 3 -> if-elif-else statement")

pipeline_status = "RUNNING"

if pipeline_status =="SUCCESS":
    print("Pipeline Creates Successfully")
elif pipeline_status =="RUNNING":
    print("Pipeline is Still Running")
elif pipeline_status =="FAILED":
    print("Pipeline Failed")
else:
    print("Unknown Pipeline Status")


# =========================================================
# CASE 4
# Numeric comparisons
# =========================================================

print("\nCASE 4 -> Numeric comparisons")

processed_records = 1250

if processed_records > 1000:
    print("Large batch processed")
else:
    print("Small batch processed")

# =========================================================
# CASE 5
# Using comparison operators
# =========================================================

print("\nCASE 5 -> Comparison operators")

error_count = 3

print("error_count == 3:", error_count == 3)
print("error_count != 3:", error_count != 3)
print("error_count > 2:", error_count > 2)
print("error_count <= 5:", error_count <= 5)

# =========================================================
# CASE 6
# Using logical operators
# and, or, not
# =========================================================

print("\nCASE 6 -> Logical operators")

pipeline_status = "FAILED"
retry_count = 2


if pipeline_status =="FAILED" and retry_count <3:
    print("Retry the pipeline")
elif pipeline_status =="FAILED" or pipeline_status == "TIMEOUT":
    print("Pipeline Requires Attention")
if not pipeline_status =="SUCCESS":
    print("Pipeline did not succeed")

# =========================================================
# CASE 7
# Nested if statements
# =========================================================

print("\nCASE 7 -> Nested if statements")

pipeline = {
    "status": "FAILED",
    "retry_count": 1
}

if pipeline ["status"] =="FAILED":
    if pipeline["retry_count"] <3:
        print("Retry Pipeline")
    else:
        print("Escalate to operations team")


# =========================================================
# CASE 8
# Truthy and falsy values
# =========================================================

print("\nCASE 8 -> Truthy and falsy values")

empty_list = []
processed_assets = ["server-101", "server-102"]

if empty_list:
    print("List Contains the data")
else:
    print("List is empty")

if processed_assets:
    print("These assets are available for processing")



# =========================================================
# CASE 9
# Checking for None
# =========================================================

print("\nCASE 9 -> Checking for None")

owner = None

if owner is None:
    print("There's no owner")
else:
    print("Pipeline Owner",owner)


# =========================================================
# CASE 10
# Practical production example
# Pipeline execution decision
# =========================================================

print("\nCASE 10 -> Production pipeline decision")

pipeline = {
    "status": "FAILED",
    "retry_count": 2,
    "processed_records": 1500
}

if pipeline["status"] == "SUCCESS":
    print("Mark pipeline as completed")
elif pipeline["status"] == "FAILED" and pipeline["retry_count"] < 3:
    print("Retry pipeline execution")
elif pipeline["status"] == "FAILED":
    print("Escalate pipeline failure")
else:
    print("Monitor pipeline status")

# =========================================================
# Expected learning
# =========================================================
#
# if executes when a condition is True.
# else executes when all previous conditions are False.
# elif handles multiple conditions.
# and, or, and not combine conditions.
# Nested if statements allow hierarchical decisions.
# Empty collections are falsy.
# None should be checked using 'is None'.
# Conditional logic drives ETL and workflow decisions.
# =========================================================