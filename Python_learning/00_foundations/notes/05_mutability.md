# Python mutability

## What is mutability?

Mutability means **whether an object can be changed after it is created**.

There are two categories of Python objects:

* **Mutable objects** → can be modified.
* **Immutable objects** → cannot be modified.

Examples:

| Type       | Mutable? |
| ---------- | -------- |
| list       | Yes      |
| dictionary | Yes      |
| set        | Yes      |
| string     | No       |
| tuple      | No       |
| integer    | No       |

---

## The core idea

Variables point to objects.

When multiple variables point to the same **mutable object**, changing the object through one variable affects all references.

Example:

```python
numbers = [10, 20, 30]

backup = numbers
```

Memory:

```text
numbers
   ↓
[10, 20, 30]
   ↑
backup
```

Both variables point to the same list.

---

## Modifying a mutable object

```python
numbers.append(40)
```

Result:

```python
print(numbers)
print(backup)
```

Output:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

The list changed.

Both variables see the change because they reference the same object.

---

## Immutable objects

Strings cannot be modified.

Example:

```python
text = "ETL"

text = text + " Pipeline"
```

Python creates a **new string object**.

Memory before:

```text
text
 ↓
"ETL"
```

Memory after:

```text
text
 ↓
"ETL Pipeline"
```

The original string was not modified.

---

## Why this happens

Mutable operations change the existing object.

Immutable operations create a new object.

This is why:

```python
a = [1, 2]
b = a

a.append(3)
```

changes both variables.

But:

```python
a = "ETL"
b = a

a = a + " Pipeline"
```

does not change `b`.

---

## The most common Python bug

```python
config = {
    "environment": "dev",
    "retry": 3
}

backup = config

backup["retry"] = 5
```

Many beginners expect only `backup` to change.

Actual result:

```python
print(config)
```

Output:

```text
{'environment': 'dev', 'retry': 5}
```

Both variables changed because they reference the same dictionary.

---

## How to create a copy

For lists:

```python
copy_numbers = numbers.copy()
```

Now the variables point to different objects.

Memory:

```text
numbers
 ↓
[10, 20, 30]

copy_numbers
 ↓
[10, 20, 30]
```

Changes to one list do not affect the other.

---

## Why this matters

Mutability affects:

* function arguments,
* list processing,
* dictionary updates,
* configuration management,
* ETL transformations,
* Pandas and PySpark operations.

---

## Interview note

A concise interview answer:

> Mutable objects can be modified after creation, while immutable objects cannot. Variables hold references to objects, so multiple variables can reference the same mutable object, causing changes through one reference to appear through the others.
