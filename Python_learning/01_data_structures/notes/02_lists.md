# Python lists

## What is a list?

A list is an **ordered collection of values**.

Lists can store:

* strings,
* numbers,
* booleans,
* other lists,
* and almost any Python object.

Example:

```python
files = [
    "sales_january.csv",
    "sales_february.csv",
    "sales_march.csv"
]
```

Lists are one of the most commonly used data structures in Python.

---

## Why lists matter

Lists are used everywhere:

* file processing,
* ETL pipelines,
* API responses,
* database records,
* batch processing,
* task scheduling,
* data transformation.

Most Python data processing starts with a list.

---

## Creating lists

```python
files = [
    "sales_january.csv",
    "sales_february.csv",
    "sales_march.csv"
]

revenues = [1200, 1500, 1800]

statuses = [True, False, True]
```

A list is created using square brackets `[]`.

---

## List indexing

Lists are ordered, so every element has a position.

```text
sales_january.csv
sales_february.csv
sales_march.csv

0
1
2
```

Example:

```python
print(files[0])
print(files[1])
print(files[-1])
```

Output:

```text
sales_january.csv
sales_february.csv
sales_march.csv
```

---

## List slicing

Slicing extracts part of a list.

```python
print(files[0:2])
print(files[1:])
print(files[-2:])
```

Output:

```text
['sales_january.csv', 'sales_february.csv']
['sales_february.csv', 'sales_march.csv']
['sales_february.csv', 'sales_march.csv']
```

---

## Lists are mutable

Lists can be modified after creation.

```python
files = ["sales_january.csv"]

files.append("sales_february.csv")
```

Result:

```python
print(files)
```

Output:

```text
['sales_january.csv', 'sales_february.csv']
```

The original list changed.

---

## Adding elements

### append()

Adds one element to the end.

```python
files.append("sales_april.csv")
```

### extend()

Adds multiple elements.

```python
files.extend([
    "sales_may.csv",
    "sales_june.csv"
])
```

### insert()

Adds an element at a specific position.

```python
files.insert(1, "sales_backup.csv")
```

---

## Removing elements

### remove()

Removes by value.

```python
files.remove("sales_backup.csv")
```

### pop()

Removes by index.

```python
last_file = files.pop()
```

### clear()

Removes everything.

```python
files.clear()
```

---

## Updating elements

```python
files[0] = "sales_2026_january.csv"
```

Lists allow in-place modification.

---

## Useful list operations

### Length

```python
len(files)
```

### Membership

```python
"sales_january.csv" in files
```

### Concatenation

```python
q1 = ["jan", "feb", "mar"]
q2 = ["apr", "may", "jun"]

all_months = q1 + q2
```

### Repetition

```python
[0] * 5
```

Output:

```text
[0, 0, 0, 0, 0]
```

---

## Sorting lists

```python
revenues = [1800, 1200, 1500]

revenues.sort()
```

Output:

```text
[1200, 1500, 1800]
```

Descending order:

```python
revenues.sort(reverse=True)
```

---

## Iterating through a list

```python
for file_name in files:
    print(file_name)
```

This is the foundation for processing multiple files.

---

## Common beginner mistakes

### Mistake 1

Expecting assignment to create a copy.

```python
a = [1, 2, 3]
b = a
```

Both variables reference the same list.

### Mistake 2

Removing an element that does not exist.

```python
files.remove("missing.csv")
```

This raises a `ValueError`.

---

## Interview note

A concise interview answer:

> A Python list is an ordered, mutable collection that supports indexing, slicing, iteration, insertion, deletion, sorting, and dynamic resizing.
