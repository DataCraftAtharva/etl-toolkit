# =========================================================

# 02_lists.py

# Purpose:

# Learn how lists are created, modified, and processed.

# =========================================================

print("CASE 1 -> Creating a list")

files = [
"sales_january.csv",
"sales_february.csv",
"sales_march.csv"
]

print("Files:", files)

print("\nCASE 2 -> List indexing")

print("First file:", files[0])

print("Second file:", files[1])

print("Last file:", files[-1])

print("\nCASE 3 -> List slicing")

print("First two files:", files[0:2])

print("Last two files:", files[-2:])

print("\nCASE 4 -> Adding elements")

files.append("sales_april.csv")

print("After append:", files)

files.extend([
"sales_may.csv",
"sales_june.csv"
])

print("After extend:", files)

files.insert(1, "sales_backup.csv")

print("After insert:", files)

print("\nCASE 5 -> Updating elements")

files[1] = "sales_archive.csv"

print("After update:", files)

print("\nCASE 6 -> Removing elements")

files.remove("sales_archive.csv")

print("After remove:", files)

last_file = files.pop()

print("Removed:", last_file)

print("Remaining files:", files)

print("\nCASE 7 -> Membership and length")

print("Contains sales_april.csv:", "sales_april.csv" in files)

print("Total files:", len(files))

print("\nCASE 8 -> Sorting")

revenues = [1800, 1200, 1500]

print("Original:", revenues)

revenues.sort()

print("Ascending:", revenues)

revenues.sort(reverse=True)

print("Descending:", revenues)

print("\nCASE 9 -> Iterating through a list")

for file_name in files:
    print("Processing", file_name)

print("\nCASE 10 -> Shared reference demonstration")

original_files = ["a.csv", "b.csv"]

shared_files = original_files

shared_files.append("c.csv")

print("original_files:", original_files)

print("shared_files:", shared_files)

print("Both changed because they reference the same list")

# =========================================================

# Expected learning

# =========================================================

#

# Lists are ordered.

# Lists are mutable.

# append(), extend(), insert() add elements.

# remove() and pop() delete elements.

# sort() modifies the list.

# Assignment shares references.

# =========================================================
