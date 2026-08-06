# Python if, elif, and else

## What is conditional execution?

A program often needs to make decisions.

Examples:

* retry a failed pipeline,
* skip invalid records,
* send alerts,
* process only active assets,
* choose a processing strategy.

Conditional execution allows Python to execute different code depending on a condition.

---

## The basic if statement

```python
pipeline_status = "SUCCESS"

if pipeline_status == "SUCCESS":
    print("Pipeline completed successfully")
```

Output:

```text
Pipeline completed successfully
```

The code inside the `if` block executes only when the condition is **True**.

---

## The if-else statement

Use `else` when exactly one of two paths should execute.

```python
pipeline_status = "FAILED"

if pipeline_status == "SUCCESS":
    print("Generate success report")
else:
    print("Generate failure alert")
```

Output:

```text
Generate failure alert
```

Only one branch executes.

---

## The if-elif-else statement

Use `elif` when multiple conditions are possible.

```python
pipeline_status = "RUNNING"

if pipeline_status == "SUCCESS":
    print("Completed")
elif pipeline_status == "RUNNING":
    print("Executing")
elif pipeline_status == "FAILED":
    print("Failed")
else:
    print("Unknown status")
```

Output:

```text
Executing
```

Python checks conditions from top to bottom.

The first matching condition executes.

---

## Execution flow

Example:

```python
if condition_1:
    ...
elif condition_2:
    ...
elif condition_3:
    ...
else:
    ...
```

Flow:

```text
condition_1

   |

   +-- True --> execute block

   |

   False

   |

condition_2

   |

   +-- True --> execute block

   |

   False

   |

condition_3

   |

   +-- True --> execute block

   |

   False

   |

else block
```

Once a condition matches, the remaining conditions are skipped.

---

## Comparison operators

Python conditions usually involve comparisons.

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

Example:

```python
processed_records = 1250

if processed_records > 1000:
    print("Large batch")
```

Output:

```text
Large batch
```

---

## Logical operators

### and

Both conditions must be true.

```python
if status == "FAILED" and retry_count < 3:
    retry_pipeline()
```

### or

At least one condition must be true.

```python
if status == "FAILED" or status == "TIMEOUT":
    send_alert()
```

### not

Reverses the condition.

```python
if not status == "SUCCESS":
    investigate()
```

---

## Nested if statements

Conditions can be nested.

```python
if pipeline["status"] == "FAILED":
    if pipeline["retry_count"] < 3:
        retry_pipeline()
    else:
        escalate()
```

Execution:

```text
FAILED?

 |

 +-- No --> stop

 |

 Yes

 |

retry_count < 3?

 |

 +-- Yes --> retry

 |

 No

 |

escalate
```

Nested conditions are useful when one decision depends on another.

---

## Truthy and falsy values

Python automatically treats some values as True or False.

Falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

Example:

```python
assets = []

if assets:
    print("Data available")
else:
    print("No data")
```

Output:

```text
No data
```

This is a very common Python pattern.

---

## Checking for None

Use:

```python
if owner is None:
    ...
```

Not:

```python
if owner == None:
    ...
```

`is None` checks object identity and is the recommended style.

Example:

```python
owner = None

if owner is None:
    print("Owner missing")
```

Output:

```text
Owner missing
```

---

## Combining conditions

Example:

```python
if (
    pipeline["status"] == "FAILED"
    and pipeline["retry_count"] < 3
    and pipeline["processed_records"] > 0
):
    retry_pipeline()
```

This style is common in production code because it remains readable.

---

## Production example

Consider a pipeline record.

```python
pipeline = {
    "status": "FAILED",
    "retry_count": 2,
    "processed_records": 1500
}
```

Decision logic:

```python
if pipeline["status"] == "SUCCESS":
    mark_completed()
elif pipeline["status"] == "FAILED" and pipeline["retry_count"] < 3:
    retry_pipeline()
elif pipeline["status"] == "FAILED":
    escalate()
else:
    monitor()
```

This pattern appears in:

* Airflow,
* Azure Data Factory,
* Databricks workflows,
* monitoring systems,
* alerting pipelines.

---

## Common beginner mistakes

### Mistake 1

Using `=` instead of `==`.

Wrong:

```python
if status = "SUCCESS":
```

Correct:

```python
if status == "SUCCESS":
```

### Mistake 2

Writing multiple independent `if` statements.

```python
if status == "FAILED":
    ...

if retry_count < 3:
    ...
```

Sometimes this should be:

```python
if status == "FAILED" and retry_count < 3:
    ...
```

### Mistake 3

Comparing with `None` using `==`.

Prefer:

```python
if value is None:
```

---

## Interview note

A concise interview answer:

> `if`, `elif`, and `else` control program execution based on Boolean conditions. Python evaluates conditions from top to bottom and executes the first matching branch. Logical operators (`and`, `or`, `not`) combine conditions, and `is None` is the preferred way to check for missing values. Conditional logic is fundamental for validation, filtering, retries, and workflow decisions in production systems.
