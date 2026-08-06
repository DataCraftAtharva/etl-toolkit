# =========================================================
# 07_copying_and_deepcopy.py
# Purpose:
# Learn the difference between assignment, shallow copy,
# and deep copy, especially for nested data structures.
# =========================================================

import copy

# =========================================================
# CASE 1
# Assignment does not create a copy.
# Both variables reference the same object.
# =========================================================

print("CASE 1 -> Assignment shares references")

pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS"
}

backup = pipeline

backup["status"] = "FAILED"

print("pipeline:", pipeline)
print("backup:", backup)

print("Both changed because they reference the same dictionary")

# =========================================================
# CASE 2
# Shallow copy creates a new outer dictionary.
# =========================================================

print("\nCASE 2 -> Shallow copy of a flat dictionary")

pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS"
}

backup = pipeline.copy()

backup["status"] = "FAILED"

print("pipeline:", pipeline)
print("backup:", backup)

print("The dictionaries are independent because there are no nested objects")

# =========================================================
# CASE 3
# Shallow copy with a nested dictionary.
# The outer dictionary is copied,
# but the nested dictionary is shared.
# =========================================================

print("\nCASE 3 -> Shallow copy with nested data")

pipeline = {
    "name": "daily_sales_etl",
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}

backup = pipeline.copy()

backup["config"]["batch_size"] = 5000

print("pipeline:", pipeline)
print("backup:", backup)

print("Both changed because the nested dictionary is shared")

# =========================================================
# CASE 4
# Deep copy creates completely independent objects.
# =========================================================

print("\nCASE 4 -> Deep copy")

pipeline = {
    "name": "daily_sales_etl",
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}

backup = copy.deepcopy(pipeline)

backup["config"]["batch_size"] = 9999

print("pipeline:", pipeline)
print("backup:", backup)

print("Deep copy created completely independent nested objects")

# =========================================================
# CASE 5
# IDs reveal what is shared.
# =========================================================

print("\nCASE 5 -> Object identities")

pipeline = {
    "config": {
        "batch_size": 1000
    }
}

shallow = pipeline.copy()
deep = copy.deepcopy(pipeline)

print("Outer dictionary IDs")
print(id(pipeline))
print(id(shallow))
print(id(deep))

print("\nNested dictionary IDs")
print(id(pipeline["config"]))
print(id(shallow["config"]))
print(id(deep["config"]))

# =========================================================
# CASE 6
# Shallow copy of nested lists.
# =========================================================

print("\nCASE 6 -> Shallow copy of nested lists")

matrix = [
    [1, 2],
    [3, 4]
]

matrix_copy = matrix.copy()

matrix_copy[0][0] = 999

print("matrix:", matrix)
print("matrix_copy:", matrix_copy)

print("Inner lists are shared")

# =========================================================
# CASE 7
# Deep copy of nested lists.
# =========================================================

print("\nCASE 7 -> Deep copy of nested lists")

matrix = [
    [1, 2],
    [3, 4]
]

matrix_copy = copy.deepcopy(matrix)

matrix_copy[0][0] = 999

print("matrix:", matrix)
print("matrix_copy:", matrix_copy)

print("Inner lists are independent")

# =========================================================
# CASE 8
# Copying lists using slicing.
# Slicing performs a shallow copy.
# =========================================================

print("\nCASE 8 -> List slicing copy")

servers = [
    {"id": "server-101"},
    {"id": "server-102"}
]

backup = servers[:]

backup[0]["id"] = "modified-server"

print("servers:", servers)
print("backup:", backup)

print("The list was copied, but the dictionaries are shared")

# =========================================================
# CASE 9
# copy.copy() is equivalent to a shallow copy.
# =========================================================

print("\nCASE 9 -> copy.copy()")

pipeline = {
    "config": {
        "batch_size": 1000
    }
}

backup = copy.copy(pipeline)

backup["config"]["batch_size"] = 7000

print("pipeline:", pipeline)
print("backup:", backup)

# =========================================================
# CASE 10
# Practical production example.
# Pipeline configuration templates.
# =========================================================

print("\nCASE 10 -> Production configuration example")

pipeline_template = {
    "retry_count": 3,
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}

pipeline_a = copy.deepcopy(pipeline_template)
pipeline_b = copy.deepcopy(pipeline_template)

pipeline_a["config"]["batch_size"] = 5000

print("Template:", pipeline_template)
print("Pipeline A:", pipeline_a)
print("Pipeline B:", pipeline_b)

print("Deep copy prevents accidental configuration sharing")

# =========================================================
# Expected learning
# =========================================================
#
# Assignment shares references.
# copy() creates a shallow copy.
# Shallow copy shares nested mutable objects.
# deepcopy() recursively copies nested objects.
# IDs help identify shared references.
# Nested lists and dictionaries are the main source of copy bugs.
# Deep copy is essential when independent nested objects are required.
# =========================================================