# Python sets

## What is a set?

A set is a **collection of unique values**.

Unlike lists, sets do not store duplicate elements.

Example:

```python
processed_assets = {
    "server-101",
    "server-102",
    "server-103"
}
```

Memory concept:

```text
processed_assets

       |

       v

{server-101, server-102, server-103}
```

The order of elements is not guaranteed.

---

## Why sets matter

Sets are extremely important in Python because they provide:

* fast membership checking,
* duplicate removal,
* set operations,
* efficient filtering,
* lookup optimization.

In data engineering, sets are commonly used for:

* deduplication,
* incremental processing,
* asset filtering,
* ID validation,
* join optimization,
* cache lookups.

---

## Creating sets

Using curly braces:

```python
processed_assets = {
    "server-101",
    "server-102",
    "server-103"
}
```

Or using the constructor:

```python
processed_assets = set(["server-101", "server-102"])
```

An empty set must be created with:

```python
empty_set = set()
```

Do **not** use:

```python
empty = {}
```

because `{}` creates an empty dictionary.

---

## Sets automatically remove duplicates

This is one of the most useful production features.

```python
incoming_assets = [
    "server-101",
    "server-102",
    "server-101",
    "server-103"
]

unique_assets = set(incoming_assets)
```

Result:

```text
{server-101, server-102, server-103}
```

Duplicates are removed automatically.

A very common ETL pattern:

```python
unique_records = set(raw_records)
```

---

## Membership testing

Sets are optimized for lookup.

```python
"server-101" in processed_assets
```

Output:

```text
True
```

This is significantly faster than checking membership in a list for large datasets.

Example:

```python
if asset_id in processed_assets:
    skip_processing()
```

This pattern is used constantly in data pipelines.

---

## Adding elements

### add()

```python
processed_assets.add("server-104")
```

Result:

```text
{server-101, server-102, server-103, server-104}
```

If the element already exists, nothing changes.

---

## Adding multiple elements

### update()

```python
processed_assets.update([
    "server-105",
    "server-106"
])
```

Result:

```text
{
    server-101,
    server-102,
    server-103,
    server-104,
    server-105,
    server-106
}
```

`update()` accepts any iterable.

---

## Removing elements

### remove()

```python
processed_assets.remove("server-106")
```

Removes the element.

If the element is missing:

```python
processed_assets.remove("server-999")
```

Output:

```text
KeyError
```

### discard()

```python
processed_assets.discard("server-999")
```

No error is raised.

In production code, `discard()` is often safer.

---

## Union

Union combines all unique elements.

```python
batch_1 = {"server-101", "server-102"}
batch_2 = {"server-102", "server-103"}

all_assets = batch_1 | batch_2
```

Result:

```text
{
    server-101,
    server-102,
    server-103
}
```

Equivalent:

```python
batch_1.union(batch_2)
```

---

## Intersection

Intersection returns common elements.

```python
batch_1 & batch_2
```

Result:

```text
{server-102}
```

Useful for:

* finding overlapping records,
* validating processed data,
* comparing batches.

---

## Difference

Difference returns elements present in the first set only.

```python
batch_2 - batch_1
```

Result:

```text
{server-103}
```

Very useful for incremental processing.

Example:

```python
new_assets = incoming_assets - processed_assets
```

Only new assets are processed.

---

## Symmetric difference

Returns elements present in exactly one set.

```python
batch_1 ^ batch_2
```

Result:

```text
{
    server-101,
    server-103
}
```

Useful for detecting changes between snapshots.

---

## Set operations summary

| Operation            | Symbol | Meaning                     |                     |
| -------------------- | ------ | --------------------------- | ------------------- |
| Union                | `      | `                           | All unique elements |
| Intersection         | `&`    | Common elements             |                     |
| Difference           | `-`    | Elements in first set only  |                     |
| Symmetric difference | `^`    | Elements in exactly one set |                     |

---

## Why sets are fast

Python sets are implemented using **hash tables**.

When you insert an element:

```python
processed_assets.add("server-101")
```

Python computes a hash value.

Simplified idea:

```text
"server-101"

     |

     v

hash()

     |

     v

bucket location
```

Membership checking uses the hash to locate elements quickly.

This is why:

```python
asset_id in processed_assets
```

is typically **O(1)** average time.

---

## Hashable objects

Set elements must be **hashable**.

Hashable objects are immutable.

Allowed:

```python
{
    "server-101",
    100,
    (1, 2)
}
```

Not allowed:

```python
{[1, 2]}
```

Output:

```text
TypeError: unhashable type: 'list'
```

Lists are mutable, so Python cannot safely hash them.

---

## Set memory model

Sets are mutable.

Example:

```python
original_assets = {"server-101"}

backup_assets = original_assets
```

Memory:

```text
original_assets ----

                    |

                    v

              {server-101}

                    ^

                    |

backup_assets ------
```

Updating one reference:

```python
backup_assets.add("server-102")
```

Result:

```python
original_assets
```

Output:

```text
{
    server-101,
    server-102
}
```

Both variables reference the same set.

---

## Copying sets

To create an independent copy:

```python
backup_assets = original_assets.copy()
```

Now the sets are separate.

---

## Common beginner mistakes

### Mistake 1

Using `{}` for an empty set.

```python
empty = {}
```

This creates a dictionary.

Correct:

```python
empty = set()
```

### Mistake 2

Expecting order.

```python
assets = {"A", "B", "C"}
```

Output order may vary.

### Mistake 3

Storing mutable objects.

```python
{[1, 2]}
```

Raises `TypeError`.

---

## Production example

Suppose an ETL pipeline receives duplicate asset IDs.

```python
asset_stream = [
    "asset-001",
    "asset-002",
    "asset-001",
    "asset-003"
]
```

Deduplicate before processing:

```python
unique_assets = set(asset_stream)

for asset in unique_assets:
    process(asset)
```

Benefits:

* no duplicate processing,
* lower compute cost,
* faster execution,
* simpler logic.

This is one of the most common real-world uses of sets.

---

## Interview note

A concise interview answer:

> A set is a mutable collection of unique hashable elements implemented using a hash table. It provides fast membership testing, automatic duplicate removal, and efficient union, intersection, and difference operations, making it ideal for deduplication and lookup optimization.
