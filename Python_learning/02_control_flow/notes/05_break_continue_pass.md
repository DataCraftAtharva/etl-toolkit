# Python — `break`, `continue`, and `pass`

## Why this matters

`break`, `continue`, and `pass` control what happens inside a loop.

They are different:

```text
break
  ↓
Stop the entire loop

continue
  ↓
Skip the current iteration

pass
  ↓
Do nothing
```

These are simple statements, but understanding their execution flow is important for writing clean loops and solving interview problems.

---

# 1. `break`

## What is `break`?

`break` immediately terminates the **nearest enclosing loop**.

Execution continues with the statement after the loop.

### Example

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
```

Output:

```text
1
2
```

When `number == 3`:

```text
break
 ↓
loop terminates
 ↓
execution continues after loop
```

---

# 2. `break` with `while`

```python
attempt = 1

while attempt <= 5:
    print(f"Attempt {attempt}")

    if attempt == 3:
        break

    attempt += 1
```

Output:

```text
Attempt 1
Attempt 2
Attempt 3
```

The loop could have continued to 5, but `break` stopped it at attempt 3.

---

# 3. Common use cases for `break`

`break` is useful when:

* the required item is found
* an operation succeeds
* a retry succeeds
* a timeout occurs
* an error requires stopping
* a termination signal is received

### Example — searching

```python
records = ["A", "B", "C", "D"]

for record in records:
    if record == "C":
        print("Record found")
        break
```

Once the record is found, there is no reason to continue searching.

---

# 4. `continue`

## What is `continue`?

`continue` skips the **current iteration** and moves to the next iteration of the loop.

It does **not** terminate the loop.

### Example

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

When `number == 3`:

```text
continue
    ↓
skip remaining code in current iteration
    ↓
next iteration
```

---

# 5. `continue` with `while`

Be careful with `continue` in a `while` loop.

The condition-changing logic must happen **before** `continue` when necessary.

Correct:

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

Output:

```text
1
2
4
5
```

Here `count += 1` happens before `continue`, so the loop can progress.

---

# 6. Common use cases for `continue`

`continue` is useful when a record should be skipped.

Examples:

* invalid records
* empty records
* unwanted statuses
* filtered data
* records failing validation

### Example

```python
records = [
    "record-101",
    "",
    "record-102",
    "",
    "record-103"
]

for record in records:
    if not record:
        continue

    print(f"Processing {record}")
```

Output:

```text
Processing record-101
Processing record-102
Processing record-103
```

This is a common data-processing pattern.

---

# 7. `pass`

## What is `pass`?

`pass` is a **placeholder statement**.

It does nothing.

```python
if condition:
    pass
```

The program continues normally after the `pass`.

---

# 8. Why does `pass` exist?

Python requires an indented statement after constructs such as:

```python
if
for
while
function
class
```

If you don't have implementation yet, `pass` can temporarily satisfy that requirement.

Example:

```python
def process_pipeline():
    pass
```

The function is syntactically valid but currently does nothing.

---

# 9. `pass` inside a loop

```python
for number in range(5):
    if number == 3:
        pass

    print(number)
```

Output:

```text
0
1
2
3
4
```

Notice that `pass` does **not** skip `3`.

Compare:

```python
continue
```

with:

```python
pass
```

### `continue`

```python
if number == 3:
    continue

print(number)
```

Output:

```text
0
1
2
4
```

### `pass`

```python
if number == 3:
    pass

print(number)
```

Output:

```text
0
1
2
3
4
```

This is one of the most important differences.

---

# 10. `break` vs `continue` vs `pass`

| Statement  | Effect                  |
| ---------- | ----------------------- |
| `break`    | Terminates the loop     |
| `continue` | Skips current iteration |
| `pass`     | Does nothing            |

Think:

```text
break
  ↓
STOP LOOP


continue
  ↓
SKIP ITERATION


pass
  ↓
DO NOTHING
```

---

# 11. Execution Flow

Consider:

```python
for number in range(1, 6):

    if number == 2:
        continue

    if number == 4:
        break

    print(number)
```

Execution:

```text
number = 1
    ↓
print 1

number = 2
    ↓
continue
    ↓
skip print

number = 3
    ↓
print 3

number = 4
    ↓
break
    ↓
loop terminates
```

Output:

```text
1
3
```

---

# 12. Nested Loops

`break` and `continue` affect the **nearest enclosing loop**.

Example:

```python
for outer in range(3):

    for inner in range(3):

        if inner == 1:
            break

        print(outer, inner)
```

`break` stops the inner loop, not the outer loop.

Conceptually:

```text
Outer loop
    │
    ├── Inner loop
    │      │
    │      └── break
    │
    ↓
Outer loop continues
```

This is important when working with nested loops.

---

# 13. `continue` in Nested Loops

Similarly, `continue` affects the nearest loop.

```python
for outer in range(2):

    for inner in range(3):

        if inner == 1:
            continue

        print(outer, inner)
```

Only the current iteration of the **inner loop** is skipped.

The outer loop continues normally.

---

# 14. Data Engineering Examples

## Example 1 — Stop when pipeline succeeds

```python
attempt = 0

while attempt < 5:
    attempt += 1

    status = check_pipeline()

    if status == "SUCCESS":
        break
```

`break` is appropriate because further attempts are unnecessary.

---

## Example 2 — Skip invalid records

```python
for record in records:

    if not record:
        continue

    process(record)
```

`continue` is appropriate because the invalid record should be ignored while processing continues.

---

## Example 3 — Placeholder implementation

```python
def validate_pipeline():
    pass
```

`pass` is appropriate temporarily when the implementation hasn't been written yet.

---

# 15. Common Mistakes

## Mistake 1 — Thinking `pass` skips an iteration

Wrong:

```python
if invalid:
    pass
```

`pass` does not skip anything.

Use:

```python
if invalid:
    continue
```

if you want to skip the current iteration.

---

## Mistake 2 — Thinking `continue` stops the loop

Wrong mental model:

```text
continue → stop loop
```

Correct:

```text
continue → skip current iteration
```

---

## Mistake 3 — Forgetting loop progress with `continue`

This can create an infinite loop:

```python
count = 0

while count < 5:

    if count == 3:
        continue

    count += 1
```

When `count == 3`, `continue` executes before `count += 1`.

Therefore:

```text
count remains 3
        ↓
condition remains True
        ↓
continue
        ↓
count remains 3
        ↓
infinite loop
```

Correct:

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue
```

---

# 16. Quick Decision Rule

When inside a loop, ask:

### Do I want to stop everything?

```python
break
```

### Do I want to skip this item?

```python
continue
```

### Do I intentionally want no operation?

```python
pass
```

---

# 17. Interview Question

### What is the difference between `break`, `continue`, and `pass`?

Answer:

> `break` immediately terminates the nearest enclosing loop. `continue` skips the remaining statements of the current iteration and proceeds to the next iteration. `pass` performs no operation and is mainly used as a placeholder where Python requires a statement.

---

# 18. Mental Model

```text
                 LOOP
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
        break   continue    pass
          │        │        │
          ↓        ↓        ↓
      stop loop  skip item  do nothing
```

The key distinction:

```text
break    → LOOP CONTROL
continue → ITERATION CONTROL
pass     → NO-OP / PLACEHOLDER
```

---

# 19. What You Should Remember

```text
break
→ terminate nearest loop

continue
→ skip current iteration

pass
→ do nothing

Nested loops
→ break/continue affect nearest enclosing loop

while + continue
→ make sure loop state still changes

pass
→ does NOT skip, stop, or change execution
```

For Data Engineering, the most useful practical patterns are:

```text
break
→ stop retry/search/monitoring when condition is satisfied

continue
→ skip invalid/unwanted records

pass
→ temporary placeholder
```
