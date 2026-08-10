# Python match-case

## What is match-case?

`match-case` is Python’s **structural pattern matching** feature introduced in Python 3.10.

It allows a program to compare a value or a data structure against multiple patterns.

Instead of writing:

```python
if status == "SUCCESS":
    ...
elif status == "FAILED":
    ...
elif status == "TIMEOUT":
    ...
else:
    ...
```

you can write:

```python
match status:
    case "SUCCESS":
        ...
    case "FAILED":
        ...
    case "TIMEOUT":
        ...
    case _:
        ...
```

This is often more readable and easier to maintain.

---

## Basic syntax

```python
match value:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:
        ...
```

Python evaluates cases from top to bottom.

The first matching pattern executes.

`_` is the default case.

---

## Matching values

Example:

```python
status = "FAILED"

match status:
    case "SUCCESS":
        print("Completed")
    case "FAILED":
        print("Failed")
    case _:
        print("Unknown")
```

Output:

```text
Failed
```

This is similar to a switch statement in other languages.

---

## Matching multiple values

Use `|` to match several values.

```python
match status:
    case "FAILED" | "TIMEOUT":
        print("Investigate")
```

This is equivalent to:

```python
if status == "FAILED" or status == "TIMEOUT":
    ...
```

---

## Matching numbers

```python
match retry_count:
    case 0:
        print("First attempt")
    case 1:
        print("First retry")
    case 2:
        print("Second retry")
```

Useful for retry logic and status codes.

---

## Guard conditions

A guard adds an additional condition.

Example:

```python
match records:
    case value if value > 1000:
        print("Large batch")
    case value if value > 0:
        print("Small batch")
```

The pattern must match **and** the guard must be true.

Guards are similar to adding an `if` after the pattern.

---

## Tuple matching

Tuples can be matched directly.

```python
event = ("FAILED", 2)

match event:
    case ("FAILED", retry):
        print(retry)
```

Python automatically unpacks the tuple.

You can also ignore values using `_`.

```python
case ("SUCCESS", _):
```

---

## List matching

Example:

```python
asset = ["server-101", "ACTIVE"]

match asset:
    case [asset_id, "ACTIVE"]:
        print(asset_id)
```

Output:

```text
server-101
```

The list structure must match the pattern.

---

## Dictionary pattern matching

One of the most useful features.

Example:

```python
pipeline = {
    "status": "FAILED",
    "retry_count": 2
}

match pipeline:
    case {"status": "FAILED", "retry_count": retry}:
        print(retry)
```

Python checks that the required keys exist.

It extracts the value into `retry`.

---

## Capturing values

Variables inside patterns capture values.

```python
case {"asset_id": asset, "status": "FAILED"}:
```

If the pattern matches:

```python
asset = "server-102"
```

This makes extraction very concise.

---

## Nested pattern matching

Nested structures can be matched directly.

Example:

```python
event = {
    "asset_id": "server-201",
    "metrics": {
        "cpu": 92
    }
}

match event:
    case {
        "asset_id": asset,
        "metrics": {"cpu": cpu}
    }:
        ...
```

Python extracts both `asset` and `cpu`.

This is extremely useful when processing JSON.

---

## Match-case vs if-elif

### if-elif

Better for:

* complex Boolean logic,
* unrelated conditions,
* range comparisons,
* multiple independent variables.

Example:

```python
if cpu > 90 and memory > 80:
    ...
```

### match-case

Better for:

* matching specific values,
* matching structured data,
* event dispatching,
* parsing JSON,
* command handling.

---

## Production example

Suppose an event processing system receives messages.

```python
event = {
    "type": "PIPELINE_FAILED",
    "pipeline": "daily_sales_etl"
}
```

Using `match`:

```python
match event:
    case {"type": "PIPELINE_STARTED", "pipeline": name}:
        ...
    case {"type": "PIPELINE_COMPLETED", "pipeline": name}:
        ...
    case {"type": "PIPELINE_FAILED", "pipeline": name}:
        ...
```

This creates a clean event dispatcher.

---

## Common beginner mistakes

### Mistake 1

Forgetting the default case.

```python
case _:
```

Always include it unless every possible pattern is handled.

### Mistake 2

Using `match` for simple numeric comparisons.

```python
match value:
    case x if x > 10:
```

A normal `if` is often clearer.

### Mistake 3

Expecting `match` to replace all `if` statements.

`match` is excellent for **pattern matching**, not general conditional logic.

---

## Interview note

A concise interview answer:

> `match-case` performs structural pattern matching. It can match literals, tuples, lists, dictionaries, and nested structures while simultaneously extracting values. It is particularly useful for event processing, command dispatching, and parsing structured data such as JSON, and it often provides a cleaner alternative to long `if-elif` chains.
