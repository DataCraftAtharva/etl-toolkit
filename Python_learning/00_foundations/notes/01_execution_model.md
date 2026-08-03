# Python execution model

## What is the Python execution model?

The Python execution model explains **what happens after a Python file is run**.

When you execute:

```bash
python main.py
```

Python does much more than simply read the file and print the output.

It goes through a series of steps before the program actually runs.

Understanding this process helps explain:

* Python scripts
* ETL jobs
* Airflow DAGs
* Spark driver programs
* FastAPI applications
* Azure Functions

Every Python application starts with this execution model.

---

## The complete execution flow

```text
main.py (source code)

↓

Python interpreter starts

↓

Source code is compiled into bytecode

↓

Bytecode is sent to the Python Virtual Machine (PVM)

↓

The PVM executes the bytecode

↓

Your program runs

↓

The program finishes
```

The most important thing to remember is:

**Python executes code sequentially (top to bottom).**

---

## Source code vs bytecode

### Source code

This is the code written by the programmer.

```python
print("Pipeline started")
```

### Bytecode

Python first converts the source code into **bytecode**, which is a lower-level representation of the program.

Bytecode is not machine code.

It is an intermediate format that the **Python Virtual Machine (PVM)** understands.

A simplified view:

```text
Source code

↓

Bytecode

↓

Python Virtual Machine

↓

Program output
```

---

## What is the Python Virtual Machine?

The Python Virtual Machine (PVM) is the engine that executes Python bytecode.

It reads one instruction at a time and performs the required operation.

For example:

```python
print("Hello")
```

becomes bytecode instructions that tell the PVM to:

1. load the text,
2. call the print operation,
3. display the output.

---

## Execution order

Python executes a file **from top to bottom**.

Example:

```python
print("Step 1")

print("Step 2")

print("Step 3")
```

Output:

```text
Step 1
Step 2
Step 3
```

Python does not execute the third line before the first line.

It follows the order of the file.

---

## Why execution order matters

Execution order affects:

* variable creation,
* imports,
* function calls,
* file reading,
* database connections,
* API requests.

For example:

```python
print(data)

data = "sales"
```

Output:

```text
NameError: name 'data' is not defined
```

Python tried to execute the first line before the variable existed.

---

## What happens when the file ends?

After the last statement is executed, the program terminates.

```python
print("Done")
```

Once this line finishes, Python exits the program.

---

## Common beginner mistakes

### Mistake 1

Thinking Python directly converts code into machine code.

Correct:

Python converts source code into **bytecode**, which is executed by the **Python Virtual Machine**.

### Mistake 2

Thinking Python executes the entire file simultaneously.

Correct:

Python executes statements **one by one in sequence**.

---

## Interview note

A concise interview answer:

> When a Python file is executed, the Python interpreter reads the source code, compiles it into bytecode, and the Python Virtual Machine executes that bytecode sequentially from top to bottom.
