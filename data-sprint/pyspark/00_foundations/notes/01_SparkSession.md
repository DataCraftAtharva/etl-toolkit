# SparkSession

## Why this matters

`SparkSession` is the main entry point for working with Spark from PySpark.

Almost every PySpark application starts by creating a `SparkSession`.

It allows us to:

- create DataFrames
- read data
- execute Spark SQL
- access Spark configuration
- interact with the Spark execution engine

---

# Mental Model

Think of `SparkSession` as the entry point between our Python application and Spark.

```text
Python Application
        |
        v
  SparkSession
        |
        v
   Spark Engine
        |
    +---+---+
    |       |
  Driver  Executors
```

We write PySpark code through the `SparkSession`.

Spark then builds and executes the required work.

---

# Basic Syntax

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PySpark Learning")
    .getOrCreate()
)
```

---

# Important Components

## `SparkSession`

```python
spark
```

The main object used by our PySpark application.

Example:

```python
df = spark.read.parquet("orders.parquet")
```

---

## `builder`

```python
SparkSession.builder
```

Used to configure and create a `SparkSession`.

---

## `appName`

```python
.appName("PySpark Learning")
```

Sets the application name.

This becomes useful when identifying applications in:

- Spark UI
- cluster managers
- logs
- monitoring systems

Production example:

```python
.appName("daily-orders-etl")
```

---

## `getOrCreate()`

```python
.getOrCreate()
```

Returns an existing `SparkSession` if one already exists.

Otherwise, it creates a new one.

This is generally preferred over repeatedly creating new sessions.

---

# Basic Example

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Orders ETL")
    .getOrCreate()
)

print(spark)
```

---

# Checking Spark Version

```python
print(spark.version)
```

Useful when debugging compatibility problems.

For example, the following versions should be checked for compatibility:

```text
PySpark version
Java version
Python version
Spark version
```

---

# Creating a DataFrame

One of the most important uses of `SparkSession` is creating DataFrames.

```python
data = [
    (101, "Atharva", 5000),
    (102, "Rahul", 3000),
    (103, "Priya", 7000),
]

df = spark.createDataFrame(
    data,
    ["customer_id", "customer_name", "amount"]
)

df.show()
```

Output:

```text
+-----------+-------------+------+
|customer_id|customer_name|amount|
+-----------+-------------+------+
|        101|      Atharva|  5000|
|        102|        Rahul|  3000|
|        103|        Priya|  7000|
+-----------+-------------+------+
```

---

# SparkSession vs SparkContext

Modern PySpark applications generally use:

```text
SparkSession
```

instead of directly interacting with:

```text
SparkContext
```

`SparkSession` provides a higher-level interface for:

- DataFrames
- Spark SQL
- reading data
- writing data
- SQL queries

Internally, `SparkSession` is connected to the Spark execution environment.

---

# SparkSession in a Production ETL

A typical pipeline might look like:

```text
Application
    |
    v
SparkSession
    |
    v
Read Data
    |
    v
Transform
    |
    v
Validate
    |
    v
Write Data
```

Example:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Daily Orders ETL")
    .getOrCreate()
)

orders_df = spark.read.parquet("/data/orders")

# transformations

orders_df.write.parquet("/output/orders")
```

---

# Important Interview Questions

## Beginner

1. What is `SparkSession`?
2. Why do we need `SparkSession`?
3. How do you create a `SparkSession`?
4. What does `getOrCreate()` do?
5. How do you check the Spark version?

## Practical

6. How would you create a DataFrame using `SparkSession`?
7. How would you read a Parquet file?
8. Why should we generally reuse an existing `SparkSession`?

## Deeper

9. What is the difference between `SparkSession` and `SparkContext`?
10. What role does `SparkSession` play in a PySpark application?

---

# Production Notes

## Application Name

Use meaningful application names.

Bad:

```python
.appName("test")
```

Better:

```python
.appName("customer-daily-etl")
```

This makes monitoring and debugging easier.

---

## Don't repeatedly create sessions

Prefer:

```python
spark = (
    SparkSession.builder
    .appName("Orders ETL")
    .getOrCreate()
)
```

rather than repeatedly creating Spark sessions throughout the application.

---

# Key Takeaways

Remember these five things:

```text
1. SparkSession = main entry point to PySpark

2. spark.read = read data

3. spark.createDataFrame() = create DataFrames

4. spark.sql() = execute Spark SQL

5. getOrCreate() = reuse existing session or create one
```

The most important mental model:

```text
Python Code
     ↓
SparkSession
     ↓
Spark
     ↓
DataFrame / SQL
     ↓
Execution
```