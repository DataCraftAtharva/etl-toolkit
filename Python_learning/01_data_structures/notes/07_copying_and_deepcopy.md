# Python copying and deepcopy

## Why copying matters

Copying is one of the most misunderstood topics in Python.

The most common production bug is:

> A developer creates a copy of a dictionary or list, modifies it, and accidentally changes the original object.

This happens because Python variables store **references**, not the actual objects.

Understanding copying is essential for:

* configuration management,
* ETL pipelines,
* API data processing,
* Spark transformations,
* caching,
* testing,
* template objects.

---

## Assignment is not copying

Example:

```python
pipeline = {
    "status": "SUCCESS"
}

backup = pipeline
```

Memory:

```text
pipeline ------+

               |

               v

      {status: SUCCESS}

               ^

               |

backup --------+
```

Both variables reference the same dictionary.

Updating one variable:

```python
backup["status"] = "FAILED"
```

Result:

```text
pipeline -> FAILED
backup   -> FAILED
```

Assignment creates another reference.

---

## Shallow copy

A shallow copy creates a **new outer object**.

```python
pipeline = {
    "status": "SUCCESS"
}

backup = pipeline.copy()
```

Memory:

```text
pipeline -----------> {status: SUCCESS}

backup -------------> {status: SUCCESS}
```

The dictionaries are different objects.

Updating:

```python
backup["status"] = "FAILED"
```

Result:

```text
pipeline -> SUCCESS
backup   -> FAILED
```

For flat dictionaries, `copy()` behaves as expected.

---

## The nested object problem

Consider a nested dictionary.

```python
pipeline = {
    "config": {
        "batch_size": 1000
    }
}

backup = pipeline.copy()
```

Memory:

```text
pipeline

 |

 v

{
  config ------+

               |

               v

       {batch_size:1000}

               ^

               |

backup --------+
```

The outer dictionary is copied.

The nested dictionary is shared.

Updating:

```python
backup["config"]["batch_size"] = 5000
```

Result:

```text
pipeline -> 5000
backup   -> 5000
```

This surprises many Python developers.

---

## What a shallow copy actually copies

For a dictionary:

```python
backup = pipeline.copy()
```

Python copies:

* keys,
* references to values.

It does **not recursively copy nested objects**.

Think of it as copying the container, not the contents.

---

## Deep copy

A deep copy recursively copies every nested object.

```python
import copy

backup = copy.deepcopy(pipeline)
```

Memory:

```text
pipeline

 |

 v

{
  config ------> {batch_size:1000}
}

backup

 |

 v

{
  config ------> {batch_size:1000}
}
```

Now the nested dictionaries are independent.

Updating:

```python
backup["config"]["batch_size"] = 9999
```

Result:

```text
pipeline -> 1000
backup   -> 9999
```

---

## Object identities

Use `id()` to check whether objects are shared.

```python
id(pipeline)

id(backup)
```

For a shallow copy:

```text
Outer IDs: different

Nested IDs: same
```

For a deep copy:

```text
Outer IDs: different

Nested IDs: different
```

This is the easiest way to verify copy behavior.

---

## Shallow copy with nested lists

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]

matrix_copy = matrix.copy()
```

Memory:

```text
matrix

 |

 +------+

 |      |

 v      v

[1,2]  [3,4]

 ^      ^

 |      |

 +------+

matrix_copy
```

The inner lists are shared.

Updating:

```python
matrix_copy[0][0] = 999
```

Result:

```text
matrix

[999,2]

[3,4]
```

Both structures change.

---

## Deep copy with nested lists

```python
matrix_copy = copy.deepcopy(matrix)
```

Each inner list is copied.

Updating:

```python
matrix_copy[0][0] = 999
```

Result:

```text
matrix

[1,2]

[3,4]

matrix_copy

[999,2]

[3,4]
```

---

## List slicing

Many developers use slicing.

```python
backup = servers[:]
```

This creates a **shallow copy**.

Example:

```python
servers = [
    {"id": "server-101"}
]

backup = servers[:]
```

Updating:

```python
backup[0]["id"] = "modified"
```

Changes both lists because the dictionary is shared.

---

## copy.copy()

The `copy` module provides:

```python
copy.copy(object)
```

This performs a shallow copy.

Equivalent to:

```python
object.copy()
```

for built-in containers.

---

## copy.deepcopy()

`deepcopy()` recursively copies:

* dictionaries,
* lists,
* tuples,
* sets,
* custom objects,
* nested structures.

Example:

```python
copy.deepcopy(pipeline)
```

Every nested mutable object becomes independent.

---

## When to use shallow copy

Use shallow copy when:

* the structure is flat,
* values are immutable,
* nested objects are intentionally shared,
* performance is important.

Example:

```python
pipeline.copy()
```

---

## When to use deep copy

Use deep copy when:

* nested dictionaries exist,
* nested lists exist,
* configurations are modified independently,
* templates are reused,
* mutation must be isolated.

Example:

```python
pipeline_config = copy.deepcopy(template)
```

---

## Performance consideration

Deep copy is more expensive.

It recursively copies every object.

For large nested structures:

* higher memory usage,
* slower execution.

Use it only when independence is required.

---

## Production example

Suppose a pipeline template is reused.

```python
template = {
    "config": {
        "batch_size": 1000
    }
}
```

Wrong approach:

```python
pipeline_a = template.copy()

pipeline_b = template.copy()
```

Changing one pipeline changes the other.

Correct approach:

```python
pipeline_a = copy.deepcopy(template)

pipeline_b = copy.deepcopy(template)
```

Each pipeline receives its own configuration.

This pattern is common in orchestration systems, ETL frameworks, and distributed job execution.

---

## Common beginner mistakes

### Mistake 1

Thinking assignment creates a copy.

```python
backup = original
```

### Mistake 2

Assuming `copy()` copies nested objects.

```python
backup = original.copy()
```

Nested objects remain shared.

### Mistake 3

Using list slicing for nested lists.

```python
backup = matrix[:]
```

Inner lists remain shared.

---

## Interview note

A concise interview answer:

> Assignment creates another reference to the same object. A shallow copy creates a new outer container but shares nested mutable objects. A deep copy recursively copies all nested objects, producing completely independent data structures. Deep copy is essential when modifying nested dictionaries or lists independently.
