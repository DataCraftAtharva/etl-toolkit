# Python tuples

## What is a tuple?

A tuple is an **ordered collection of values** that **cannot be modified after creation**.

Example:

```python
pipeline = ("daily_sales_etl", "development", 2026)
```

Like lists, tuples are ordered and support indexing and slicing.

Unlike lists, tuples are **immutable**.

---

## Why tuples matter

Tuples are used when data should remain fixed.

Common examples:

* database query results,
* configuration values,
* geographic coordinates,
* date and time values,
* dictionary keys,
* function return values.

---

## Creating tuples

```python
pipeline = ("daily_sales_etl", "development", 2026)

coordinates = (19.0760, 72.8777)

record = (101, "Mumbai", 1250)
```

A tuple is created using parentheses `()`.

---

## Tuple indexing

Tuples support indexing exactly like lists.

```python
record = (101, "Mumbai", 1250)

print(record[0])

print(record[1])

print(record[-1])
```

Output:

```text
101
Mumbai
1250
```

---

## Tuple slicing

```python
record = (101, "Mumbai", 1250, "Retail")

print(record[0:2])

print(record[1:])

print(record[-2:])
```

Output:

```text
(101, 'Mumbai')
('Mumbai', 1250, 'Retail')
(1250, 'Retail')
```

---

## Tuples are immutable

This is the most important property.

```python
record = (101, "Mumbai", 1250)

record[1] = "Pune"
```

Output:

```text
TypeError
```

Python does not allow modification of tuple elements.

---

## Tuple unpacking

Tuples can be unpacked into variables.

```python
record = (101, "Mumbai", 1250)

customer_id, city, revenue = record

print(customer_id)

print(city)

print(revenue)
```

Output:

```text
101
Mumbai
1250
```

This is very common when processing records.

---

## Returning multiple values

Functions often return tuples.

```python
def get_pipeline_status():
    return "SUCCESS", 1250

status, processed_records = get_pipeline_status()
```

The function returns a tuple automatically.

---

## Single-element tuple

A common beginner mistake:

```python
value = (10)
```

This is an integer.

Correct:

```python
value = (10,)
```

The comma creates the tuple.

---

## Tuple methods

Tuples have very few methods because they are immutable.

### count()

```python
numbers = (10, 20, 20, 30)

print(numbers.count(20))
```

Output:

```text
2
```

### index()

```python
print(numbers.index(30))
```

Output:

```text
3
```

---

## Tuple vs list

| Feature               | List | Tuple                       |
| --------------------- | ---- | --------------------------- |
| Ordered               | Yes  | Yes                         |
| Mutable               | Yes  | No                          |
| Indexing              | Yes  | Yes                         |
| Slicing               | Yes  | Yes                         |
| Can be dictionary key | No   | Yes (if immutable contents) |

---

## Why tuples can be dictionary keys

Because tuples are immutable.

```python
locations = {
    (19.0760, 72.8777): "Mumbai",
    (28.6139, 77.2090): "Delhi"
}
```

Lists cannot be used as dictionary keys because they are mutable.

---

## Common beginner mistakes

### Mistake 1

Trying to modify a tuple.

```python
record[0] = 102
```

This raises a `TypeError`.

### Mistake 2

Forgetting the comma in a single-element tuple.

```python
(10)
```

This is not a tuple.

---

## Interview note

A concise interview answer:

> A tuple is an ordered immutable collection. It supports indexing and slicing, is commonly used for fixed data and multiple return values, and can be used as a dictionary key because it is immutable.
> 
> The interview-level summary question: [-1] returns the last element; [-1:] returns a new list/tuple containing the last element and never raises IndexError for an empty sequence.