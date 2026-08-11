# =========================================================
# 04_while_loops.py
# Purpose:
# Learn how while loops execute until a condition becomes
# false and how they are used for retries, polling, and
# continuous processing.
# =========================================================

# =========================================================
# CASE 1
# Basic while loop
# =========================================================

print("CASE 1 -> Basic while loop")

retry_count = 0

while retry_count < 3:
    print("Retry attempt", retry_count)
    retry_count += 1

# =========================================================
# CASE 2
# Counting loop
# =========================================================

print("\nCASE 2 -> Counting loop")

processed_batches = 1

while processed_batches <= 5:
    print("Processing batch", processed_batches)
    processed_batches += 1

# =========================================================
# CASE 3
# Waiting for a condition
# =========================================================

print("\nCASE 3 -> Waiting for a condition")

pipeline_status = "RUNNING"
checks = 0

while pipeline_status == "RUNNING":
    print("Checking pipeline status...")

    checks += 1

    if checks == 3:
        pipeline_status = "SUCCESS"

print("Final status:", pipeline_status)

# =========================================================
# CASE 4
# Retry until success
# =========================================================

print("\nCASE 4 -> Retry until success")

attempt = 0
success = False

while not success and attempt < 5:
    attempt += 1

    print(f"Attempt {attempt}")

    if attempt == 3:
        success = True
        print("Pipeline succeeded")

# =========================================================
# CASE 5
# while with else
# The else block executes if the loop ends normally.
# =========================================================

print("\nCASE 5 -> while with else")

attempt = 0

while attempt < 3:
    print("Attempt", attempt)
    attempt += 1
else:
    print("Retry limit reached")

# =========================================================
# CASE 6
# Infinite loop with manual exit
# =========================================================

print("\nCASE 6 -> Infinite loop with manual exit")

counter = 0

while True:
    print("Heartbeat", counter)

    counter += 1

    if counter == 3:
        print("Stopping monitoring")
        break

# =========================================================
# CASE 7
# Polling for new records
# =========================================================

print("\nCASE 7 -> Polling example")

new_records = []

poll_count = 0

while not new_records:
    print("Polling for records...")

    poll_count += 1

    if poll_count == 2:
        new_records = [
            "record-001",
            "record-002"
        ]

print("Received records:", new_records)

# =========================================================
# CASE 8
# Processing a queue
# =========================================================

print("\nCASE 8 -> Processing a queue")

job_queue = [
    "job-101",
    "job-102",
    "job-103"
]

while job_queue:
    current_job = job_queue.pop(0)

    print("Processing", current_job)

print("Queue is empty")

# =========================================================
# CASE 9
# Timeout simulation
# =========================================================

print("\nCASE 9 -> Timeout simulation")

elapsed_seconds = 0
max_wait = 5

resource_ready = False

while elapsed_seconds < max_wait:
    print(f"Waiting... {elapsed_seconds}s")

    elapsed_seconds += 1

    if elapsed_seconds == 4:
        resource_ready = True
        break

if resource_ready:
    print("Resource became available")
else:
    print("Operation timed out")

# =========================================================
# CASE 10
# Practical production example
# Monitoring a pipeline
# =========================================================

print("\nCASE 10 -> Production monitoring example")

pipeline = {
    "status": "RUNNING",
    "checks": 0
}

while pipeline["status"] == "RUNNING":
    pipeline["checks"] += 1

    print(f"Monitoring check {pipeline['checks']}")

    if pipeline["checks"] == 3:
        pipeline["status"] = "SUCCESS"

print("Pipeline completed successfully")

# =========================================================
# Expected learning
# =========================================================
#
# while loops execute until a condition becomes false.
# Variables inside the loop must usually change.
# while is ideal for retries and polling.
# while True creates a continuous loop.
# break is commonly used to exit infinite loops.
# Empty collections are useful while conditions.
# while loops are heavily used in monitoring systems.
# =========================================================