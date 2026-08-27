# Python while Loops

## What is a while loop?

A `while` loop repeatedly executes a block of code **while a condition is True**.

```python
count = 0

while count < 3:
    print(count)
    count += 1
````

Output:

```text
0
1
2
```

The condition is checked **before every iteration**.

---

# Basic Structure

```python
while condition:
    # work
```

Execution:

```text
Check condition
      ↓
   True?
   /   \
 Yes    No
  ↓      ↓
Work    Stop
  ↓
Check again
```

---

# Counter-Controlled Loop

Use a counter when the number of iterations is controlled by a condition.

```python
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
```

Important:

> Make sure something inside the loop changes the condition.

---

# Condition-Controlled Loop

Use `while` when the loop should continue until some state changes.

```python
status = "RUNNING"

while status == "RUNNING":
    check_status()
```

The number of iterations may not be known beforehand.

---

# `while True`

`while True` creates a loop that continues until explicitly stopped.

```python
while True:
    value = get_value()

    if value == "STOP":
        break
```

Common for:

- event processing
    
- monitoring
    
- consumers
    
- long-running processes
    

---

# `break`

`break` immediately exits the loop.

```python
attempt = 0

while attempt < 5:
    attempt += 1

    if success():
        break
```

Think:

```text
break → Stop the loop now
```

---

# `continue`

`continue` skips the current iteration and starts the next iteration.

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

Think:

```text
continue → Skip this iteration
```

---

# `pass`

`pass` does nothing.

It is mainly used as a placeholder.

```python
while condition:
    pass
```

Think:

```text
pass → Do nothing
```

Unlike `break` and `continue`, it does **not** change loop execution.

---

# Retry Pattern

A common `while` pattern is:

```python
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    attempt += 1

    # perform operation
```

The loop stops when:

```text
attempt >= max_attempts
```

Production systems usually also need:

- clear retry limits
    
- error handling
    
- delays/backoff
    
- logging
    

---

# Polling Pattern

Polling means repeatedly checking a condition.

```python
status = "RUNNING"

while status == "RUNNING":
    status = check_status()
```

Typical examples:

- waiting for a job
    
- checking an API
    
- monitoring a pipeline
    
- waiting for a file
    

In real systems, polling normally includes a delay.

```python
import time

while status == "RUNNING":
    status = check_status()
    time.sleep(5)
```

---

# Queue Processing

A `while` loop can process items until a queue becomes empty.

```python
while queue:
    item = queue.pop(0)
    process(item)
```

The condition:

```python
while queue:
```

means:

> Continue while the queue contains elements.

---

# Avoid Infinite Loops

An infinite loop occurs when the condition never becomes False.

Wrong:

```python
count = 0

while count < 5:
    print(count)
```

`count` never changes.

Correct:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Always identify:

```text
What starts the loop?
        ↓
What changes?
        ↓
What eventually stops the loop?
```

---

# `for` vs `while`

This is the most important distinction.

| Use `for`                         | Use `while`                            |
| --------------------------------- | -------------------------------------- |
| Iterating over a collection       | Waiting for a condition                |
| Known/collection-driven iteration | Unknown number of iterations           |
| Processing records                | Retrying an operation                  |
| Traversing a list                 | Polling a service                      |
| Iterating over dictionary items   | Monitoring a process                   |
| Processing file lines             | Processing until a queue/state changes |

### Simple rule

> **Use `for` when you are iterating over something.**

```python
for record in records:
    process(record)
```

> **Use `while` when you are waiting for something to happen or continue while a condition remains true.**

```python
while status == "RUNNING":
    check_status()
```

---

# Quick Decision Rule

Ask yourself:

```text
Am I iterating over a collection?
        |
       YES
        ↓
       for


Do I continue until a condition changes?
        |
       YES
        ↓
      while
```

---

# Common Mistakes

### Forgetting to update the condition

```python
while count < 5:
    print(count)
```

Possible infinite loop.

---

### Using `while` unnecessarily

Instead of:

```python
index = 0

while index < len(records):
    process(records[index])
    index += 1
```

Prefer:

```python
for record in records:
    process(record)
```

when simply iterating through a collection.

---

### Busy polling

Avoid repeatedly checking an external system without a delay.

```python
while status == "RUNNING":
    check_status()
```

Prefer an appropriate delay/backoff in real systems.

---

# Mental Model

```text
FOR
→ "Give me each item."

WHILE
→ "Keep going while this condition is true."

BREAK
→ "Stop now."

CONTINUE
→ "Skip this iteration."

PASS
→ "Do nothing for now."
```

---

# Interview Note

> A `for` loop is generally used to iterate over an iterable or collection, while a `while` loop is used when execution should continue as long as a condition remains true. `while` is commonly useful for retries, polling, monitoring, and state-based processing. The key concern with `while` is ensuring a clear termination condition.

