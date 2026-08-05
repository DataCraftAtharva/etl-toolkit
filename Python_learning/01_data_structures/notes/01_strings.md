# Python strings

## What is a string?

A string is a sequence of characters enclosed in quotation marks.

Examples:

```python
pipeline = "daily_sales_etl"

environment = 'development'

file_path = "data/sales_2026.csv"
```

Strings are used to represent text.

---

## Why strings matter

Strings are everywhere in Python:

* file names,
* file paths,
* SQL queries,
* JSON keys,
* API responses,
* log messages,
* timestamps,
* configuration values.

A large part of ETL and data engineering work involves processing strings.

---

## Strings are immutable

Strings **cannot be modified after they are created**.

Example:

```python
text = "ETL"

text = text + " Pipeline"
```

Python creates a **new string object**.

Memory before:

```text
text

↓

"ETL"
```

Memory after:

```text
text

↓

"ETL Pipeline"
```

The original string remains unchanged.

---

## Creating strings

```python
pipeline = "daily_sales_etl"

environment = 'development'

message = "Pipeline started successfully"
```

Both single and double quotes create strings.

---

## String length

Use `len()` to count characters.

```python
pipeline = "daily_sales_etl"

print(len(pipeline))
```

Output:

```text
15
```

---

## Indexing

Each character has a position.

```text
daily_sales

012345678910
```

Example:

```python
name = "daily"

print(name[0])

print(name[1])

print(name[-1])
```

Output:

```text
d
a
y
```

Negative indexes count from the end.

---

## Slicing

Slicing extracts part of a string.

Syntax:

```python
text[start:end]
```

Example:

```python
pipeline = "daily_sales_etl"

print(pipeline[0:5])

print(pipeline[6:11])

print(pipeline[-3:])
```

Output:

```text
daily
sales
etl
```

The end index is **not included**.

---

## Common string methods

### Convert case

```python
environment = "Development"

print(environment.lower())

print(environment.upper())
```

### Remove spaces

```python
text = "  ETL Pipeline  "

print(text.strip())
```

### Replace text

```python
file_name = "sales_2025.csv"

print(file_name.replace("2025", "2026"))
```

### Split text

```python
record = "101,Mumbai,1250"

print(record.split(","))
```

Output:

```text
['101', 'Mumbai', '1250']
```

This is extremely common when processing CSV and log files.

---

## Joining strings

```python
parts = ["daily", "sales", "etl"]

pipeline = "_".join(parts)

print(pipeline)
```

Output:

```text
daily_sales_etl
```

---

## String formatting

Use f-strings.

```python
pipeline = "daily_sales_etl"

status = "SUCCESS"

print(f"Pipeline {pipeline} completed with status {status}")
```

Output:

```text
Pipeline daily_sales_etl completed with status SUCCESS
```

F-strings are the preferred formatting method in modern Python.

---

## Checking string content

```python
file_name = "sales_2026.csv"

print(file_name.endswith(".csv"))

print(file_name.startswith("sales"))

print("2026" in file_name)
```

Output:

```text
True
True
True
```

---

## Common beginner mistakes

### Mistake 1

Trying to modify a string directly.

```python
text = "ETL"

text[0] = "A"
```

Output:

```text
TypeError
```

Strings are immutable.

### Mistake 2

Using `+` repeatedly in loops for large strings.

Prefer `"".join()` when combining many strings.

---

## Interview note

A concise interview answer:

> Strings are immutable sequences of characters. Indexing accesses individual characters, slicing extracts substrings, string methods return new strings, and f-strings are the preferred way to format strings in modern Python.
