# Python for Loops

## What is a for loop?

A `for` loop repeatedly executes a block of code for each element in an iterable.

Example:

```python
assets = ["server-101", "server-102", "server-103"]

for asset in assets:
    print(asset)
````

Output:

```text
server-101
server-102
server-103
```

The loop variable (`asset`) receives one element at a time.

---

# What is an iterable?

An **iterable** is an object whose elements can be accessed one at a time during iteration.

Common Python iterables include:

- lists
    
- tuples
    
- strings
    
- dictionaries
    
- sets
    
- `range()`
    

Example:

```python
assets = ["server-101", "server-102", "server-103"]

for asset in assets:
    print(asset)
```

Conceptually:

```text
assets
   ↓
server-101
   ↓
server-102
   ↓
server-103
```

The `for` loop processes each element one at a time.

### Common iterables

```python
# List
assets = ["server-101", "server-102"]

# Tuple
statuses = ("ACTIVE", "FAILED")

# String
pipeline_name = "ETL"

# Dictionary
pipeline = {
    "name": "sales_etl",
    "status": "SUCCESS"
}

# Set
unique_assets = {"server-101", "server-102"}

# range
numbers = range(5)
```

All of these can be used with a `for` loop.

> Detailed iterator internals (`iter()`, `next()`, generators, etc.) will be covered separately.

---

# Why for loops matter

For loops are the foundation of data processing.

They are used for:

- reading files
    
- processing database rows
    
- handling API responses
    
- transforming records
    
- validating data
    
- generating reports
    
- processing Kafka messages
    
- processing ETL records
    

Almost every Python data engineering task involves iteration.

---

# Iterating over a list

```python
assets = [
    "server-101",
    "server-102",
    "server-103"
]

for asset in assets:
    print(asset)
```

Output:

```text
server-101
server-102
server-103
```

Execution:

```text
Iteration 1 → server-101
Iteration 2 → server-102
Iteration 3 → server-103
```

The loop variable receives one element during each iteration.

---

# Iterating over a string

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

Each iteration receives one character.

---

# Iterating over a tuple

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

Tuples can be iterated over just like lists.

---

# Iterating over a dictionary

Dictionaries require special attention.

Consider:

```python
pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS",
    "retry_count": 0
}
```

## Iterating over keys

```python
for key in pipeline:
    print(key)
```

Output:

```text
name
status
retry_count
```

A normal dictionary iteration iterates over the **keys**.

This is equivalent to:

```python
for key in pipeline.keys():
    print(key)
```

---

## Iterating over values

Use `.values()`.

```python
for value in pipeline.values():
    print(value)
```

Output:

```text
daily_sales_etl
SUCCESS
0
```

---

## Iterating over key-value pairs

Use `.items()`.

```python
for key, value in pipeline.items():
    print(key, value)
```

Output:

```text
name daily_sales_etl
status SUCCESS
retry_count 0
```

This is one of the most common dictionary iteration patterns.

---

## Important dictionary distinction

This:

```python
for item in pipeline:
    print(item)
```

is **not wrong**.

It iterates over the dictionary's keys.

If you need both the key and its corresponding value, use:

```python
for key, value in pipeline.items():
    print(key, value)
```

Mental model:

```text
for key in dictionary
        ↓
      keys

for value in dictionary.values()
        ↓
      values

for key, value in dictionary.items()
        ↓
      key + value
```

---

# Iterating over a set

Sets are iterable.

```python
unique_assets = {
    "server-101",
    "server-102",
    "server-103"
}

for asset in unique_assets:
    print(asset)
```

A set does not provide sequence-style indexing.

Also, do not rely on a particular set iteration order.

For interview and production code, treat set ordering as not guaranteed.

---

# The range() function

`range()` represents a sequence of integers that can be iterated over.

Example:

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

# range() mental model

The general form is:

```python
range(start, stop, step)
```

Think:

```text
start → where to begin
stop  → where to stop before
step  → how much to move each time
```

The `stop` value is **always excluded**.

---

## range(stop)

```python
range(5)
```

Produces:

```text
0
1
2
3
4
```

Equivalent mental model:

```text
start = 0
stop = 5
step = 1
```

Therefore:

```text
0 → 1 → 2 → 3 → 4
```

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

Because:

```text
start = 1
stop = 6
step = 1
```

`6` is excluded.

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

Mental model:

```text
0
 ↓ +2
2
 ↓ +2
4
 ↓ +2
6
 ↓ +2
8
 ↓ +2
10 → stop
```

`10` is excluded.

---

## Negative step

`range()` can also move backwards.

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

Here:

```text
start = 5
stop = 0
step = -1
```

`0` is excluded.

---

# When should you use range()?

Use `range()` when you actually need a sequence of numbers.

For example:

```python
for batch_number in range(1, 6):
    print(f"Processing batch {batch_number}")
```

Output:

```text
Processing batch 1
Processing batch 2
Processing batch 3
Processing batch 4
Processing batch 5
```

If you only need the elements of a collection, don't unnecessarily use indexes.

Prefer:

```python
for asset in assets:
    print(asset)
```

instead of:

```python
for i in range(len(assets)):
    print(assets[i])
```

---

# enumerate()

`enumerate()` is used when you need both:

- the index
    
- the element
    

Consider:

```python
assets = [
    "server-101",
    "server-102",
    "server-103"
]
```

Without `enumerate()`:

```python
for asset in assets:
    print(asset)
```

You get the value but not the index.

Use:

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

# enumerate(start=1)

Indexes normally start at `0`.

You can change the starting index.

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

This is useful when displaying human-readable numbering.

---

# Understanding unpacking

Python can unpack multiple values directly during iteration.

Example:

```python
records = [
    ("server-101", "ACTIVE"),
    ("server-102", "FAILED")
]

for asset_id, status in records:
    print(asset_id, status)
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
```

Each tuple contains two values:

```text
("server-101", "ACTIVE")
        ↓
asset_id    status
```

Python automatically assigns the two values to:

```python
asset_id
status
```

This is called **unpacking**.

---

## Unpacking with enumerate()

`enumerate()` returns two values:

```text
index
value
```

Therefore:

```python
for index, asset in enumerate(assets):
    print(index, asset)
```

works through unpacking.

Conceptually:

```text
(0, "server-101")
        ↓
 index      asset
```

---

## Unpacking with dictionary items()

`.items()` returns key-value pairs.

Therefore:

```python
for key, value in pipeline.items():
    print(key, value)
```

also uses unpacking.

Conceptually:

```text
("status", "SUCCESS")
       ↓
     key       value
```

Unpacking is an important concept behind many Python iteration patterns.

---

# zip()

`zip()` allows you to iterate over multiple iterables together.

Example:

```python
assets = [
    "server-101",
    "server-102",
    "server-103"
]

statuses = [
    "ACTIVE",
    "FAILED",
    "ACTIVE"
]

for asset, status in zip(assets, statuses):
    print(asset, status)
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
server-103 ACTIVE
```

`zip()` pairs elements by position.

Mental model:

```text
assets              statuses

server-101    →     ACTIVE
server-102    →     FAILED
server-103    →     ACTIVE
```

The loop receives:

```text
(asset, status)
```

for each pair.

---

## zip() with three iterables

You can combine more than two iterables.

```python
asset_ids = ["101", "102", "103"]
statuses = ["ACTIVE", "FAILED", "ACTIVE"]
regions = ["Mumbai", "Pune", "Delhi"]

for asset_id, status, region in zip(
    asset_ids,
    statuses,
    regions
):
    print(asset_id, status, region)
```

Output:

```text
101 ACTIVE Mumbai
102 FAILED Pune
103 ACTIVE Delhi
```

This also uses unpacking.

---

## Important zip() behavior

By default, `zip()` stops when the shortest iterable is exhausted.

Example:

```python
assets = ["server-101", "server-102", "server-103"]

statuses = ["ACTIVE", "FAILED"]

for asset, status in zip(assets, statuses):
    print(asset, status)
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
```

`server-103` has no corresponding status, so it is not included.

Mental model:

```text
assets              statuses

server-101    →     ACTIVE
server-102    →     FAILED
server-103    →     no pair

                     ↓

                  STOP
```

---

# Lists of dictionaries

One of the most important ETL patterns.

```python
records = [
    {
        "asset_id": "server-101",
        "status": "ACTIVE"
    },
    {
        "asset_id": "server-102",
        "status": "FAILED"
    },
    {
        "asset_id": "server-103",
        "status": "ACTIVE"
    }
]

for record in records:
    print(
        record["asset_id"],
        record["status"]
    )
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
server-103 ACTIVE
```

This structure appears frequently when processing:

- JSON
    
- API responses
    
- configuration data
    
- event data
    
- database results
    

---

# Conditional processing

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

This is a basic filtering pattern.

Mental model:

```text
Record
  ↓
Check condition
  ↓
True  → process
False → skip
```

---

# Loop Pattern 1 — Counting

Counting occurrences is one of the most common loop patterns.

Example:

```python
statuses = [
    "SUCCESS",
    "FAILED",
    "SUCCESS",
    "SUCCESS"
]

success_count = 0

for status in statuses:
    if status == "SUCCESS":
        success_count += 1

print(success_count)
```

Output:

```text
3
```

Mental model:

```text
counter = 0

SUCCESS → counter = 1
FAILED  → no change
SUCCESS → counter = 2
SUCCESS → counter = 3
```

---

# Loop Pattern 2 — Summation

Use an accumulator when calculating a total.

```python
order_amounts = [1000, 2500, 5000]

total = 0

for amount in order_amounts:
    total += amount

print(total)
```

Output:

```text
8500
```

Mental model:

```text
total = 0

1000 → 1000
2500 → 3500
5000 → 8500
```

This pattern is common in aggregation problems.

---

# Loop Pattern 3 — Searching

A loop can be used to search for a specific value.

```python
assets = [
    "server-101",
    "server-102",
    "server-103"
]

target = "server-102"

found = False

for asset in assets:
    if asset == target:
        found = True
        break

print(found)
```

Output:

```text
True
```

The `break` statement stops the loop once the target is found.

---

# Loop Pattern 4 — Filtering

Filtering means keeping only elements that satisfy a condition.

```python
records = [
    {"asset_id": "server-101", "status": "ACTIVE"},
    {"asset_id": "server-102", "status": "FAILED"},
    {"asset_id": "server-103", "status": "ACTIVE"}
]

active_assets = []

for record in records:
    if record["status"] == "ACTIVE":
        active_assets.append(record["asset_id"])

print(active_assets)
```

Output:

```text
[
    "server-101",
    "server-103"
]
```

Mental model:

```text
Input records
      ↓
Check condition
      ↓
Matching records
      ↓
Build result
```

---

# Loop Pattern 5 — Building result lists

A loop can transform input data into a new list.

Example:

```python
prices = [100, 200, 300]

discounted_prices = []

for price in prices:
    discounted_prices.append(price * 0.9)

print(discounted_prices)
```

Output:

```text
[90.0, 180.0, 270.0]
```

The input collection is transformed into a new collection.

This pattern is extremely important because it leads naturally to:

```python
list comprehensions
```

which will be covered separately.

---

# Nested loops

Loops can be nested.

Example:

```python
regions = [
    "Mumbai",
    "Pune"
]

technologies = [
    "Linux",
    "Windows"
]

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

The inner loop runs completely for each iteration of the outer loop.

---

## Nested loop execution count

If:

```text
len(regions) = n
len(technologies) = m
```

then the total number of iterations is:

```text
n × m
```

Therefore:

```text
Time complexity = O(n × m)
```

If both collections contain `n` elements:

```text
n × n = n²

Time complexity = O(n²)
```

Nested loops can become expensive for large datasets.

---

# A practical ETL example

Suppose pipeline events arrive:

```python
events = [
    {
        "pipeline": "sales_etl",
        "status": "SUCCESS"
    },
    {
        "pipeline": "inventory_etl",
        "status": "FAILED"
    }
]
```

Process them:

```python
success_count = 0
failed_pipelines = []

for event in events:

    if event["status"] == "SUCCESS":
        success_count += 1

    else:
        failed_pipelines.append(
            event["pipeline"]
        )
```

Result:

```text
success_count = 1

failed_pipelines = [
    "inventory_etl"
]
```

This combines:

- iteration
    
- dictionary access
    
- conditional logic
    
- counting
    
- result-list construction
    

These patterns appear frequently in data engineering code.

---

# Common beginner mistakes

## Mistake 1 — Modifying a collection while iterating

Avoid:

```python
for asset in assets:
    assets.remove(asset)
```

Modifying a collection while iterating over it can cause elements to be skipped and can make the behavior difficult to reason about.

Instead, build a new collection when appropriate:

```python
remaining_assets = []

for asset in assets:
    if should_keep(asset):
        remaining_assets.append(asset)
```

---

## Mistake 2 — Using indexes unnecessarily

Instead of:

```python
for i in range(len(assets)):
    print(assets[i])
```

prefer:

```python
for asset in assets:
    print(asset)
```

Use indexes when you actually need the index.

If you need both index and value, use:

```python
for index, asset in enumerate(assets):
    print(index, asset)
```

---

## Mistake 3 — Misunderstanding dictionary iteration

This:

```python
for item in pipeline:
    print(item)
```

iterates over keys.

If you need values:

```python
for value in pipeline.values():
    print(value)
```

If you need both:

```python
for key, value in pipeline.items():
    print(key, value)
```

---

## Mistake 4 — Forgetting that range() excludes stop

This:

```python
range(1, 5)
```

produces:

```text
1
2
3
4
```

not:

```text
1
2
3
4
5
```

Remember:

```text
start → included
stop  → excluded
step  → movement
```

---

## Mistake 5 — Assuming zip() fills missing values

Given:

```python
assets = ["A", "B", "C"]
statuses = ["ACTIVE", "FAILED"]
```

this:

```python
zip(assets, statuses)
```

does not create:

```text
C → something
```

It stops at the shortest iterable.

---

# Complexity of for loops

A basic loop over `n` elements usually performs `n` iterations.

```python
for value in numbers:
    process(value)
```

Time complexity:

```text
O(n)
```

A nested loop can produce:

```text
O(n²)
```

Example:

```python
for x in numbers:
    for y in numbers:
        process(x, y)
```

The exact complexity depends on what the loop body does and how the input sizes relate.

---

# for loop mental model

When you see:

```python
for value in collection:
    process(value)
```

think:

```text
collection
    ↓
one element
    ↓
process
    ↓
next element
    ↓
process
    ↓
...
```

For interview questions, ask:

```text
1. What collection am I iterating?
2. How many elements are there?
3. Is there a condition?
4. Am I counting?
5. Am I summing?
6. Am I searching?
7. Am I filtering?
8. Am I building a result?
9. Is there a nested loop?
10. What is the time complexity?
```

---

# Interview note

A concise interview answer:

> A `for` loop iterates over an iterable such as a list, tuple, string, dictionary, set, or `range`. The loop processes one element at a time. `enumerate()` is useful when both the index and value are required, while `zip()` allows multiple iterables to be processed together. Dictionary iteration can access keys, values, or key-value pairs using direct iteration, `.values()`, or `.items()`. For data engineering, loops are commonly used for filtering, transformation, validation, counting, and processing records.

---

# What to remember

```text
for
 ↓
iterate over an iterable
```

Common iterables:

```text
list
tuple
string
dictionary
set
range
```

Important patterns:

```text
for value in values
        ↓
basic iteration

for index, value in enumerate(values)
        ↓
index + value

for key, value in dictionary.items()
        ↓
key + value

for value in dictionary.values()
        ↓
values only

for a, b in zip(first, second)
        ↓
multiple iterables together

for a, b in records
        ↓
unpacking
```

Core loop patterns:

```text
Counting
Summation
Searching
Filtering
Building result lists
Nested loops
```

The most important idea:

> **A `for` loop processes elements from an iterable one at a time.**