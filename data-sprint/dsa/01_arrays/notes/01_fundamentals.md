# Arrays — Day 01 Fundamentals

## Why arrays matter

Arrays are one of the most important data structures in DSA.

A large number of interview problems begin with an array and require you to:

- access elements
- update elements
- add elements
- remove elements
- search elements
- traverse elements
- calculate values
- identify maximum/minimum values
- count elements matching a condition

For Python, the closest general-purpose structure to a traditional interview array is the `list`.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

---

# 1. Array Indexing

Python lists use **zero-based indexing**.

```python
numbers = [10, 20, 30, 40, 50]
```

The indexes are:

```text
index:     0    1    2    3    4
value:    10   20   30   40   50
```

Therefore:

```python
numbers[0]
```

returns:

```text
10
```

and:

```python
numbers[3]
```

returns:

```text
40
```

---

# 2. Access an Element

Access an element using its index.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

## Negative indexing

Python also supports negative indexes.

```python
numbers[-1]
```

returns the last element:

```text
50
```

The mental model:

```text
Positive indexes

0    1    2    3    4
↓    ↓    ↓    ↓    ↓
10   20   30   40   50


Negative indexes

-5   -4   -3   -2   -1
 ↓    ↓    ↓    ↓    ↓
10   20   30   40   50
```

---

# 3. Update an Element

Lists are mutable.

You can replace an element using its index.

```python
numbers = [10, 20, 30, 40, 50]

numbers[2] = 45

print(numbers)
```

Output:

```text
[10, 20, 45, 40, 50]
```

Mental model:

```text
Before:

10  20  30  40  50
        ↑
       index 2


After:

10  20  45  40  50
        ↑
      updated
```

---

# 4. Insert an Element

Use `insert(index, value)`.

```python
numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 25)

print(numbers)
```

Output:

```text
[10, 20, 25, 30, 40, 50]
```

The existing elements after the insertion position are shifted.

```text
Before:

10  20  30  40  50
        ↑
      index 2


Insert 25:

10  20  25  30  40  50
```

---

# 5. Append an Element

Use `append()` to add an element to the end.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

This is one of the most common list operations.

---

# 6. Remove an Element

There are multiple ways to remove elements.

## Remove by value

Use:

```python
numbers.remove(30)
```

Example:

```python
numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)
```

Output:

```text
[10, 20, 40]
```

`remove()` removes the **first matching value**.

---

## Delete by index

Use `del`.

```python
numbers = [10, 20, 30, 40]

del numbers[2]

print(numbers)
```

Output:

```text
[10, 20, 40]
```

Here we removed the element at index `2`.

---

# 7. Traversal

Traversal means visiting elements one by one.

The simplest approach is:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
50
```

Mental model:

```text
10 → 20 → 30 → 40 → 50
```

This is called **value-based traversal**.

---

# 8. Find Maximum

A common array problem is finding the largest value.

Instead of immediately using:

```python
max(numbers)
```

we should understand the traversal logic.

```python
numbers = [10, 20, 30, 40, 50]

max_element = numbers[0]

for number in numbers:
    if number > max_element:
        max_element = number

print(max_element)
```

Execution:

```text
Initial:
max_element = 10

20 > 10 → max = 20

30 > 20 → max = 30

40 > 30 → max = 40

50 > 40 → max = 50
```

Final:

```text
50
```

### Pattern

```text
Start with first element
        ↓
Compare each element
        ↓
Replace maximum when a larger value is found
```

---

# 9. Find Minimum

The same idea can be used for the minimum.

```python
numbers = [10, 20, 30, 40, 50]

min_element = numbers[0]

for number in numbers:
    if number < min_element:
        min_element = number

print(min_element)
```

Output:

```text
10
```

Mental model:

```text
Start with first element
        ↓
Compare each element
        ↓
Replace minimum when a smaller value is found
```

---

# 10. Count Occurrences

Suppose we want to count how many times a target value appears.

```python
numbers = [10, 20, 10, 30, 10, 40]

target = 10

count = 0

for number in numbers:
    if number == target:
        count += 1

print(count)
```

Output:

```text
3
```

Mental model:

```text
count = 0

10 → match → count = 1
20 → no
10 → match → count = 2
30 → no
10 → match → count = 3
40 → no
```

This is a fundamental **counting pattern**.

---

# 11. Calculate Sum

We can calculate the sum by maintaining an accumulator.

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print(total)
```

Output:

```text
150
```

Mental model:

```text
total = 0

+10 → 10
+20 → 30
+30 → 60
+40 → 100
+50 → 150
```

This is called an **accumulator pattern**.

---

# 12. The Three Important Traversal Patterns

The problems we solved already introduce three very important patterns.

## Pattern 1 — Visit every element

```python
for number in numbers:
    print(number)
```

Used for:

- processing every element
- validation
- transformation
- inspection

---

## Pattern 2 — Track a value

```python
best = numbers[0]

for number in numbers:
    if number > best:
        best = number
```

Used for:

- maximum
- minimum
- highest price
- lowest price
- largest transaction

---

## Pattern 3 — Accumulate a result

```python
total = 0

for number in numbers:
    total += number
```

Used for:

- sum
- count
- totals
- metrics

---

# 13. Array Operation Mental Model

For now, remember the practical behavior.

| Operation | Example |
|---|---|
| Access | `numbers[index]` |
| Update | `numbers[index] = value` |
| Append | `numbers.append(value)` |
| Insert | `numbers.insert(index, value)` |
| Remove by value | `numbers.remove(value)` |
| Delete by index | `del numbers[index]` |
| Traversal | `for number in numbers` |

We will learn the exact complexity of these operations in the dedicated complexity/fundamentals section.

---

# 14. Important Edge Cases

When solving array problems, don't assume the input is always perfect.

Think about:

### Empty array

```python
numbers = []
```

For example, this is unsafe:

```python
max_element = numbers[0]
```

because there is no index `0`.

---

### One-element array

```python
numbers = [10]
```

Maximum and minimum are both:

```text
10
```

---

### Duplicate values

```python
numbers = [10, 20, 20, 30]
```

There can be multiple occurrences of the same value.

---

### Negative values

```python
numbers = [-10, -5, -20]
```

The maximum is:

```text
-5
```

The minimum is:

```text
-20
```

---

# 15. Interview Thinking

Before solving an array problem, ask:

```text
1. What is the input?
        ↓
2. What does n represent?
        ↓
3. What exactly is the required output?
        ↓
4. Do I need to traverse the array?
        ↓
5. Do I need to track something?
        ↓
6. Do I need an accumulator?
        ↓
7. Can I stop early?
        ↓
8. What are the edge cases?
```

Don't immediately jump to built-in functions.

First understand the underlying algorithm.

---

# 16. What We Practiced

Day 01 covered:

- [x] Access an element
- [x] Update an element
- [x] Insert an element
- [x] Delete an element
- [x] Append an element
- [x] Remove an element
- [x] Traverse an array
- [x] Find maximum
- [x] Find minimum
- [x] Count occurrences
- [x] Calculate sum

---

# 17. Current Learning Strategy

At this stage, focus on **implementation first**.

Do not try to memorize every complexity detail immediately.

The learning sequence is:

```text
Understand the operation
        ↓
Implement it manually
        ↓
Understand the traversal
        ↓
Solve basic problems
        ↓
Analyze complexity
        ↓
Learn optimization patterns
```

Later we will connect these fundamentals to:

```text
Arrays
   ↓
Two Pointers
   ↓
Sliding Window
   ↓
Hashing
   ↓
Prefix Sum
   ↓
Top K
   ↓
Interview Problems
```

---

# Key Takeaways

```text
Array
  ↓
Indexed collection

Access
  ↓
numbers[index]

Update
  ↓
numbers[index] = value

Insert
  ↓
numbers.insert(index, value)

Append
  ↓
numbers.append(value)

Remove
  ↓
numbers.remove(value)

Delete by index
  ↓
del numbers[index]

Traversal
  ↓
for number in numbers

Maximum
  ↓
Track the largest value

Minimum
  ↓
Track the smallest value

Count
  ↓
Accumulator + condition

Sum
  ↓
Accumulator
```

The most important skill from Day 01 is:

> **Given an array problem, recognize that a simple traversal plus the right tracking/accumulator logic can solve it.**