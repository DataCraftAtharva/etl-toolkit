# =========================================================
# 05_break_continue_pass.py
# Purpose:
# Practice break, continue, and pass.
# Focus:
# - loop termination
# - skipping iterations
# - placeholders
# - nested loops
# - data engineering patterns
# =========================================================


# =========================================================
# CASE 1
# break -> stop loop
# =========================================================

print("CASE 1 -> break")
for attempt in range(1, 6):

    print(f"Attempt {attempt}")

    if attempt == 3:
        print("Stopping attempts")
        break


# =========================================================
# CASE 2
# continue -> skip current iteration
# =========================================================

print("\nCASE 2 -> continue")

records = [
    "record-101",
    "",
    "record-102",
    "",
    "record-103"
]

for record in records:

    if not record:
        continue

    print(f"Processing {record}")


# =========================================================
# CASE 3
# pass -> do nothing
# =========================================================

print("\nCASE 3 -> pass")

for number in range(1, 6):

    if number == 3:
        pass

    print(number)


# =========================================================
# CASE 4
# break -> search
# =========================================================

print("\nCASE 4 -> Search using break")

servers = [
    "server-101",
    "server-102",
    "server-103",
    "server-104"
]

target_server = "server-103"

for server in servers:

    if server == target_server:
        print(f"Found {server}")
        break


# =========================================================
# CASE 5
# continue -> skip invalid records
# =========================================================

print("\nCASE 5 -> Skip invalid records")

records = [
    {"id": 101, "status": "VALID"},
    {"id": 102, "status": "INVALID"},
    {"id": 103, "status": "VALID"},
    {"id": 104, "status": "INVALID"},
]

for record in records:

    if record["status"] == "INVALID":
        continue

    print(f"Processing record {record['id']}")


# =========================================================
# CASE 6
# while + break
# =========================================================

print("\nCASE 6 -> while + break")

attempt = 0
max_attempts = 5

while attempt < max_attempts:

    attempt += 1

    print(f"Pipeline attempt {attempt}")

    if attempt == 3:
        print("Pipeline succeeded")
        break


# =========================================================
# CASE 7
# while + continue
# =========================================================

print("\nCASE 7 -> while + continue")

count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(f"Processing {count}")


# =========================================================
# CASE 8
# Nested loops + break
# =========================================================

print("\nCASE 8 -> Nested loops + break")

for batch in range(1, 4):

    for record in range(1, 4):

        if record == 2:
            break

        print(f"Batch {batch}, Record {record}")


# =========================================================
# CASE 9
# Nested loops + continue
# =========================================================

print("\nCASE 9 -> Nested loops + continue")



for batch in range(1, 3):

    for record in range(1, 4):

        if record == 2:
            continue

        print(f"Batch {batch}, Record {record}")


# =========================================================
# CASE 10
# Practical pipeline monitoring
# =========================================================

print("\nCASE 10 -> Pipeline monitoring")

pipeline_status = "RUNNING"
checks = 0
max_checks = 5

while checks < max_checks:

    checks += 1

    print(f"Monitoring check {checks}")

    # Simulate pipeline success
    if checks == 3:
        pipeline_status = "SUCCESS"

    if pipeline_status == "SUCCESS":
        print("Pipeline completed successfully")
        break


# =========================================================
# EXPECTED LEARNING
# =========================================================
#
# break
# -> immediately terminates the nearest loop.
#
# continue
# -> skips the current iteration.
#
# pass
# -> does nothing.
#
# Nested loops:
# -> break/continue affect the nearest enclosing loop.
#
# Important:
# -> while + continue must still allow loop state to change.
#
# =========================================================
