# Python imports

## What is an import?

A **module** is simply a Python file with a `.py` extension.

For example:

```text
main.py
extract.py
```

When you write:

```python
import extract
```

Python loads the `extract.py` file into the current program.

---

## Why imports matter

Imports allow us to:

* organize code into multiple files,
* reuse code,
* build larger applications,
* create Python packages,
* structure ETL pipelines and data engineering projects.

Almost every real Python project uses imports.

---

## What actually happens during an import?

When Python executes:

```python
import extract
```

it performs these steps:

```text
main.py

↓

Python sees: import extract

↓

Find extract.py

↓

Compile extract.py into bytecode

↓

Execute all top-level code in extract.py

↓

Create a module object

↓

Store it in sys.modules

↓

Return control to main.py
```

The most important point is:

**Python executes the imported file.**

---

## Top-level code

Any code that is **not inside a function or class** is called **top-level code**.

Example:

```python
print("Extract module loaded")
```

This line runs immediately when the module is imported.

---

## Example

`extract.py`

```python
print("Extract module loaded")
```

`main.py`

```python
print("Main started")

import extract

print("Main finished")
```

Output:

```text
Main started
Extract module loaded
Main finished
```

Notice that the imported file executes before Python continues with the next line in `main.py`.

---

## Why this matters in production

Imagine an ETL module:

```python
connect_to_database()
```

If that code is placed at the top level of a module, importing the module will immediately connect to the database.

This can:

* slow application startup,
* create unnecessary database connections,
* cause import-time failures,
* make testing difficult.

---

## The import cache

Python imports a module **only once**.

The first import:

```python
import extract
```

loads and executes the module.

The second import:

```python
import extract
```

does **not execute it again**.

Python reuses the cached module stored in `sys.modules`.

---

## Common beginner mistakes

### Mistake 1

Thinking import copies code.

Correct:

Import executes the module and creates a module object.

### Mistake 2

Putting expensive operations at the top level.

Correct:

Place database connections, file reading, API calls, and heavy computations inside functions.

---

## Interview note

When asked **“What happens when Python imports a module?”**, answer:

> Python finds the module, compiles it into bytecode, executes its top-level code, creates a module object, stores it in `sys.modules`, and returns that module object to the importing program.
