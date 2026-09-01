# Python `match-case`

## 1. What is `match-case`?

`match-case` is Python's **structural pattern matching** feature introduced in Python 3.10.

It allows you to compare a value against different patterns.

Unlike a traditional `if-elif` chain, `match-case` can match not only simple values but also **data structures** such as:

* strings
* numbers
* tuples
* lists
* dictionaries
* nested structures

It is especially useful when processing structured data such as JSON events, commands, API responses, and pipeline events.

---

# 2. Basic Syntax

```python
match value:
    case pattern_1:
        ...
    case pattern_2:
        ...
    case _:
        ...
```

Python evaluates cases **from top to bottom**.

The first matching case is executed.

```python
status = "FAILED"

match status:
    case "SUCCESS":
        print("Pipeline completed")
    case "FAILED":
        print("Pipeline failed")
    case _:
        print("Unknown status")
```

Output:

```text
Pipeline failed
```

---

# 3. `_` — Wildcard Pattern

`_` matches anything.

```python
match status:
    case "SUCCESS":
        print("Success")
    case _:
        print("Everything else")
```

The wildcard is commonly used as the default case.

It does **not capture** the value.

```python
case _:
```

means:

> Match anything, but don't store the value.

---

# 4. Literal Value Matching

You can match literal values directly.

```python
status = "SUCCESS"

match status:
    case "SUCCESS":
        print("Completed")
    case "FAILED":
        print("Failed")
```

This is similar to a switch statement in other languages.

However, `match-case` is more powerful than a traditional switch because it can match **structures**.

---

# 5. Matching Multiple Values

Use `|` for an OR pattern.

```python
status = "TIMEOUT"

match status:
    case "FAILED" | "TIMEOUT":
        print("Pipeline requires investigation")
    case "SUCCESS":
        print("Pipeline completed")
    case _:
        print("Unknown status")
```

This is conceptually similar to:

```python
if status == "FAILED" or status == "TIMEOUT":
    print("Pipeline requires investigation")
```

---

# 6. Matching Numbers

Numbers can be matched directly.

```python
retry_count = 2

match retry_count:
    case 0:
        print("First attempt")
    case 1:
        print("First retry")
    case 2:
        print("Second retry")
    case _:
        print("More retries")
```

However, `match-case` is not generally the best choice for ranges.

For example:

```python
if retry_count > 3:
    ...
```

is often clearer than:

```python
match retry_count:
    case value if value > 3:
        ...
```

---

# 7. Capture Patterns

A variable inside a pattern can **capture** a value.

```python
match retry_count:
    case value:
        print(value)
```

Here, `value` does NOT mean:

> compare against an existing variable called `value`

Instead, it captures whatever value was matched.

This is called a **capture pattern**.

Example:

```python
event = ("FAILED", 2)

match event:
    case ("FAILED", retry):
        print(retry)
```

Output:

```text
2
```

The value `2` is captured into `retry`.

---

# 8. Guards

A guard adds an additional condition to a pattern.

```python
records = 1500

match records:
    case value if value > 1000:
        print("Large batch")
    case value if value > 0:
        print("Small batch")
    case _:
        print("No records")
```

The pattern must match **and** the guard must evaluate to `True`.

Conceptually:

```text
pattern matches
       AND
guard is True
       ↓
execute case
```

---

# 9. Tuple Pattern Matching

Tuples can be matched structurally.

```python
event = ("FAILED", 2)

match event:
    case ("SUCCESS", _):
        print("Pipeline succeeded")

    case ("FAILED", retry):
        print(f"Retry pipeline: {retry}")
```

The tuple structure must match.

The `_` ignores a value.

---

# 10. List Pattern Matching

Lists can also be matched.

```python
asset = ["server-101", "ACTIVE"]

match asset:
    case [asset_id, "ACTIVE"]:
        print(f"Process active asset: {asset_id}")

    case [asset_id, "FAILED"]:
        print(f"Alert for {asset_id}")

    case _:
        print("Unknown asset")
```

The pattern:

```python
[asset_id, "ACTIVE"]
```

means:

```text
first element → capture as asset_id
second element → must equal "ACTIVE"
```

---

# 11. Sequence Matching with `*`

You can capture multiple remaining values using `*`.

```python
numbers = [10, 20, 30, 40]

match numbers:
    case [first, *remaining]:
        print(first)
        print(remaining)
```

Output:

```text
10
[20, 30, 40]
```

This can be useful when processing variable-length sequences.

---

# 12. Dictionary Pattern Matching

Dictionaries can be matched by structure.

```python
pipeline = {
    "status": "FAILED",
    "retry_count": 2
}

match pipeline:
    case {"status": "FAILED", "retry_count": retry}:
        print(f"Retry: {retry}")
```

The value of `retry_count` is captured into `retry`.

---

# 13. Important Dictionary Behavior

A dictionary pattern does **not** require the dictionary to contain only those keys.

For example:

```python
event = {
    "status": "FAILED",
    "retry_count": 2,
    "pipeline": "sales_etl"
}

match event:
    case {"status": "FAILED"}:
        print("Pipeline failed")
```

This still matches.

Why?

Because the pattern only requires:

```text
status == "FAILED"
```

Additional keys are allowed.

This is different from checking exact dictionary equality.

---

# 14. Capturing Dictionary Values

You can extract values while matching.

```python
event = {
    "asset_id": "server-102",
    "status": "FAILED"
}

match event:
    case {"asset_id": asset, "status": "FAILED"}:
        print(f"Alert generated for {asset}")
```

Output:

```text
Alert generated for server-102
```

This is particularly useful when processing JSON-like data.

---

# 15. Nested Pattern Matching

Nested structures can be matched directly.

```python
event = {
    "asset_id": "server-201",
    "metrics": {
        "cpu": 92
    }
}

match event:
    case {
        "asset_id": asset,
        "metrics": {"cpu": cpu}
    } if cpu > 90:
        print(f"Critical CPU alert for {asset}: {cpu}%")
```

This simultaneously:

1. matches the dictionary
2. finds `asset_id`
3. enters the nested `metrics` dictionary
4. extracts `cpu`
5. checks the guard

This is one of the strongest use cases for structural pattern matching.

---

# 16. Case Ordering Matters

Cases are evaluated from top to bottom.

Therefore, put **specific patterns before general patterns**.

Good:

```python
match event:
    case {"status": "FAILED", "retry_count": retry} if retry < 3:
        print("Retry")

    case {"status": "FAILED"}:
        print("Escalate")

    case _:
        print("Unknown")
```

The specific case comes first.

A broad pattern placed too early can prevent later cases from ever being reached.

Think:

```text
specific
   ↓
less specific
   ↓
default
```

---

# 17. Practical Data Engineering Example

Suppose a pipeline monitoring system receives events:

```python
event = {
    "type": "PIPELINE_FAILED",
    "pipeline": "daily_sales_etl"
}
```

We can dispatch the event using `match-case`.

```python
match event:
    case {
        "type": "PIPELINE_STARTED",
        "pipeline": pipeline_name
    }:
        print(f"Start monitoring {pipeline_name}")

    case {
        "type": "PIPELINE_COMPLETED",
        "pipeline": pipeline_name
    }:
        print(f"Generate completion report for {pipeline_name}")

    case {
        "type": "PIPELINE_FAILED",
        "pipeline": pipeline_name
    }:
        print(f"Generate alert for {pipeline_name}")

    case _:
        print("Ignore unknown event")
```

This is much easier to extend when many event types exist.

---

# 18. `match-case` vs `if-elif`

## Use `if-elif` when:

The logic is primarily based on conditions.

```python
if cpu > 90 and memory > 80:
    ...
elif cpu > 70:
    ...
```

This is naturally expressed as conditional logic.

## Use `match-case` when:

The logic is primarily based on patterns or structures.

```python
match event:
    case {"type": "FAILED"}:
        ...
    case {"type": "SUCCESS"}:
        ...
```

Especially useful for:

* event dispatching
* command processing
* JSON structures
* API responses
* state machines
* structured messages

---

# 19. Common Mistakes

## Mistake 1 — Treating `match` as only a switch

`match-case` is more than a switch statement.

Its major feature is **structural pattern matching**.

---

## Mistake 2 — Confusing capture with comparison

This:

```python
case status:
```

captures a value.

It does NOT mean:

```python
value == status
```

For a literal string, use:

```python
case "SUCCESS":
```

---

## Mistake 3 — Putting `_` too early

Avoid:

```python
match event:
    case _:
        print("Anything")
    case {"status": "FAILED"}:
        print("Failed")
```

The second case will never be reached.

The wildcard should normally be last.

---

## Mistake 4 — Using `match-case` for everything

Don't replace every `if` statement with `match`.

Use the construct that makes the logic easiest to understand.

---

# 20. Interview Answer

### What is `match-case`?

> `match-case` is Python's structural pattern matching feature introduced in Python 3.10. It allows us to match literals as well as structured data such as tuples, lists, dictionaries, and nested structures. It can also capture values, combine patterns using `|`, and apply additional conditions using guards. It is particularly useful for event dispatching, JSON processing, and state-based logic.

---

# 21. Data Engineering Use Cases

`match-case` can be useful for:

```text
Kafka event processing
        ↓
API response handling
        ↓
Pipeline event dispatching
        ↓
ETL state management
        ↓
Validation / routing
        ↓
Command processing
```

Example:

```python
match event:
    case {"type": "ORDER_CREATED"}:
        ...
    case {"type": "ORDER_UPDATED"}:
        ...
    case {"type": "ORDER_DELETED"}:
        ...
```

---

# 22. What You Should Remember

```text
match
  ↓
compare against patterns
  ↓
first matching case executes
  ↓
patterns can be structural
  ↓
values can be captured
  ↓
guards add conditions
  ↓
_ = wildcard
```

The most important concepts are:

```text
Literal matching
OR patterns |
Capture patterns
Wildcard _
Guards
Tuple patterns
List patterns
Dictionary patterns
Nested patterns
Sequence unpacking *
Case ordering
```

---

# 23. Practice Problems

Before moving to `for` loops, solve these without looking at the previous examples.

### Problem 1 — Job Status

Given:

```python
job = ("FAILED", 2)
```

Print:

```text
Retry job
```

when the retry count is below 3.

Hint:

```python
case ("FAILED", retry) if ...
```

---

### Problem 2 — API Response

Given:

```python
response = {
    "status": 200,
    "data": "success"
}
```

Use `match-case` to handle:

```text
200 → Success
404 → Not Found
500 → Server Error
anything else → Unknown
```

---

### Problem 3 — Kafka Event

Given:

```python
event = {
    "type": "ORDER_CREATED",
    "order_id": 101
}
```

Extract `order_id` and print:

```text
Process order 101
```

---

### Problem 4 — Nested Event

Given:

```python
event = {
    "type": "PIPELINE",
    "details": {
        "status": "FAILED",
        "retry_count": 2
    }
}
```

Print:

```text
Retry pipeline
```

if retries are below 3.

---

### Problem 5 — Variable-Length List

Given:

```python
records = ["server-101", "server-102", "server-103"]
```

Use pattern matching to capture the first server and the remaining servers.

---
