# Python while loops

## What is a while loop?

A `while` loop repeatedly executes a block of code **until a condition becomes False**.

Example:

```python
attempt = 1

while attempt <= 3:
    print(attempt)
    attempt += 1
```

Output:

```text
1
2
3
```

The condition is checked **before every iteration**.

---

## How a while loop works

General syntax:

```python
while condition:
    work()
```

Execution flow:

```text
Check condition
       |
       +-- False --> Exit loop
       |
       True
       |
Execute loop body
       |
Repeat
```

The loop continues until the condition becomes False.

---

## Basic example

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining -= 1
```

Output:

```text
3
2
1
```

Notice that `remaining` changes during each iteration.

---

## Why while loops matter

`while` loops are used when the **number of iterations is unknown**.

Common examples:

* retrying a failed pipeline,
* waiting for a file,
* polling an API,
* monitoring a running job,
* processing a queue,
* consuming streaming data.

---

## Retry mechanism

A very common production pattern.

```python
retry_count = 0
max_retries = 3

while status == "FAILED" and retry_count < max_retries:
    retry_count += 1
```

Execution:

```text
Failed?
   |
   +-- No --> Stop
   |
   Yes
   |
Retry count < max?
   |
   +-- No --> Escalate
   |
   Yes
   |
Retry pipeline
```

This pattern appears in Airflow, Azure Data Factory, Databricks, and API clients.

---

## Polling

Polling repeatedly checks whether a task has completed.

Example:

```python
while job_status == "RUNNING":
    check_status()
```

Typical use cases:

* Spark job completion,
* Azure Data Factory pipeline status,
* Databricks job monitoring,
* Kubernetes pod readiness,
* file arrival monitoring.

Polling usually includes a delay.

```python
import time

while job_status == "RUNNING":
    check_status()
    time.sleep(5)
```

This prevents excessive API calls.

---

## Waiting for data

Example:

```python
while not records_available:
    check_storage()
```

Business examples:

* waiting for a CSV file,
* waiting for an ADLS object,
* waiting for Kafka messages,
* waiting for an upstream pipeline.

---

## Infinite loops

```python
while True:
    ...
```

This loop runs forever unless explicitly stopped.

Usually combined with:

```python
break
```

Example:

```python
while True:
    event = read_event()

    if event == "STOP":
        break
```

Common use cases:

* stream consumers,
* monitoring agents,
* long-running services,
* event processors.

---

## Queue processing

A realistic processing pattern.

```python
while task_queue:
    task = task_queue.pop(0)
    process(task)
```

The loop continues until the queue becomes empty.

Used in:

* task scheduling,
* work queues,
* batch processing,
* orchestration systems.

---

## Exponential backoff

Production systems often increase the waiting time between retries.

Example:

```python
wait_time = 2 ** retry
```

Sequence:

```text
Retry 1 -> 2s
Retry 2 -> 4s
Retry 3 -> 8s
Retry 4 -> 16s
```

This reduces pressure on failing systems.

Common in:

* cloud APIs,
* distributed systems,
* Kafka clients,
* HTTP clients.

---

## Monitoring loops

Example:

```python
while pipeline["status"] == "RUNNING":
    monitor_pipeline()
```

Workflow:

```text
Start monitoring
       |
Check status
       |
Completed?
       |
       +-- No --> Wait and repeat
       |
       Yes
       |
Generate report
```

---

## The biggest while-loop risk

An infinite loop occurs when the condition never becomes False.

Example:

```python
count = 0

while count < 5:
    print(count)
```

Output:

```text
0
0
0
0
...
```

The variable `count` never changes.

Correct:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Always ensure that the loop has a termination path.

---

## for vs while

This is one of the most important engineering decisions.

| Use for                     | Use while                    |
| --------------------------- | ---------------------------- |
| Known number of records     | Unknown number of iterations |
| Processing a list           | Waiting for completion       |
| Reading file lines          | Retrying a failed task       |
| Transforming data           | Polling an API               |
| Iterating over dictionaries | Monitoring a running process |

The key question is:

> **Do I know how many times I need to iterate?**

If yes, use `for`.

If no, use `while`.

---

## Common beginner mistakes

### Mistake 1

Forgetting to update the condition.

Wrong:

```python
while retry < 3:
    process()
```

Correct:

```python
while retry < 3:
    process()
    retry += 1
```

---

### Mistake 2

Using `while` instead of `for`.

Wrong:

```python
index = 0

while index < len(records):
    process(records[index])
    index += 1
```

Better:

```python
for record in records:
    process(record)
```

Use `for` when iterating over a collection.

---

### Mistake 3

Creating busy polling loops.

Wrong:

```python
while status == "RUNNING":
    check_status()
```

Better:

```python
while status == "RUNNING":
    check_status()
    time.sleep(5)
```

---

## Business usage guide

### Use if-elif-else

When choosing **one action** based on a condition.

Examples:

* pipeline succeeded,
* pipeline failed,
* validation decisions,
* routing logic.

---

### Use match-case

When matching **specific values or structured data**.

Examples:

* event types,
* command processors,
* API message types,
* Kafka event routing.

---

### Use for loops

When processing a **known collection of data**.

Examples:

* database rows,
* CSV files,
* JSON records,
* aggregation,
* transformation.

---

### Use while loops

When the number of iterations is **not known in advance**.

Examples:

* retries,
* polling,
* waiting,
* monitoring,
* queue processing,
* streaming consumers.

---

## Interview note

A concise interview answer:

> A `while` loop repeatedly executes code until a condition becomes False. It is ideal when the number of iterations is unknown, such as retries, polling, monitoring, queue processing, and stream consumption. The most important consideration is ensuring that the loop has a clear termination condition to avoid infinite loops.
