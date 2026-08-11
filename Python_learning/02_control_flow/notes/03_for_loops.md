# Python for loops

## What is a for loop?

A `for` loop repeatedly executes a block of code for each element in an iterable.

Example:

```python
assets = ["server-101", "server-102", "server-103"]

for asset in assets:
    print(asset)
```

Output:

```text
server-101
server-102
server-103
```

The loop variable (`asset`) receives one element at a time.

---

## Why for loops matter

For loops are the foundation of data processing.

They are used for:

* reading files,
* processing database rows,
* handling API responses,
* transforming records,
* validating data,
* generating reports,
* processing Kafka messages,
* ETL pipelines.

Almost every Python data engineering task involves iteration.

---

## Iterating over a list

```python
assets = [
    "server-101",
    "server-102",
    "server-103"
]

for asset in assets:
    print(asset)
```

Execution:

```text
Iteration 1 -> server-101
Iteration 2 -> server-102
Iteration 3 -> server-103
```

---

## Iterating over a string

Strings are iterable.

```python
for character in "ETL":
    print(character)
```

Output:

```text
E
T
L
```

---

## Iterating over a tuple

```python
pipeline = (
    "daily_sales_etl",
    "SUCCESS"
)

for value in pipeline:
    print(value)
```

Output:

```text
daily_sales_etl
SUCCESS
```

---

## Iterating over a dictionary

### Keys

```python
for key in pipeline:
    print(key)
```

### Values

```python
for value in pipeline.values():
    print(value)
```

### Key-value pairs

```python
for key, value in pipeline.items():
    print(key, value)
```

This is the most common dictionary iteration pattern.

---

## Iterating over a set

```python
unique_assets = {
    "server-101",
    "server-102",
    "server-103"
}

for asset in unique_assets:
    print(asset)
```

Remember that sets are unordered.

The iteration order is not guaranteed.

---

## The range() function

`range()` generates a sequence of numbers.

```python
for i in range(3):
    print(i)
```

Output:

```text
0
1
2
```

The stop value is excluded.

---

## range(start, stop)

```python
for day in range(1, 6):
    print(day)
```

Output:

```text
1
2
3
4
5
```

---

## range(start, stop, step)

```python
for offset in range(0, 10, 2):
    print(offset)
```

Output:

```text
0
2
4
6
8
```

Useful for batch processing.

---

## enumerate()

A common beginner mistake:

```python
for asset in assets:
    print(asset)
```

This does not provide the index.

Use `enumerate()`.

```python
for index, asset in enumerate(assets):
    print(index, asset)
```

Output:

```text
0 server-101
1 server-102
2 server-103
```

---

## enumerate(start=1)

```python
for index, asset in enumerate(assets, start=1):
    print(index, asset)
```

Output:

```text
1 server-101
2 server-102
3 server-103
```

Useful for human-readable numbering.

---

## Lists of dictionaries

One of the most important ETL patterns.

```python
records = [
    {"asset_id": "server-101", "status": "ACTIVE"},
    {"asset_id": "server-102", "status": "FAILED"},
    {"asset_id": "server-103", "status": "ACTIVE"}
]

for record in records:
    print(record["asset_id"], record["status"])
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
server-103 ACTIVE
```

This structure appears constantly in JSON processing.

---

## Conditional processing

Loops often contain conditions.

```python
for record in records:
    if record["status"] == "ACTIVE":
        print(record["asset_id"])
```

Output:

```text
server-101
server-103
```

This is basic filtering.

---

## Accumulating results

A common transformation pattern.

```python
active_assets = []

for record in records:
    if record["status"] == "ACTIVE":
        active_assets.append(record["asset_id"])
```

Result:

```text
[
    "server-101",
    "server-103"
]
```

The loop builds a new collection.

---

## Nested loops

Loops can be nested.

```python
for region in regions:
    for technology in technologies:
        print(region, technology)
```

Output:

```text
Mumbai Linux
Mumbai Windows
Pune Linux
Pune Windows
```

Execution count:

```text
len(regions) × len(technologies)
```

Nested loops can become expensive for large datasets.

---

## A practical ETL example

Suppose pipeline events arrive.

```python
events = [
    {"pipeline": "sales_etl", "status": "SUCCESS"},
    {"pipeline": "inventory_etl", "status": "FAILED"}
]
```

Process them.

```python
success_count = 0
failed_pipelines = []

for event in events:
    if event["status"] == "SUCCESS":
        success_count += 1
    else:
        failed_pipelines.append(event["pipeline"])
```

Result:

```text
success_count = 1

failed_pipelines = ["inventory_etl"]
```

This pattern combines:

* iteration,
* conditions,
* accumulation.

It is a very common interview problem.

---

## Common beginner mistakes

### Mistake 1

Modifying a collection while iterating over it.

```python
for asset in assets:
    assets.remove(asset)
```

This can skip elements.

### Mistake 2

Using indexes unnecessarily.

```python
for i in range(len(assets)):
    print(assets[i])
```

Prefer:

```python
for asset in assets:
    print(asset)
```

### Mistake 3

Forgetting `items()` for dictionaries.

Wrong:

```python
for item in pipeline:
```

Correct:

```python
for key, value in pipeline.items():
```

---

## Interview note

A concise interview answer:

> A `for` loop iterates over any iterable object such as lists, tuples, dictionaries, sets, strings, and ranges. In data engineering, for loops are primarily used to process records, apply transformations, filter data, and accumulate results. `enumerate()` provides indexes during iteration, and dictionary iteration is typically performed using `items()` for key-value access.
