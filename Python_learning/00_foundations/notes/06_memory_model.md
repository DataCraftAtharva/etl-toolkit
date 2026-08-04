# Python memory model

## What is the Python memory model?

The Python memory model explains **how objects are created, stored, referenced, and removed from memory** while a program is running.

The most important idea is:

**Variables do not store values directly. Variables store references to objects.**

Everything in Python is an object.

---

## The mental model

When Python executes:

```python
pipeline = "daily_sales_etl"
```

Python creates a string object in memory and makes the variable `pipeline` refer to it.

```text
Variable           Memory

pipeline --------> "daily_sales_etl"
```

The variable points to the object.

---

## Creating multiple references

```python
pipeline_a = "daily_sales_etl"
pipeline_b = pipeline_a
```

Memory:

```text
pipeline_a -----

                 ↓

           "daily_sales_etl"

                 ↑

pipeline_b -----
```

Both variables point to the same object.

---

## Reassignment

```python
pipeline = "daily_sales_etl"

pipeline = "customer_etl"
```

Memory before:

```text
pipeline

↓

"daily_sales_etl"
```

Memory after:

```text
pipeline

↓

"customer_etl"
```

The variable now points to a new object.

The previous object is no longer referenced by `pipeline`.

---

## Mutable objects in memory

```python
numbers = [10, 20]

backup = numbers
```

Memory:

```text
numbers -----

              ↓

           [10, 20]

              ↑

backup  -----
```

If we execute:

```python
numbers.append(30)
```

Memory becomes:

```text
numbers -----

              ↓

        [10, 20, 30]

              ↑

backup  -----
```

The list object changed.

Both variables see the modification.

---

## Immutable objects in memory

```python
text = "ETL"

backup = text

text = text + " Pipeline"
```

Memory before:

```text
text -----

          ↓

        "ETL"

          ↑

backup -----
```

Memory after:

```text
text

↓

"ETL Pipeline"


backup

↓

"ETL"
```

A new string object was created.

The original string object remained unchanged.

---

## Object identity

Python provides `id()` to inspect object identity.

```python
a = [1, 2]

b = a

print(id(a))

print(id(b))
```

The IDs are the same because both variables reference the same object.

If a new object is created, the ID changes.

---

## Garbage collection

What happens to an object that is no longer referenced?

Example:

```python
pipeline = "daily_sales_etl"

pipeline = "customer_etl"
```

The original string object may become **unreferenced**.

Python automatically frees such objects through **garbage collection**.

Simplified view:

```text
Before reassignment:

pipeline

↓

"daily_sales_etl"


After reassignment:

pipeline

↓

"customer_etl"


"daily_sales_etl" has no references

↓

Garbage collector removes it
```

Python automatically manages memory, so developers usually do not free memory manually.

---

## Why this matters

The memory model explains:

* variable assignment,
* mutability,
* copying,
* function arguments,
* object sharing,
* identity vs equality,
* unexpected list and dictionary modifications.

Many real ETL bugs occur because multiple variables reference the same mutable object.

---

## Common beginner mistakes

### Mistake 1

Thinking assignment creates a copy.

```python
a = [1, 2]

b = a
```

This creates a new reference, not a new list.

### Mistake 2

Expecting immutable objects to change in place.

Strings create new objects.

---

## Interview note

A concise interview answer:

> Python variables hold references to objects stored in memory. Assignment creates references, mutable objects can change in place, immutable objects create new objects when modified, and unreferenced objects are automatically removed by Python’s garbage collector.
