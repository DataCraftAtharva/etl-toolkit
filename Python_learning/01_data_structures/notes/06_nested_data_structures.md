# Python nested data structures

## What are nested data structures?

A nested data structure is a **collection that contains other collections**.

Examples:

* dictionary containing a dictionary,
* dictionary containing a list,
* list containing dictionaries,
* list containing lists,
* tuple containing dictionaries.

Example:

```python
pipeline = {
    "name": "daily_sales_etl",
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}
```

Memory concept:

```text
pipeline
   |
   v
{
  name ---------> "daily_sales_etl"
  config -------+
                |
                v
           {
             batch_size ----> 1000
             parallelism --> 4
           }
}
```

Nested structures are simply objects that reference other objects.

---

## Why nested structures matter

Real-world data is almost always nested.

Examples:

* JSON API responses,
* Kafka messages,
* Elasticsearch documents,
* configuration files,
* Spark records,
* monitoring events,
* cloud resource metadata.

Understanding nested structures is essential for data engineering.

---

## Nested dictionaries

The most common production structure.

```python
pipeline = {
    "name": "daily_sales_etl",
    "status": "SUCCESS",
    "config": {
        "batch_size": 1000,
        "parallelism": 4
    }
}
```

Access nested values:

```python
pipeline["config"]["batch_size"]
```

Output:

```text
1000
```

---

## Nested lists

Lists can contain other lists.

```python
daily_sales = [
    [120, 140, 160],
    [180, 200, 220],
    [240, 260, 280]
]
```

Access values:

```python
daily_sales[0][1]
```

Output:

```text
140
```

Think of this as:

```text
Row 0 -> [120, 140, 160]
Row 1 -> [180, 200, 220]
Row 2 -> [240, 260, 280]
```

---

## Dictionary containing a list

Very common in configuration and API data.

```python
asset_inventory = {
    "region": "Mumbai",
    "servers": [
        "server-101",
        "server-102",
        "server-103"
    ]
}
```

Access:

```python
asset_inventory["servers"][0]
```

Output:

```text
server-101
```

---

## List containing dictionaries

One of the most important data engineering patterns.

```python
assets = [
    {"id": "server-101", "status": "ACTIVE"},
    {"id": "server-102", "status": "FAILED"},
    {"id": "server-103", "status": "ACTIVE"}
]
```

Access:

```python
assets[1]["status"]
```

Output:

```text
FAILED
```

This structure is used constantly when processing JSON records.

---

## Modifying nested objects

Nested mutable objects can be modified directly.

```python
pipeline["config"]["batch_size"] = 5000
```

Result:

```python
{
    "config": {
        "batch_size": 5000
    }
}
```

You are modifying the nested dictionary, not replacing it.

---

## Shared nested references

This is one of the most common Python bugs.

```python
shared_config = {
    "batch_size": 1000
}

pipeline_a = {
    "config": shared_config
}

pipeline_b = {
    "config": shared_config
}
```

Memory:

```text
pipeline_a

     |

     v

config -------+

              |

              v

      {batch_size: 1000}

              ^

              |

config -------+

     ^

pipeline_b
```

Updating:

```python
pipeline_a["config"]["batch_size"] = 9999
```

Changes both pipelines.

Output:

```text
pipeline_a -> 9999
pipeline_b -> 9999
```

Both dictionaries reference the same nested object.

---

## The famous nested list bug

This creates shared references.

```python
matrix = [[0] * 3] * 3
```

Memory:

```text
matrix

 |

 +----+

 |    |

 v    v

+-----------+

| [0,0,0]   |

+-----------+

 ^    ^

 |    |

 +----+
```

All rows point to the same inner list.

Updating one element:

```python
matrix[0][0] = 1
```

Result:

```text
[
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
]
```

Every row changed.

---

## Correct nested list creation

Use a comprehension.

```python
matrix = [[0] * 3 for _ in range(3)]
```

Memory:

```text
matrix

 |

 +----------+

 |          |

 v          v

[0,0,0]   [0,0,0]   [0,0,0]
```

Each row is independent.

Updating:

```python
matrix[0][0] = 1
```

Result:

```text
[
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

Only one row changes.

---

## Iterating through nested structures

List of dictionaries:

```python
for asset in assets:
    print(asset["id"], asset["status"])
```

Output:

```text
server-101 ACTIVE
server-102 FAILED
server-103 ACTIVE
```

This pattern is extremely common in ETL pipelines.

---

## Filtering nested data

Example:

```python
active_assets = []

for asset in assets:
    if asset["status"] == "ACTIVE":
        active_assets.append(asset["id"])
```

Result:

```text
[
    "server-101",
    "server-103"
]
```

This is a basic transformation operation.

---

## Tuples containing mutable objects

Tuples are immutable.

However, they can contain mutable objects.

```python
pipeline_tuple = (
    "daily_sales_etl",
    {
        "batch_size": 1000
    }
)
```

This works:

```python
pipeline_tuple[1]["batch_size"] = 2000
```

Result:

```python
(
    "daily_sales_etl",
    {
        "batch_size": 2000
    }
)
```

Why?

Because the tuple stores a reference to the dictionary.

The reference is immutable, but the dictionary is mutable.

---

## Processing nested JSON

A realistic example.

```python
events = [
    {
        "asset_id": "server-101",
        "metrics": {
            "cpu": 78,
            "memory": 65
        }
    },
    {
        "asset_id": "server-102",
        "metrics": {
            "cpu": 92,
            "memory": 81
        }
    }
]
```

Extract high CPU assets:

```python
high_cpu_assets = []

for event in events:
    if event["metrics"]["cpu"] > 80:
        high_cpu_assets.append(event["asset_id"])
```

Result:

```text
[
    "server-102"
]
```

This is very similar to processing monitoring events or API responses.

---

## Common beginner mistakes

### Mistake 1

Assuming nested objects are copied automatically.

```python
pipeline_b = pipeline_a
```

Both variables reference the same nested objects.

### Mistake 2

Using:

```python
[[0] * 3] * 3
```

This creates shared references.

### Mistake 3

Forgetting that tuples can contain mutable objects.

---

## Interview note

A concise interview answer:

> Nested data structures are collections that contain other collections. In Python, nested lists and dictionaries are reference-based, so modifying a shared nested mutable object affects every reference pointing to it. Understanding nested references is essential for safely processing JSON, API responses, and ETL data structures.
