# =========================================================
# 04_while_loops.py
# Purpose:
# Practice while loops, loop control, retries, polling,
# queue processing, timeouts, and monitoring.
# =========================================================


# =========================================================
# CASE 1
# Basic while loop
# =========================================================

print("CASE 1 -> Basic while loop")

attempt = 1

while attempt <= 3:
    print("Attempt:", attempt)
    attempt += 1


# =========================================================
# CASE 2
# Counting loop
# =========================================================

print("\nCASE 2 -> Counting loop")

processed_batches = 1

while processed_batches <= 5:
    print("Processing batch:", processed_batches)
    processed_batches += 1


# =========================================================
# CASE 3
# Condition-controlled loop
# =========================================================

print("\nCASE 3 -> Condition-controlled loop")

status = "RUNNING"
checks = 0

while status == "RUNNING":
    print("Pipeline is running")

    checks += 1

    if checks == 3:
        status = "SUCCESS"

print("Final pipeline status:", status)


# =========================================================
# CASE 4
# Retry until success
# =========================================================

print("\nCASE 4 -> Retry until success")

attempt = 0
max_attempts = 5
success = False

while not success and attempt < max_attempts:

    attempt += 1

    print("Attempt:", attempt)

    if attempt == 3:
        success = True
        print("Pipeline succeeded")

print("Total attempts:", attempt)


# =========================================================
# CASE 5
# while with else
# =========================================================

print("\nCASE 5 -> while with else")

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print("Attempt:", attempt)
    attempt += 1
else:
    print("Loop completed normally")


# =========================================================
# CASE 6
# Infinite loop with manual exit
# =========================================================

print("\nCASE 6 -> Infinite loop with manual exit")

counter = 0

while True:
    print("Heartbeat:", counter)

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
max_polls = 5

while not new_records and poll_count < max_polls:

    print("Polling for records...")

    poll_count += 1

    if poll_count == 2:
        new_records = [
            "record-001",
            "record-002"
        ]

if new_records:
    print("Received records:", new_records)
else:
    print("Polling timed out")


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

iteration = 1

while job_queue:

    current_job = job_queue.pop(0)

    print("Iteration:", iteration)
    print("Current job:", current_job)
    print("Remaining queue:", job_queue)

    iteration += 1

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
# Production-style pipeline monitoring
# =========================================================

print("\nCASE 10 -> Production monitoring example")

pipeline = {
    "status": "RUNNING",
    "checks": 0
}

while pipeline["status"] == "RUNNING":

    pipeline["checks"] += 1

    print(
        f"Monitoring check {pipeline['checks']}..."
    )

    if pipeline["checks"] == 3:
        pipeline["status"] = "SUCCESS"

print("Final status:", pipeline["status"])


# =========================================================
# CASE 11
# continue
# =========================================================

print("\nCASE 11 -> continue")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print("Processing:", count)


# =========================================================
# CASE 12
# pass
# =========================================================

print("\nCASE 12 -> pass")

count = 0

while count < 3:

    count += 1

    if count == 2:
        pass

    print("Count:", count)


# =========================================================
# Expected learning
# =========================================================
#
# while -> continue while condition is True.
# Counter -> manually control the number of iterations.
# Condition-controlled -> continue until state changes.
# break -> immediately exit the loop.
# continue -> skip the current iteration.
# pass -> do nothing; placeholder statement.
# while True -> continuous loop with explicit exit.
# Retry -> repeat an operation until success/limit.
# Polling -> repeatedly check external state.
# Queue -> process until collection becomes empty.
# Timeout -> stop waiting after a maximum limit.
# Monitoring -> repeatedly inspect system state.
# =========================================================




# =========================================================
# Problem 1 — Payment Retry
# =========================================================
"""
An order payment can be retried at most 3 times.

Rules:
    If payment succeeds:
        stop retrying

    If payment remains failed after 3 attempts:
        print "Payment failed permanently"

Requirements:
    - use while
    - track attempts
    - stop immediately when payment succeeds
"""

print("\nProblem 1 — Payment Retry")

payment_status = "FAILED"
attempt = 1
max_attempts = 3

while payment_status == "FAILED" and attempt <= max_attempts:

    print(f"Payment attempt {attempt}")

    # Simulate payment succeeding on attempt 2
    if attempt == 2:
        payment_status = "SUCCESS"

    if payment_status == "SUCCESS":
        print(f"Payment succeeded on attempt {attempt}")
        break

    attempt += 1

if payment_status == "FAILED":
    print("Payment failed permanently")


# =========================================================
# Problem 2 — Pipeline Polling
# =========================================================
"""
pipeline_status = "RUNNING"

A pipeline is checked repeatedly.

After the 4th check:
    pipeline_status becomes "SUCCESS"

Requirements:
    - use while
    - track number of checks
    - stop when pipeline is no longer RUNNING
    - print final status
"""

print("\nProblem 2 — Pipeline Polling")

pipeline_status = "RUNNING"
checks = 0

while pipeline_status == "RUNNING":

    checks += 1

    print(f"Checking pipeline — check {checks}")

    if checks == 4:
        pipeline_status = "SUCCESS"

print("Final pipeline status:", pipeline_status)
print("Total checks:", checks)


# =========================================================
# Problem 3 — Maximum Retry
# =========================================================
"""
A data ingestion job can run at most 5 attempts.

Attempt 1 → FAILED
Attempt 2 → FAILED
Attempt 3 → FAILED
Attempt 4 → SUCCESS

Requirements:
    - use while
    - stop immediately on SUCCESS
    - print the successful attempt number
"""

print("\nProblem 3 — Maximum Retry")

pipeline_status = "FAILED"
attempt = 0
max_attempts = 5

while pipeline_status == "FAILED" and attempt < max_attempts:

    attempt += 1

    print(f"Pipeline attempt {attempt}")

    # Simulate success on attempt 4
    if attempt == 4:
        pipeline_status = "SUCCESS"

    if pipeline_status == "SUCCESS":
        print(f"Pipeline succeeded on attempt {attempt}")
        break

if pipeline_status == "FAILED":
    print("Pipeline failed after maximum attempts")


# =========================================================
# Problem 4 — Queue Processing
# =========================================================
"""
jobs = [
    "extract",
    "transform",
    "validate",
    "load"
]

Process every job until the queue becomes empty.

Requirements:
    - use while
    - remove one job at a time
    - process the current job
    - stop when queue is empty
"""

print("\nProblem 4 — Queue Processing")

jobs = [
    "extract",
    "transform",
    "validate",
    "load"
]

iteration = 0

while jobs:

    iteration += 1

    current_job = jobs.pop(0)

    print(f"Iteration {iteration}")
    print(f"Processing job: {current_job}")
    print(f"Remaining jobs: {jobs}")

print("All jobs processed")


# =========================================================
# Problem 5 — Poll for File
# =========================================================
"""
file_available = False

Check repeatedly.

After the 3rd check:
    file_available = True

Requirements:
    - use while
    - track number of checks
    - stop when file becomes available
"""

print("\nProblem 5 — Poll for File")

file_available = False
check_count = 0

while not file_available:

    check_count += 1

    print(f"Checking file — check {check_count}")

    if check_count == 3:
        file_available = True

if file_available:
    print("File is available now")


# =========================================================
# Problem 6 — Timeout
# =========================================================
"""
A service should be waited on for a maximum of 5 checks.

Rules:

    If service becomes ready before the limit:
        Service is ready

    Otherwise:
        Service timed out

Requirements:
    - use while
    - track checks
    - stop when service becomes ready
    - stop when maximum checks are reached
"""

print("\nProblem 6 — Timeout")

service_ready = False
check_count = 0
max_checks = 5

while not service_ready and check_count < max_checks:

    check_count += 1

    print(f"Checking service — attempt {check_count}")

    # Simulate service becoming ready on attempt 4
    if check_count == 4:
        service_ready = True

if service_ready:
    print("Service is ready")
else:
    print("Service timed out")


# =========================================================
# Problem 7 — Skip Invalid Records
# =========================================================
"""
Given:

records = [
    "record-101",
    "",
    "record-102",
    "",
    "record-103"
]

Process all records, but skip empty records.

Requirements:
    - use while
    - use continue
    - print only valid records
"""

print("\nProblem 7 — Skip Invalid Records")

records = [
    "record-101",
    "",
    "record-102",
    "",
    "record-103"
]

index = 0

while index < len(records):

    record = records[index]

    index += 1

    # Skip empty records
    if record == "":
        continue

    print("Processing:", record)


# =========================================================
# Problem 8 — Pipeline Monitoring
# =========================================================
"""
Given:

pipeline = {
    "status": "RUNNING",
    "checks": 0,
    "max_checks": 5
}

Rules:

    RUNNING → continue monitoring

    3rd check → SUCCESS

Requirements:
    - use while
    - update checks
    - stop when status changes
    - print final status
    - print number of checks
"""

print("\nProblem 8 — Pipeline Monitoring")

pipeline = {
    "status": "RUNNING",
    "checks": 0,
    "max_checks": 5
}

while (
    pipeline["status"] == "RUNNING"
    and pipeline["checks"] < pipeline["max_checks"]
):

    pipeline["checks"] += 1

    print(f"Monitoring check {pipeline['checks']}")

    if pipeline["checks"] == 3:
        pipeline["status"] = "SUCCESS"

print("Final pipeline status:", pipeline["status"])
print("Total checks:", pipeline["checks"])


# =========================================================
# Key Patterns Practiced
# =========================================================
#
# 1. Condition-controlled loop
#       while condition:
#
# 2. Counter-controlled loop
#       count += 1
#
# 3. Retry pattern
#       while failed and attempts < max_attempts
#
# 4. Polling pattern
#       while status == "RUNNING"
#
# 5. Queue processing
#       while queue:
#
# 6. Timeout protection
#       while condition and checks < max_checks
#
# 7. Skip current iteration
#       continue
#
# 8. Stop immediately
#       break
#
# 9. Empty collection as condition
#       while jobs:
#
# =========================================================
# End of Implementation
# =========================================================