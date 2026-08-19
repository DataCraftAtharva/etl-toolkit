
from pyspark.sql import SparkSession


# ============================================================
# 1. CREATE SPARK SESSION
# ============================================================

spark = (
    SparkSession.builder
    .appName("SparkSession_creation")
    .getOrCreate()
)




# ============================================================
# 2. CHECK SPARK VERSION
# ============================================================

print("Spark version:",spark.version)




# ============================================================
# 3. CREATE A DATAFRAME
# ============================================================

data = [
    (101, "Atharva", "Mumbai", 5000),
    (102, "Rahul", "Pune", 3000),
    (103, "Priya", "Mumbai", 7000),
    (104, "Neha", "Delhi", 2500),
]

columns = [
    "customer_id",
    "customer_name",
    "city",
    "amount",
]

df = spark.createDataFrame(data, columns)


# ============================================================
# 4. DISPLAY DATAFRAME
# ============================================================

df.show()


# ============================================================
# 5. DISPLAY DATAFRAME SCHEMA
# ============================================================

df.printSchema()


# ============================================================
# 6. BASIC DATAFRAME INFORMATION
# ============================================================

print("Number of rows:", df.count())

print("Number of columns:", len((df.columns)))

print("Columns:", df.columns)


# ============================================================
# 7. CREATE A SECOND DATAFRAME
# ============================================================

data_2 = [
    (105, "Amit", "Bangalore", 4500),
    (106, "Sneha", "Chennai", 6000),
]

df_2 = spark.createDataFrame(data_2, columns)

df_2.show()


# ============================================================
# 8. SIMPLE SPARK SQL
# ============================================================


df.createOrReplaceTempView("customers")

result = spark.sql(
    """
    select 
    city
    from customers
    """
)

result.show()


# ============================================================
# INTERVIEW NOTE
# ============================================================

# Spark transformations are lazy.
#
# Operations such as:
#
#     select()
#     filter()
#     groupBy()
#
# build a logical plan.
#
# They do not necessarily execute immediately.
#
# Actions such as:
#
#     show()
#     count()
#     collect()
#
# trigger execution.


# ============================================================
# PRODUCTION NOTE
# ============================================================

# Avoid:
#
#     df.collect()
#
# on large production datasets.
#
# collect() brings the data back to the DRIVER.
#
# This can cause driver memory problems.


# ============================================================
# CLEANUP
# ============================================================

spark.stop()