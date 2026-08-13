# Arrays

## Why this matters

Arrays are one of the most important data structures in DSA.

A large portion of interview problems are ultimately based on:

* traversing data
* accessing elements
* searching
* modifying elements
* comparing elements
* rearranging elements
* finding subarrays
* using two pointers
* using sliding windows

For data roles, this thinking also maps directly to:

* rows of data
* batches
* records
* in-memory collections
* columnar data concepts

In Python, the closest common structure to an array is `list`.

---

# What is an array?

An array stores multiple values in an ordered sequence.

Conceptually:

```text
index
  0    1    2    3    4
  ↓    ↓    ↓    ↓    ↓
[10] [20] [30] [40] [50]
```

Each element has an index.

Python:

```python
numbers = [10, 20, 30, 40, 50]
```

Access:

```python
numbers[0]   # 10
numbers[3]   # 40
```

The important property for DSA is:

> Accessing an element by index is fast.

---

# Python lists are dynamic arrays

A Python `list` behaves like a dynamic array.

This means:

```text
Array
  ↓
stores elements in an ordered structure
  ↓
supports index-based access
  ↓
can grow and shrink
```

Unlike a fixed-size array in lower-level languages, Python lists can dynamically resize.

For interview purposes, remember:

```text
list[index]
→ O(1) average / direct access
```

---

# Core array operations

| Operation             | Typical complexity |
| --------------------- | ------------------ |
| Access by index       | `O(1)`             |
| Update by index       | `O(1)`             |
| Search by value       | `O(n)`             |
| Append at end         | `O(1)` amortized   |
| Insert at beginning   | `O(n)`             |
| Insert in middle      | `O(n)`             |
| Delete from beginning | `O(n)`             |
| Delete from middle    | `O(n)`             |
| Delete from end       | `O(1)` amortized   |
| Traverse              | `O(n)`             |

The key idea:

```text
Fast at the end
Slow when elements must be shifted
```

---

# Access by index — O(1)

```python
numbers = [10, 20, 30, 40, 50]

value = numbers[3]
```

The list does not need to scan:

```text
10 → 20 → 30 → 40
```

It can directly access the indexed position.

* **Time:** `O(1)`
* **Space:** `O(1)`

This is one of the main reasons arrays are useful.

---

# Updating by index — O(1)

```python
numbers[2] = 100
```

The element at index `2` can be replaced directly.

```text
Before:
[10, 20, 30, 40]

After:
[10, 20, 100, 40]
```

* **Time:** `O(1)`
* **Auxiliary space:** `O(1)`

---

# Searching by value — O(n)

```python
numbers = [10, 20, 30, 40, 50]

30 in numbers
```

Python may need to check elements one by one:

```text
10 → no
20 → no
30 → yes
```

Worst case:

* target is the last element

* target does not exist

* **Time:** `O(n)`

This is linear search.

---

# Append — O(1) amortized

```python
numbers.append(60)
```

Usually the element is added at the end.

* **Time:** `O(1)` amortized

## Why amortized?

Sometimes the underlying dynamic array must resize.

That resize can require moving existing elements.

A single append can occasionally be expensive, but across many append operations, the average cost remains `O(1)`.

---

# Insert at the beginning — O(n)

```python
numbers = [10, 20, 30, 40]
numbers.insert(0, 5)
```

The existing elements must shift.

```text
Before:
[10][20][30][40]

After:
[5][10][20][30][40]
```

* **Time:** `O(n)`

---

# Insert in the middle — O(n)

```python
numbers.insert(2, 25)
```

Elements after index `2` may need to shift.

* **Time:** `O(n)`

---

# Delete from the beginning — O(n)

```python
numbers.pop(0)
```

After removing the first element, all remaining elements shift left.

```text
Before:
[10][20][30][40]

After:
[20][30][40]
```

* **Time:** `O(n)`

---

# Delete from the end — O(1) amortized

```python
numbers.pop()
```

The last element can be removed without shifting the others.

* **Time:** `O(1)` amortized

A useful pattern:

```text
End of array
→ usually cheap

Beginning/middle
→ potentially expensive
```

---

# Traversal — O(n)

```python
for number in numbers:
    print(number)
```

Every element must be visited.

* **Time:** `O(n)`
* **Auxiliary space:** `O(1)`

---

# In-place array modification

```python
for index in range(len(numbers)):
    numbers[index] *= 2
```

The original list is modified.

* **Time:** `O(n)`
* **Auxiliary space:** `O(1)`

Important interview question:

> Can I modify the existing structure instead of creating another one?

---

# Copying an array

```python
new_numbers = numbers.copy()
```

A new collection containing `n` elements is created.

* **Time:** `O(n)`
* **Space:** `O(n)`

This is different from an in-place modification.

---

# Array problems usually involve these operations

When you see an array problem, identify what it is asking you to do.

Common operations:

* access
* search
* count
* modify
* insert
* delete
* compare
* rearrange
* find pairs
* find subarrays
* find maximum/minimum
* find duplicates

Then ask:

* Can I solve this with one pass?
* Can I use hashing?
* Can I use two pointers?
* Can I use a sliding window?
* Can I use prefix sums?
* Do I need sorting?

These questions bridge basic arrays and interview patterns.

---

# Common array interview patterns

## Hashing

Used for:

* duplicate detection
* frequency counting
* fast lookup
* two-sum style problems

Typical complexity:

* **Time:** `O(n)` expected
* **Space:** `O(n)`

---

## Two pointers

Used for:

* sorted arrays
* pairs
* palindromes
* in-place rearrangement

Typical complexity:

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## Sliding window

Used for:

* contiguous subarrays
* longest/shortest ranges
* maximum/minimum window

Typical complexity:

* **Time:** `O(n)`

---

## Prefix sum

Used for:

* repeated range-sum queries
* subarray sum problems
* cumulative information

Usually:

* preprocessing: `O(n)`
* range query: `O(1)`

---

# Array problem recognition

### Find a pair

Think:

* hashing
* two pointers

### Find duplicates

Think:

* set
* hash map

### Find the longest subarray

Think:

* sliding window
* prefix sum
* hashing

### Array is sorted

Think:

* two pointers
* binary search

### Modify without an extra array

Think:

* in-place
* two pointers

This is how we transition from data structures to pattern recognition.

---

# Industry / data-engineering connection

Arrays appear conceptually everywhere in data systems.

Examples:

* batches of records
* lists of IDs
* lists of events
* partition contents
* in-memory processing

Large-scale systems often use more specialized structures such as:

* DataFrames
* columnar storage
* Arrow arrays
* NumPy arrays
* Spark partitions

The underlying questions remain the same:

* How is the data stored?
* Can we access it efficiently?
* Are we copying it?
* How much memory does it use?
* How much work is required to process it?

---

# Common mistakes

## Mistake 1: Assuming every list operation is O(1)

For example:

```python
numbers.insert(0, value)
```

is **O(n)** because elements may need to shift.

---

## Mistake 2: Confusing value search with index access

```python
numbers[500]
```

* **O(1)**

But:

```python
500 in numbers
```

* **O(n)** worst case

---

## Mistake 3: Creating unnecessary copies

```python
new_list = old_list.copy()
```

uses `O(n)` additional memory.

---

## Mistake 4: Ignoring whether the array is sorted

A sorted array enables:

* binary search
* two pointers

and can significantly improve a solution.

---

# Interview checklist

Before coding an array problem, ask:

1. Is the array sorted?
2. Do I need index access?
3. Do I need fast lookup?
4. Is extra memory allowed?
5. Can I modify the array in place?
6. Is the problem about pairs?
7. Is it about a contiguous subarray?
8. Do I need to preserve order?
9. What is the required time complexity?
10. What happens with empty or single-element input?

---

# What to remember

```text
Index access      → O(1)
Index update      → O(1)

Search by value   → O(n)

Append            → O(1) amortized
Pop from end      → O(1) amortized

Insert beginning  → O(n)
Insert middle     → O(n)

Delete beginning  → O(n)
Delete middle     → O(n)

Traversal         → O(n)

Copy              → O(n) space
In-place update   → O(1) auxiliary space
```

The most important mental model:

```text
Array
  ↓
Fast random access
  ↓
Expensive shifting
```

When analyzing an array algorithm, first identify **how elements are accessed**, **whether elements are shifted**, and **whether additional memory is being created**.
