# Big-O complexity

## Why this matters

In a DSA interview, getting the correct answer is only part of the solution.

You should also be able to explain:

* How fast does the solution grow with input size?
* How much additional memory does it need?
* Why is one approach better than another?
* Will it still work when the input becomes very large?

Big-O gives us a way to describe this growth.

---

# The mental model

Think of one question:

> **As the input size grows, how much more work does my algorithm do?**

Usually:

```text
n = input size
```

Examples:

* Array → `n = number of elements`
* String → `n = number of characters`
* Records → `n = number of records`

The goal is not the exact runtime.

The goal is understanding how the work **scales**.

---

# Complexity levels to know

| Complexity     | Mental model                           | Typical example    |
| -------------- | -------------------------------------- | ------------------ |
| **O(1)**       | Same amount of work                    | Array index access |
| **O(log n)**   | Keep reducing the problem              | Binary search      |
| **O(n)**       | One pass through data                  | Linear search      |
| **O(n log n)** | Efficient sorting / divide and conquer | Merge sort         |
| **O(n²)**      | Compare many pairs                     | Nested loops       |
| **O(2ⁿ)**      | Explore combinations                   | Generate subsets   |
| **O(n!)**      | Explore permutations                   | All permutations   |

For interview preparation, these are the most important complexity classes.

---

# How to calculate time complexity

## One loop → O(n)

```python
for value in numbers:
    process(value)
```

If there are `n` elements, the loop runs `n` times.

**Time complexity:** `O(n)`

---

## Nested loops → O(n²)

```python
for x in numbers:
    for y in numbers:
        process(x, y)
```

The outer loop runs `n` times.

The inner loop runs `n` times for each outer iteration.

```text
n × n = n²
```

**Time complexity:** `O(n²)`

---

## Sequential loops → O(n)

```python
for x in numbers:
    process(x)

for y in numbers:
    process(y)
```

Total work:

```text
n + n = 2n
```

Big-O ignores constant factors.

**Time complexity:** `O(n)`

---

## Different input sizes → O(n + m)

```python
for x in first:
    process(x)

for y in second:
    process(y)
```

If:

* `n = len(first)`
* `m = len(second)`

Then:

**Time complexity:** `O(n + m)`

Use this when the two inputs are independent.

---

## Different input sizes with nesting → O(n × m)

```python
for x in first:
    for y in second:
        process(x, y)
```

**Time complexity:** `O(n × m)`

This is common in:

* joins
* comparing datasets
* combining large collections

---

# Recognizing O(log n)

Look for repeated reduction of the problem size.

```python
while n > 1:
    n //= 2
```

The sequence becomes:

```text
n
n/2
n/4
n/8
n/16
...
```

So the number of iterations grows logarithmically.

**Time complexity:** `O(log n)`

The classic example is **binary search**.

---

# Best, average, and worst case

Example: linear search.

```python
for value in numbers:
    if value == target:
        return True
```

### Best case

Target is the first element.

**O(1)**

### Worst case

Target is the last element or missing.

**O(n)**

In interviews, clearly state which case you are discussing.

---

# Space complexity

Time asks:

> How much work does the algorithm do?

Space asks:

> How much additional memory does the algorithm use?

Example:

```python
seen = set()

for value in numbers:
    seen.add(value)
```

The set can contain up to `n` values.

* **Time:** `O(n)`
* **Space:** `O(n)`

Compare with:

```python
total = 0

for value in numbers:
    total += value
```

* **Time:** `O(n)`
* **Space:** `O(1)`

Focus on **auxiliary space** (extra memory created by the algorithm).

---

# The first optimization pattern

A common interview transformation:

```text
Brute force
     ↓
Repeated search
     ↓
Use a better data structure
     ↓
Faster lookup
```

### Brute force

Check every pair.

* **Time:** `O(n²)`

### Optimized

Store previously seen values in a hash set or hash map.

* **Time:** `O(n)` (expected)
* **Space:** `O(n)`

This is the classic **time vs space trade-off**.

---

# Input constraints tell you what is realistic

Suppose:

```text
n = 10
```

An `O(n²)` solution performs about **100 operations**, which is fine.

Now suppose:

```text
n = 100,000
```

Then:

```text
n² = 10,000,000,000
```

That should immediately make you question an `O(n²)` approach.

Always ask:

* What is `n`?
* What are the constraints?

---

# Data engineering connection

In data engineering, `n` may represent:

* rows
* events
* records
* files
* keys

A pipeline processing **100 million records** makes complexity important.

An `O(n²)` operation is often impractical.

At scale, performance also depends on:

* CPU
* memory
* disk I/O
* network I/O
* shuffle
* partitioning
* data skew
* file count

For Spark, think:

```text
Algorithmic complexity
+
Distributed execution cost
```

---

# Common mistakes

## Mistake 1: Counting lines of code

Wrong:

```text
10 lines of code = O(10)
```

Complexity depends on how operations grow with input size.

---

## Mistake 2: Assuming two loops means O(n²)

Not always.

Sequential loops are often `O(n)`.

---

## Mistake 3: Ignoring multiple input sizes

`O(n + m)` is different from `O(n)` when the inputs are independent.

---

## Mistake 4: Ignoring extra memory

These are different:

* `O(n)` time + `O(1)` space
* `O(n)` time + `O(n)` space

---

# Interview checklist

For every DSA problem, ask:

1. What is the input?
2. What does `n` represent?
3. What are the constraints?
4. What is the brute-force approach?
5. What makes it expensive?
6. Which pattern or data structure removes the bottleneck?
7. What is the time complexity?
8. What is the auxiliary space?
9. What are the edge cases?

---

# Interview answer template

A strong answer sounds like this:

> The input size is `n`. The algorithm scans the input once, so the time complexity is `O(n)`. It uses a hash map containing up to `n` elements, so the auxiliary space is `O(n)`. We trade memory for faster lookup.

---

# What to remember

```text
O(1)       → constant
O(log n)   → repeatedly reduce the problem
O(n)       → one pass
O(n log n) → efficient sorting / divide and conquer
O(n²)      → pairwise comparisons
O(2ⁿ)      → combinations
O(n!)      → permutations
```

The key skill is not memorizing the list.

The key skill is being able to look at code and explain:

> **Why is this the time complexity?**

---

# Further depth

These topics are intentionally excluded from the core note and should be learned later when they become useful:

* amortized complexity
* recursion complexity
* recurrence relations
* tight bounds
* average-case analysis
* Master theorem
* distributed algorithm cost
