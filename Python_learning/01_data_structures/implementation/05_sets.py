# =========================================================
# 05_sets.py
# Purpose:
# Learn how sets store unique values and provide fast lookup.
# =========================================================

print("CASE 1 -> Creating a set")

processed_assets = {
    "server-101",
    "server-102",
    "server-103"
}

print("Processed assets:", processed_assets)

# =========================================================
# CASE 2
# Sets automatically remove duplicates.
# This is one of the most important production use cases.
# =========================================================

print("\nCASE 2 -> Automatic duplicate removal")

incoming_assets = [
    "server-101",
    "server-102",
    "server-101",
    "server-103",
    "server-102"
]

unique_assets = set(incoming_assets)

print("Original list:", incoming_assets)
print("Unique assets:", unique_assets)

# =========================================================
# CASE 3
# Membership testing is extremely fast in sets.
# This is why sets are heavily used in ETL pipelines.
# =========================================================

print("\nCASE 3 -> Membership testing")

print("server-101 processed:", "server-101" in processed_assets)
print("server-999 processed:", "server-999" in processed_assets)

# =========================================================
# CASE 4
# Adding new elements.
# =========================================================

print("\nCASE 4 -> Adding elements")

processed_assets.add("server-104")

print("After adding server-104:", processed_assets)

# =========================================================
# CASE 5
# Adding multiple elements.
# update() accepts any iterable.
# =========================================================

print("\nCASE 5 -> Adding multiple elements")

processed_assets.update([
    "server-105",
    "server-106"
])

print("After update:", processed_assets)

# =========================================================
# CASE 6
# Removing elements.
# remove() raises KeyError if missing.
# discard() does nothing if missing.
# =========================================================

print("\nCASE 6 -> Removing elements")

processed_assets.remove("server-106")

print("After remove:", processed_assets)

processed_assets.discard("server-999")

print("After discard of missing element:", processed_assets)

# =========================================================
# CASE 7
# Union combines unique elements from both sets.
# =========================================================

print("\nCASE 7 -> Union")

batch_1 = {"server-101", "server-102", "server-103"}
batch_2 = {"server-103", "server-104", "server-105"}

all_assets = batch_1 | batch_2

print("Batch 1:", batch_1)
print("Batch 2:", batch_2)
print("Union:", all_assets)

# =========================================================
# CASE 8
# Intersection finds common elements.
# Useful for identifying overlapping records.
# =========================================================

print("\nCASE 8 -> Intersection")

common_assets = batch_1 & batch_2

print("Common assets:", common_assets)

# =========================================================
# CASE 9
# Difference finds elements present in one set only.
# Useful for incremental processing.
# =========================================================

print("\nCASE 9 -> Difference")

new_assets = batch_2 - batch_1

print("New assets to process:", new_assets)

# =========================================================
# CASE 10
# Symmetric difference finds elements present in exactly
# one of the sets.
# =========================================================

print("\nCASE 10 -> Symmetric difference")

changed_assets = batch_1 ^ batch_2

print("Changed assets:", changed_assets)

# =========================================================
# CASE 11
# Sets cannot contain mutable objects.
# Lists are mutable and therefore unhashable.
# =========================================================

print("\nCASE 11 -> Mutable objects are not allowed")

try:
    invalid_set = {[1, 2, 3]}
except TypeError as error:
    print("Error:", error)

# Tuples are immutable and therefore hashable.

valid_set = {(1, 2, 3), (4, 5, 6)}

print("Set containing tuples:", valid_set)

# =========================================================
# CASE 12
# Shared reference demonstration.
# Sets are mutable, so assignment shares references.
# =========================================================

print("\nCASE 12 -> Shared reference demonstration")

original_assets = {"server-101", "server-102"}

backup_assets = original_assets

backup_assets.add("server-103")

print("original_assets:", original_assets)
print("backup_assets:", backup_assets)

print("Both changed because they reference the same set")

# =========================================================
# CASE 13
# Practical production example.
# Deduplicating asset IDs before processing.
# =========================================================

print("\nCASE 13 -> Production deduplication example")

asset_stream = [
    "asset-001",
    "asset-002",
    "asset-001",
    "asset-003",
    "asset-002",
    "asset-004"
]

unique_asset_stream = set(asset_stream)

print("Incoming asset count:", len(asset_stream))
print("Unique asset count:", len(unique_asset_stream))
print("Assets to process:", unique_asset_stream)

# =========================================================
# Expected learning
# =========================================================
#
# Sets store only unique values.
# Duplicate values are removed automatically.
# Membership testing is extremely fast.
# add(), update(), remove(), and discard() modify sets.
# Union, intersection, and difference are powerful operations.
# Mutable objects cannot be stored in sets.
# Assignment shares references.
# Sets are ideal for deduplication and fast lookups.
# =========================================================