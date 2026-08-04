# Python variables and references

## What is a variable?

A variable is **not the object itself**.

A variable is a **reference (label)** that points to an object stored in memory.

For example:

```python
pipeline = "daily_sales_etl"
```

Here:

* `"daily_sales_etl"` is the object,
* `pipeline` is the reference to that object.

---

## The mental model

Think of a variable as a label attached to an object.

```text
pipeline

↓

"daily_sales_etl"
```

The variable points to the object.

---

## Creating a variable

```python
pipeline = "daily_sales_etl"
```

Python performs two steps:

1. create the string object,
2. make the variable `pipeline` refer to that object.

---

## Reassigning a variable

```python
pipeline = "daily_sales_etl"

pipeline = "customer_etl"
```

After reassignment:

```text
pipeline

↓

"customer_etl"
```

The variable now points to a different object.

The previous object is no longer referenced by `pipeline`.

---

## Multiple variables can point to the same object

```python
pipeline_a = "daily_sales_etl"

pipeline_b = pipeline_a
```

Memory model:

```text
pipeline_a

↓

"daily_sales_etl"

↑

pipeline_b
```

Both variables refer to the same object.

---

## Checking object identity

Python provides the `id()` function.

```python
pipeline_a = "daily_sales_etl"

pipeline_b = pipeline_a

print(id(pipeline_a))
print(id(pipeline_b))
```

The IDs are usually the same because both variables reference the same object.

---

## Why this matters

Understanding references is essential for:

* lists,
* dictionaries,
* function arguments,
* object mutation,
* copying,
* debugging Python programs.

---

## Common beginner mistake

Many beginners think this creates a copy:

```python
a = [1, 2, 3]

b = a
```

It does **not** create a new list.

It creates a new reference to the same list.

---

## Interview note

A concise interview answer:

> In Python, variables hold references to objects. Assignment binds a variable name to an object rather than copying the object itself.
