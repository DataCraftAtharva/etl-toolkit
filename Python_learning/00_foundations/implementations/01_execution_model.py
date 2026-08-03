# =========================================================

# 01_execution_model.py

# Purpose:

# Observe how Python executes a file from top to bottom.

# Read the comments first, then run the file.

# =========================================================

# ---------------------------------------------------------

# STEP 1

# The Python interpreter starts and begins reading this file.

# The first executable statement is the print() statement below.

# ---------------------------------------------------------

print("STEP 1 -> Python started executing the file")

# ---------------------------------------------------------

# STEP 2

# Python continues to the next line.

# A variable is created and stored in memory.

# ---------------------------------------------------------

pipeline_name = "daily_sales_etl"

print("STEP 2 -> Variable 'pipeline_name' was created")

# ---------------------------------------------------------

# STEP 3

# Python executes the next statement.

# It reads the value stored in the variable and prints it.

# ---------------------------------------------------------

print("STEP 3 -> Pipeline name:", pipeline_name)

# ---------------------------------------------------------

# STEP 4

# Another variable is created.

# ---------------------------------------------------------

environment = "development"

print("STEP 4 -> Environment:", environment)

# ---------------------------------------------------------

# STEP 5

# Python reaches the final statement in the file.

# After executing this line, the program ends.

# ---------------------------------------------------------

print("STEP 5 -> Python reached the end of the file")

# =========================================================

# Expected output

# =========================================================

#

# STEP 1 -> Python started executing the file

# STEP 2 -> Variable 'pipeline_name' was created

# STEP 3 -> Pipeline name: daily_sales_etl

# STEP 4 -> Environment: development

# STEP 5 -> Python reached the end of the file

#

# Notice that the output appears in exactly the same order

# as the code in this file.

# =========================================================
