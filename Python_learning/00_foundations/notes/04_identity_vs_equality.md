# Python identity vs equality

## What is the difference between `==` and `is`?

This is one of the most important Python interview topics.

Many beginners think `==` and `is` mean the same thing.

They do not.

* `==` compares **values**
* `is` compares **object identity**

---

## Equality (`==`)

`==` checks whether two objects contain the same value.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

The values are the same.

---

## Identity (`is`)

`is` checks whether both variables refer to the **same object in memory**.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

Although the values are identical, Python created **two different list objects**.

---

## Memory model

```python
a = [1, 2, 3]
b = [1, 2, 3]
```

Memory:

```text
a

↓

[1, 2, 3]

b

↓

[1, 2, 3]
```

Two separate objects.

---

## Same object example

```python
a = [1, 2, 3]
b = a
```

Memory:

```text
a

↓

[1, 2, 3]

↑

b
```

Now both variables point to the same object.

---

## Using `id()`

The `id()` function shows the identity of an object.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

The IDs are the same.

---

## Why this matters

Identity becomes important when working with:

* lists,
* dictionaries,
* function arguments,
* mutable objects,
* caching,
* singleton objects.

---

## The special case: `None`

Always compare `None` using `is`.

Correct:

```python
if value is None:
    print("Missing")
```

Avoid:

```python
if value == None:
    print("Missing")
```

`None` is a singleton object, so identity comparison is the recommended approach.

---

## Common beginner mistakes

### Mistake 1

Using `is` for value comparison.

```python
a = 1000
b = 1000

print(a is b)
```

This may produce unexpected results.

### Mistake 2

Using `==` when checking for `None`.

Use `is None`.

---

## Interview note

A concise interview answer:

> `==` compares the values of two objects, while `is` compares whether both variables reference the same object in memory.
