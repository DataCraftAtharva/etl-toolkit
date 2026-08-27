# Arrays — Day 02 Traversal & Basic Problems

## Why this matters

Most beginner and intermediate array interview problems are built on one fundamental operation:

> **Traverse the array and maintain the required state.**

The state might be:

- a counter
- a sum
- a maximum
- a minimum
- an index
- a Boolean flag
- a result collection

The goal is to become comfortable recognizing which traversal pattern a problem requires.

---

# 1. Forward Traversal

Forward traversal processes elements from the first element to the last.

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Execution:

```text
10
20
30
40
50
```

Mental model:

```text
first
  ↓
second
  ↓
third
  ↓
...
  ↓
last
```

This is the most common array traversal pattern.

---

# 2. Value-Based Traversal

When you only need the values, iterate directly over the array.

```python
for number in numbers:
    print(number)
```

Use this when you don't need the index.

Examples:

```python
for number in numbers:
    if number > 0:
        ...
```

```python
for number in numbers:
    total += number
```

---

# 3. Index-Based Traversal

When the index is required, use `range()`.

```python
numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers)):
    print(index, numbers[index])
```

Output:

```text
0 10
1 20
2 30
3 40
4 50
```

Mental model:

```text
index
  ↓
numbers[index]
  ↓
value
```

Use index-based traversal when you need to:

- modify elements
- compare neighboring elements
- work with positions
- access multiple positions

---

# 4. Traversal Using enumerate()

When you need both the index and value, `enumerate()` is usually cleaner.

```python
for index, number in enumerate(numbers):
    print(index, number)
```

Output:

```text
0 10
1 20
2 30
3 40
4 50
```

Instead of:

```python
for index in range(len(numbers)):
    number = numbers[index]
```

prefer:

```python
for index, number in enumerate(numbers):
    ...
```

when both index and value are required.

---

# 5. Reverse Traversal

Reverse traversal processes an array from the last element to the first.

```python
numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])
```

Output:

```text
50
40
30
20
10
```

Understand the `range()`:

```python
range(4, -1, -1)
```

produces:

```text
4
3
2
1
0
```

Therefore:

```python
numbers[4] → 50
numbers[3] → 40
numbers[2] → 30
numbers[1] → 20
numbers[0] → 10
```

### Important distinction

This is **reverse traversal**.

It does not modify the original array.

```python
numbers
```

is still:

```text
[10, 20, 30, 40, 50]
```

We are simply processing it from right to left.

---

# 6. Traversal With a Condition

A very common pattern is:

```python
for number in numbers:
    if condition:
        ...
```

Example:

```python
numbers = [-5, 10, -2, 30, 0, 15]

for number in numbers:
    if number > 0:
        print(number)
```

Output:

```text
10
30
15
```

Mental model:

```text
Traverse
   ↓
Check condition
   ↓
Process matching elements
```

This pattern is the foundation of filtering.

---

# 7. Traversal With an Accumulator

An accumulator stores a result while the array is being processed.

Example:

```python
total = 0

for number in numbers:
    total += number
```

The variable changes during traversal.

Common accumulators:

```text
count
total
maximum
minimum
result
found
```

---

# 8. Find Maximum

```python
numbers = [10, 20, 30, 40, 50]

max_element = numbers[0]

for number in numbers:
    if number > max_element:
        max_element = number

print(max_element)
```

Mental model:

```text
Start
  ↓
max = first element
  ↓
compare every element
  ↓
replace max when larger value found
```

Complexity:

```text
Time  → O(n)
Space → O(1)
```

---

# 9. Find Minimum

```python
numbers = [10, 20, 30, 40, 50]

min_element = numbers[0]

for number in numbers:
    if number < min_element:
        min_element = number

print(min_element)
```

Mental model:

```text
Start
  ↓
min = first element
  ↓
compare every element
  ↓
replace min when smaller value found
```

Complexity:

```text
Time  → O(n)
Space → O(1)
```

---

# 10. Count Positive Numbers

```python
numbers = [-5, 10, -2, 30, 0, 15]

count = 0

for number in numbers:
    if number > 0:
        count += 1

print(count)
```

Output:

```text
3
```

Notice:

```text
0
```

is neither positive nor negative.

The condition:

```python
number > 0
```

correctly excludes it.

Complexity:

```text
Time  → O(n)
Space → O(1)
```

---

# 11. Count Negative Numbers

```python
numbers = [-5, 10, -2, 30, 0, 15]

count = 0

for number in numbers:
    if number < 0:
        count += 1

print(count)
```

Output:

```text
2
```

Again:

```text
0
```

is not counted.

---

# 12. Find First Occurrence

Suppose:

```python
numbers = [10, 20, 30, 20, 40]
target = 20
```

We want the index of the **first** occurrence.

```python
first_index = -1

for index, number in enumerate(numbers):
    if number == target:
        first_index = index
        break

print(first_index)
```

Output:

```text
1
```

### Why `break`?

Once the first occurrence is found, the answer is known.

```text
10 → no
20 → YES
     ↓
   stop
```

### Complexity

Best case:

```text
O(1)
```

Worst case:

```text
O(n)
```

Space:

```text
O(1)
```

---

# 13. Find Last Occurrence

For the last occurrence, we cannot stop at the first match.

We continue traversing and update the result whenever we find another match.

```python
numbers = [10, 20, 30, 20, 40]
target = 20

last_index = -1

for index, number in enumerate(numbers):
    if number == target:
        last_index = index

print(last_index)
```

Output:

```text
3
```

Execution:

```text
index 0 → 10 → no

index 1 → 20 → last_index = 1

index 2 → 30 → no

index 3 → 20 → last_index = 3

index 4 → 40 → no
```

Final:

```text
last_index = 3
```

### Important pattern

First occurrence:

```text
find → stop
```

Last occurrence:

```text
find → remember → continue
```

Complexity:

```text
Time  → O(n)
Space → O(1)
```

---

# 14. Check Whether an Element Exists

We can use a Boolean flag.

```python
numbers = [10, 20, 30, 40]
target = 30

element_exists = False

for number in numbers:
    if number == target:
        element_exists = True
        break

print(element_exists)
```

Output:

```text
True
```

### Why `break`?

Once the element is found, we don't need to search further.

Mental model:

```text
Not found
    ↓
keep searching
    ↓
found
    ↓
True
    ↓
stop
```

Complexity:

```text
Best case → O(1)
Worst case → O(n)

Space → O(1)
```

---

# 15. Reverse Traversal

```python
numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])
```

Output:

```text
50
40
30
20
10
```

This is useful when the problem requires:

```text
right → left
last → first
latest → oldest
```

### Important

This does not reverse the array itself.

It only changes the direction in which we process it.

Actual in-place array reversal is a separate problem and will later connect to the **two-pointer pattern**.

---

# 16. Core Traversal Patterns

The problems from Day 01 and Day 02 can be grouped into a few reusable patterns.

---

## Pattern 1 — Simple traversal

```python
for number in numbers:
    process(number)
```

Used when every element must be processed.

---

## Pattern 2 — Conditional traversal

```python
for number in numbers:
    if condition:
        process(number)
```

Used for:

- filtering
- validation
- counting matching elements

---

## Pattern 3 — Counting

```python
count = 0

for number in numbers:
    if condition:
        count += 1
```

Used for:

- positive numbers
- negative numbers
- occurrences
- valid records
- failed records

---

## Pattern 4 — Accumulation

```python
total = 0

for number in numbers:
    total += number
```

Used for:

- sum
- totals
- metrics

---

## Pattern 5 — Track maximum/minimum

```python
best = numbers[0]

for number in numbers:
    if number > best:
        best = number
```

Used for:

- maximum
- minimum
- highest transaction
- lowest price

---

## Pattern 6 — Find first match

```python
result = -1

for index, number in enumerate(numbers):
    if number == target:
        result = index
        break
```

Used when the first matching element matters.

---

## Pattern 7 — Find last match

```python
result = -1

for index, number in enumerate(numbers):
    if number == target:
        result = index
```

Used when the last matching element matters.

---

## Pattern 8 — Existence check

```python
found = False

for number in numbers:
    if number == target:
        found = True
        break
```

Used when the only question is:

```text
Does the element exist?
```

---

# 17. First vs Last Occurrence

This distinction is important for interviews.

### First occurrence

```python
for index, number in enumerate(numbers):
    if number == target:
        result = index
        break
```

```text
Find first
   ↓
Stop immediately
```

### Last occurrence

```python
for index, number in enumerate(numbers):
    if number == target:
        result = index
```

```text
Find match
   ↓
Remember it
   ↓
Continue
   ↓
Later match replaces earlier match
```

---

# 18. Reverse Traversal vs Reverse Array

These are different.

### Reverse traversal

```python
for index in range(len(numbers) - 1, -1, -1):
    print(numbers[index])
```

Processes:

```text
50 → 40 → 30 → 20 → 10
```

But the original array remains unchanged.

### Reverse array

The actual array must become:

```text
[50, 40, 30, 20, 10]
```

We will study the actual reversal algorithm later using **two pointers**.

---

# 19. Edge Cases

Always consider:

### Empty array

```python
numbers = []
```

Be careful with:

```python
numbers[0]
```

because index `0` does not exist.

---

### One element

```python
numbers = [10]
```

The first and last occurrence are both index `0`.

---

### Target does not exist

```python
numbers = [10, 20, 30]
target = 99
```

A useful convention is:

```python
result = -1
```

If the result remains `-1`, the target was not found.

---

### Duplicate values

```python
numbers = [10, 20, 20, 30, 20]
```

This is important when testing:

- first occurrence
- last occurrence
- count occurrences

---

### Negative numbers and zero

```python
numbers = [-5, -2, 0, 10]
```

Remember:

```text
negative → < 0
zero     → == 0
positive → > 0
```

---

# 20. Interview Thinking

For every array problem, ask:

```text
1. What is the input?

2. What does n represent?

3. Do I need to traverse the array?

4. Do I need the value?
       ↓
   value-based traversal

5. Do I need the index?
       ↓
   enumerate() / index traversal

6. Do I need to count something?
       ↓
   accumulator

7. Do I need to track a best value?
       ↓
   maximum / minimum pattern

8. Do I need the first match?
       ↓
   stop with break

9. Do I need the last match?
       ↓
   continue and update

10. Can I stop early?

11. What happens if the target doesn't exist?

12. What happens with an empty array?

13. What is the time complexity?

14. What is the auxiliary space?
```

---

# 21. Complexity of These Basic Problems

Most problems from this day use one traversal.

Therefore:

```text
Time  → O(n)
Space → O(1)
```

Exceptions are based on early termination.

For example:

```python
if number == target:
    break
```

can produce:

```text
Best case  → O(1)
Worst case → O(n)
```

The important thing is to understand **why** rather than memorize the complexity.

---

# 22. What We Practiced

Day 02 covered:

- [x] Forward traversal
- [x] Reverse traversal
- [x] Index-based traversal
- [x] Value-based traversal
- [x] Traversal with conditions
- [x] Traversal with an accumulator
- [x] Find maximum
- [x] Find minimum
- [x] Find sum
- [x] Count occurrences
- [x] Count positive numbers
- [x] Count negative numbers
- [x] Find first occurrence
- [x] Find last occurrence
- [x] Check if an element exists
- [x] Reverse traversal
- [x] Basic interview thinking

---

# 23. Current Learning Strategy

The current DSA approach is intentionally practical.

We are not trying to memorize every theoretical detail before writing code.

The sequence is:

```text
Understand the operation
        ↓
Implement manually
        ↓
Practice traversal
        ↓
Solve basic problems
        ↓
Recognize reusable patterns
        ↓
Analyze complexity
        ↓
Move to optimized patterns
```

The next important step will eventually be:

```text
Basic traversal
      ↓
Two pointers
      ↓
Sliding window
      ↓
Hashing / frequency maps
      ↓
Prefix sum
      ↓
Top K
      ↓
Interview problems
```

---

# Key Takeaways

```text
Forward traversal
    ↓
first → last

Reverse traversal
    ↓
last → first

Value traversal
    ↓
for value in array

Index + value
    ↓
enumerate(array)

Count
    ↓
counter + condition

Sum
    ↓
accumulator

Maximum
    ↓
track largest

Minimum
    ↓
track smallest

First occurrence
    ↓
find → break

Last occurrence
    ↓
find → update → continue

Existence
    ↓
Boolean flag → break
```

The most important skill from Day 02 is:

> **Look at the requirement and identify the traversal pattern before writing the code.**