# Python dictionaries

## What is a dictionary?

A dictionary is a **collection of key-value pairs**.

Example:

```python
pipeline = {
    "name": "daily_sales_etl",
    "environment": "development",
    "status": "SUCCESS",
    "processed_records": 1250
}
```

Each key maps to a value.

```text
name --------------> daily_sales_etl
environment -------> development
status ------------> SUCCESS
processed_records -> 1250
```

---

## Why dictionaries matter

Dictionaries are used everywhere in Python:

* JSON data,
* API responses,
* configuration files,
* database records,
* ETL metadata,
* log events,
* caching,
* lookup tables.

Most real-world Python programs process dictionaries.

---

## Creating dictionaries

```python
pipeline = {
    "name": "daily_sales_etl",
    "environment": "development",
    "status": "SUCCESS"
}
```

Keys are usually strings.

Values can be any Python object.

---

## Accessing values

Use the key.

```python
print(pipeline["name"])

print(pipeline["status"])
```

Output:

```text
daily_sales_etl
SUCCESS
```

---

## Updating values

Dictionaries are **mutable**.

```python
pipeline["status"] = "FAILED"
```

Result:

```python
print(pipeline)
```

Output:

```text
{
    'name': 'daily_sales_etl',
    'environment': 'development',
    'status': 'FAILED'
}
```

---

## Adding new key-value pairs

```python
pipeline["processed_records"] = 1250
```

The dictionary grows dynamically.

---

## Removing values

### pop()

```python
status = pipeline.pop("status")
```

Returns the removed value.

### del

```python
del pipeline["environment"]
```

Deletes the key completely.

---

## Safe access with get()

A common beginner mistake:

```python
print(pipeline["owner"])
```

Output:

```text
KeyError
```

Use `get()`.

```python
print(pipeline.get("owner"))
```

Output:

```text
None
```

Provide a default value:

```python
print(pipeline.get("owner", "Unknown"))
```

Output:

```text
Unknown
```

This is the preferred approach when processing external data.

---

## Checking if a key exists

```python
"status" in pipeline
```

Output:

```text
True
```

---

## Iterating through a dictionary

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

This is extremely common in ETL processing.

---

## Dictionary methods

### keys()

```python
pipeline.keys()
```

### values()

```python
pipeline.values()
```

### items()

```python
pipeline.items()
```

### update()

```python
pipeline.update({
    "environment": "production",
    "retry_count": 3
})
```

Updates multiple values at once.

---

## Nested dictionaries

Real data is often nested.

```python
pipeline = {
    "name": "daily_sales_etl",
    "config": {
        "environment": "development",
        "retry_count": 3
    }
}
```

Access nested values:

```python
print(pipeline["config"]["environment"])
```

Output:

```text
development
```

---

## Dictionary memory model

```python
config = {
    "environment": "development"
}

backup = config
```

Memory:

```text
config ------

             ↓

{environment: development}

             ↑

backup ------
```

Updating through one reference affects the other.

---

## Common beginner mistakes

### Mistake 1

Accessing a missing key.

```python
pipeline["owner"]
```

Use `get()` instead.

### Mistake 2

Assuming assignment creates a copy.

```python
backup = pipeline
```

Both variables reference the same dictionary.

---

## Interview note

A concise interview answer:

> A dictionary is a mutable key-value data structure implemented using hashing. It provides fast key lookup, supports dynamic updates, nested structures, and efficient iteration over keys and values.
