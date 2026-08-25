# SELECT, FROM, WHERE, ORDER BY, LIMIT, DISTINCT

## Why this matters

These clauses form the foundation of almost every SQL query.

For basic data retrieval, think:

```text
What columns?
    ↓
SELECT

Which table?
    ↓
FROM

Which rows?
    ↓
WHERE

What order?
    ↓
ORDER BY

How many rows?
    ↓
LIMIT

Should duplicate result rows be removed?
    ↓
DISTINCT
```

---

# 1. SELECT

`SELECT` determines which columns appear in the result.

```sql
SELECT
    customer_id,
    customer_name,
    city
FROM customers;
```

Think:

```text
SELECT → What information do I want?
```

### `SELECT *`

```sql
SELECT *
FROM customers;
```

Returns all columns.

Useful for exploration, but prefer explicit columns when you know exactly what the query needs.

---

# 2. FROM

`FROM` determines the source table.

```sql
SELECT
    customer_name
FROM customers;
```

Think:

```text
FROM → Which table provides the data?
```

Later, `FROM` becomes the starting point for:

* joins
* subqueries
* CTEs
* aggregations
* more complex queries

---

# 3. WHERE

`WHERE` filters rows.

```sql
SELECT
    customer_id,
    customer_name,
    city
FROM customers
WHERE city = 'Mumbai';
```

Mental model:

```text
Table
  ↓
WHERE condition
  ↓
Keep matching rows
```

Important:

* `WHERE` filters **rows**
* `SELECT` chooses **columns**

---

# 4. Common WHERE Conditions

## Equality

```sql
WHERE city = 'Mumbai'
```

## Not equal

```sql
WHERE city <> 'Mumbai'
```

## Comparisons

```sql
WHERE price > 10000
```

```sql
WHERE price >= 10000
```

```sql
WHERE price < 10000
```

```sql
WHERE price <= 10000
```

---

# 5. AND / OR

## AND

All conditions must be true.

```sql
SELECT
    order_id,
    customer_id,
    order_amount
FROM orders
WHERE order_status = 'COMPLETED'
  AND order_amount > 20000;
```

Mental model:

```text
Condition A
    AND
Condition B

Both must be TRUE
```

## OR

At least one condition must be true.

```sql
SELECT
    customer_name,
    city
FROM customers
WHERE city = 'Mumbai'
   OR city = 'Pune';
```

Mental model:

```text
Condition A
    OR
Condition B

At least one must be TRUE
```

### Best practice

Use parentheses when combining `AND` and `OR` so the intended logic is explicit.

```sql
WHERE
    (city = 'Mumbai' OR city = 'Pune')
    AND customer_status = 'ACTIVE';
```

---

# 6. IN

`IN` is useful when comparing one column against multiple possible values.

```sql
SELECT *
FROM customers
WHERE city IN ('Mumbai', 'Pune');
```

Equivalent idea:

```sql
WHERE city = 'Mumbai'
   OR city = 'Pune';
```

For multiple values, `IN` is usually clearer.

### Mental model

```text
Is city one of these values?

Mumbai
Pune
Delhi
Bangalore
```

---

# 7. BETWEEN

`BETWEEN` checks an **inclusive range**.

```sql
SELECT
    product_name,
    price
FROM products
WHERE price BETWEEN 5000 AND 30000;
```

This means:

```text
5000 <= price <= 30000
```

Both boundaries are included.

Equivalent form:

```sql
WHERE price >= 5000
  AND price <= 30000;
```

### Important

`BETWEEN` is inclusive on both ends.

---

# 8. ORDER BY

`ORDER BY` sorts the result.

### Ascending

```sql
ORDER BY price ASC;
```

### Descending

```sql
ORDER BY price DESC;
```

`ASC` is the default.

Therefore:

```sql
ORDER BY price;
```

means:

```sql
ORDER BY price ASC;
```

Think:

```text
ORDER BY → In what order should the result appear?
```

---

# 9. Multiple ORDER BY Columns

You can sort using multiple columns.

```sql
SELECT
    customer_name,
    city
FROM customers
ORDER BY
    city ASC,
    customer_name ASC;
```

The database processes the sorting keys in order:

```text
1. Sort by city
       ↓
2. For equal cities,
   sort by customer_name
```

Example:

| customer_name | city   |
| ------------- | ------ |
| Rahul         | Mumbai |
| Zara          | Mumbai |
| Amit          | Pune   |
| Neha          | Pune   |

The first sorting key is `city`.

Then `customer_name` is used to break ties within the same city.

### Different directions

Each column can have its own direction.

```sql
ORDER BY
    city ASC,
    customer_name DESC;
```

Meaning:

```text
1. city → ascending
2. customer_name → descending within each city
```

### Mental model

```text
ORDER BY col1, col2, col3

col1 → primary sorting key
col2 → tie-breaker
col3 → next tie-breaker
```

This becomes important later for:

* ranking
* window functions
* deterministic ordering

---

# 10. LIMIT

`LIMIT` restricts the number of returned rows.

```sql
SELECT
    customer_id,
    customer_name
FROM customers
LIMIT 5;
```

This returns at most 5 rows.

## LIMIT does not mean "Top N"

This:

```sql
SELECT *
FROM products
LIMIT 5;
```

does **not** mean:

> Give me the 5 most expensive products.

To define what "top" means, use `ORDER BY`.

```sql
SELECT
    product_name,
    price
FROM products
ORDER BY price DESC
LIMIT 5;
```

Mental model:

```text
ORDER BY
    ↓
Define what "top" means
    ↓
LIMIT
    ↓
Keep N rows
```

### Important

Avoid treating this as a Top-N query:

```sql
SELECT *
FROM products
LIMIT 5;
```

Without an explicit `ORDER BY`, the database does not guarantee the desired business ordering.

---

# 11. DISTINCT

`DISTINCT` removes duplicate result rows.

```sql
SELECT DISTINCT
    city
FROM customers;
```

If many customers live in Mumbai, Mumbai appears only once.

## Multiple DISTINCT Columns

```sql
SELECT DISTINCT
    city,
    customer_name
FROM customers;
```

Uniqueness is determined by the **combination**:

```text
(city, customer_name)
```

`DISTINCT` does **not** make each column independently unique.

### Example

Suppose we have:

| customer_name | city   |
| ------------- | ------ |
| Rahul         | Mumbai |
| Rahul         | Delhi  |
| Amit          | Pune   |
| Amit          | Pune   |

Query:

```sql
SELECT DISTINCT
    customer_name,
    city
FROM customers;
```

Result:

| customer_name | city   |
| ------------- | ------ |
| Rahul         | Mumbai |
| Rahul         | Delhi  |
| Amit          | Pune   |

Only the duplicate combination:

```text
(Amit, Pune)
```

is removed.

### Mental model

```text
DISTINCT col1, col2

        ↓

Treat (col1, col2) as one combination

        ↓

Remove duplicate combinations
```

---

# 12. NULL

`NULL` represents a missing or unknown value.

Do **not** use:

```sql
WHERE delivered_at = NULL;
```

Use:

```sql
WHERE delivered_at IS NULL;
```

And:

```sql
WHERE delivered_at IS NOT NULL;
```

### Why?

Comparisons involving `NULL` produce `UNKNOWN`, not `TRUE`.

Therefore:

```sql
column = NULL
```

does not correctly identify NULL values.

Mental model:

```text
NULL is not a normal value.

Use:
    IS NULL
    IS NOT NULL
```

---

# 13. Logical Query Processing Order

The order SQL is written is not exactly the same as the logical order used to reason about a query.

For the concepts covered so far, use this mental model:

```text
FROM
  ↓
WHERE
  ↓
SELECT
  ↓
ORDER BY
  ↓
LIMIT
```

Example:

```sql
SELECT
    customer_name
FROM customers
WHERE city = 'Mumbai'
ORDER BY customer_name
LIMIT 3;
```

Think:

```text
1. Get rows from customers
        ↓
2. Keep Mumbai rows
        ↓
3. Return customer_name
        ↓
4. Sort by customer_name
        ↓
5. Keep first 3
```

### Important clarification

This is a **logical processing model**, not necessarily the exact physical execution order used internally by the database engine.

The optimizer may choose a different physical execution plan.

---

# 14. Common Patterns

| Requirement                 | SQL Pattern                      |
| --------------------------- | -------------------------------- |
| Select specific columns     | `SELECT`                         |
| Select all columns          | `SELECT *`                       |
| Filter rows                 | `WHERE`                          |
| Multiple allowed values     | `IN`                             |
| Range                       | `BETWEEN` / comparison operators |
| Combine required conditions | `AND`                            |
| Match either condition      | `OR`                             |
| Sort ascending              | `ORDER BY ... ASC`               |
| Sort descending             | `ORDER BY ... DESC`              |
| Multiple sorting keys       | `ORDER BY col1, col2`            |
| Top N                       | `ORDER BY ... LIMIT`             |
| Unique result values        | `DISTINCT`                       |
| Missing value               | `IS NULL`                        |
| Non-missing value           | `IS NOT NULL`                    |

---

# 15. Business Examples

## Mumbai Customers

```sql
SELECT
    customer_id,
    customer_name
FROM customers
WHERE city = 'Mumbai';
```

---

## High-Value Completed Orders

```sql
SELECT
    order_id,
    customer_id,
    order_amount
FROM orders
WHERE order_status = 'COMPLETED'
  AND order_amount > 20000;
```

---

## Top 5 Products by Price

```sql
SELECT
    product_name,
    price
FROM products
ORDER BY price DESC
LIMIT 5;
```

---

## Unique Cities

```sql
SELECT DISTINCT
    city
FROM customers;
```

---

## Undelivered Shipments

```sql
SELECT
    shipment_id,
    order_id,
    shipment_status
FROM shipments
WHERE delivered_at IS NULL;
```

---

# 16. Common Interview Mistakes

## Mistake 1 — Missing a Requirement

Question:

> Find completed orders above 20,000.

You need both conditions:

```sql
WHERE order_status = 'COMPLETED'
  AND order_amount > 20000;
```

Don't accidentally write only:

```sql
WHERE order_amount > 20000;
```

because that also returns non-completed orders.

---

## Mistake 2 — Wrong Table or Column

Before writing SQL, translate the question into:

```text
1. Which table?
2. Which columns?
3. Which filters?
4. Which ordering?
5. How many rows?
```

Then write the query.

---

## Mistake 3 — LIMIT Without ORDER BY

This:

```sql
LIMIT 5
```

only limits the number of rows.

It does not define which rows are the "best", "highest", "latest", or "top".

For example:

```sql
ORDER BY price DESC
LIMIT 5;
```

means:

> Give me the 5 highest-priced products.

---

## Mistake 4 — `= NULL`

Wrong:

```sql
WHERE delivered_at = NULL;
```

Correct:

```sql
WHERE delivered_at IS NULL;
```

---

## Mistake 5 — Misunderstanding DISTINCT

This:

```sql
SELECT DISTINCT
    city,
    customer_name
FROM customers;
```

means uniqueness is determined by:

```text
(city, customer_name)
```

It does **not** mean:

```text
unique cities
+
unique customer names
```

---

## Mistake 6 — Misunderstanding Multiple ORDER BY Columns

This:

```sql
ORDER BY city, customer_name;
```

does **not** mean:

```text
sort cities independently
AND
sort names independently
```

It means:

```text
1. Sort by city
2. For equal cities, sort by customer_name
```

---

# 17. Interview Checklist

Before submitting a basic SQL query, verify:

* [ ] Did I choose the correct table?
* [ ] Did I select only the required columns?
* [ ] Did I apply every required filter?
* [ ] Did I use `AND` / `OR` correctly?
* [ ] Should I use `IN` for multiple allowed values?
* [ ] Is the range inclusive when using `BETWEEN`?
* [ ] Do I need `IS NULL` / `IS NOT NULL`?
* [ ] Do I need `ORDER BY`?
* [ ] If there is a Top-N requirement, did I use `ORDER BY` before `LIMIT`?
* [ ] If I used multiple `ORDER BY` columns, is the priority correct?
* [ ] If I used `DISTINCT`, am I removing duplicate combinations intentionally?

---

# 18. Core Mental Model

For the foundation queries, remember:

```text
SELECT
    ↓
What columns?

FROM
    ↓
Which table?

WHERE
    ↓
Which rows?

ORDER BY
    ↓
What order?

LIMIT
    ↓
How many rows?

DISTINCT
    ↓
Which duplicate result rows should be removed?
```

The most important distinction:

```text
SELECT  → columns
WHERE   → rows
ORDER BY → order
LIMIT   → number of rows
DISTINCT → duplicate result rows
```

---

# 19. Foundation Summary

At this stage, you should be comfortable writing:

```sql
SELECT columns
FROM table
WHERE condition
ORDER BY column
LIMIT n;
```

And you should understand the supporting patterns:

```sql
AND
OR
IN
BETWEEN
IS NULL
IS NOT NULL
DISTINCT
```

These are the building blocks for the next major SQL pattern:

```text
SELECT / WHERE
        ↓
AGGREGATION
        ↓
GROUP BY
        ↓
HAVING
        ↓
Aggregate analysis
```

# Additional SQL Filtering Notes

## `NOT`, `LIKE`, `NOT LIKE`, and Filtering Mental Model

---

# 1. `NOT`

`NOT` reverses the result of a condition.

For example:

```sql
SELECT
    customer_id,
    customer_name,
    city
FROM customers
WHERE NOT city = 'Mumbai';
```

This means:

> Keep customers whose city is not Mumbai.

---

## `NOT` with `IN`

You can use `NOT` with `IN`.

```sql
WHERE NOT city IN ('Mumbai', 'Pune');
```

This means:

> Keep customers whose city is neither Mumbai nor Pune.

A more common and readable form is:

```sql
WHERE city NOT IN ('Mumbai', 'Pune');
```

Therefore:

```sql
NOT city IN (...)
```

and:

```sql
city NOT IN (...)
```

express the same filtering idea.

---

## `NOT` with `LIKE`

`NOT` can also be used with pattern matching.

For example:

```sql
WHERE customer_name NOT LIKE 'A%';
```

This means:

> Keep customers whose names do not start with `A`.

---

## `NOT` vs `<>` vs `NOT IN`

These are related, but they should not be treated as identical in every situation.

### Single value

```sql
WHERE city <> 'Mumbai';
```

or:

```sql
WHERE NOT city = 'Mumbai';
```

Both express:

> City is not Mumbai.

### Multiple values

```sql
WHERE city NOT IN ('Mumbai', 'Pune');
```

This means:

> City is neither Mumbai nor Pune.

### Pattern

```sql
WHERE customer_name NOT LIKE 'A%';
```

This means:

> Customer name does not match the pattern `A%`.

### Mental model

```text
NOT
 │
 ├── NOT condition
 │
 ├── NOT IN
 │
 └── NOT LIKE
```

`NOT` is the general logical operator.

`NOT IN` and `NOT LIKE` are specialized SQL filtering forms.

---

# 2. `LIKE`

`LIKE` is used for **pattern-based string matching**.

It is useful when you don't know the exact value you are looking for.

For example, instead of:

```sql
WHERE customer_name = 'Atharva';
```

you can search for a pattern:

```sql
WHERE customer_name LIKE 'Ath%';
```

This can match names beginning with `Ath`.

---

# LIKE Wildcards

The two important wildcards for Day 1 are:

| Wildcard | Meaning |
|---|---|
| `%` | Zero or more characters |
| `_` | Exactly one character |

---

## `%` — Zero or More Characters

The `%` wildcard represents zero or more characters.

---

### Starts with

```sql
WHERE customer_name LIKE 'A%';
```

Meaning:

> Starts with `A`.

Possible matches:

```text
Amit
Anjali
Atharva
Arjun
```

Mental model:

```text
A + anything
```

```text
A%
```

---

### Ends with

```sql
WHERE customer_name LIKE '%a';
```

Meaning:

> Ends with `a`.

Mental model:

```text
anything + a
```

```text
%a
```

---

### Contains

```sql
WHERE customer_name LIKE '%an%';
```

Meaning:

> Contains `an` anywhere in the string.

Mental model:

```text
anything + an + anything
```

```text
%an%
```

---

# `_` — Exactly One Character

The underscore `_` matches exactly one character.

Example:

```sql
WHERE customer_name LIKE 'A____';
```

This means:

```text
A + exactly 4 characters
```

Therefore, the total length is **5 characters**.

Mental model:

```text
A _ _ _ _
```

Each `_` represents exactly one character.

---

# Multiple Underscores

For example:

```sql
WHERE customer_name LIKE '_____';
```

means:

```text
Exactly 5 characters
```

because there are five `_` characters.

---

# Combining `%` and `_`

You can combine the wildcards.

Example:

```sql
WHERE customer_name LIKE 'A___%';
```

Meaning:

```text
Starts with A
+
at least 3 additional characters
+
anything after that
```

You don't need to memorize complicated patterns at this stage.

The important thing is understanding:

```text
% → zero or more characters
_ → exactly one character
```

---

# `NOT LIKE`

`NOT LIKE` finds values that do not match a pattern.

Example:

```sql
SELECT
    customer_id,
    customer_name
FROM customers
WHERE customer_name NOT LIKE 'A%';
```

Meaning:

> Customers whose names do not start with `A`.

Another example:

```sql
SELECT
    product_id,
    product_name
FROM products
WHERE product_name NOT LIKE '%Phone%';
```

Meaning:

> Products whose names do not contain `Phone`.

---

# 3. Filtering Mental Model

Think about SQL filtering like this:

```text
                    TABLE
                      │
                      ↓
                   WHERE
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
      Exact value    Range      Pattern
          │           │           │
          ↓           ↓           ↓
          =         BETWEEN      LIKE
          <>        > <          NOT LIKE
          IN        >= <=
          NOT IN
                      │
                      ↓
                 Filtered Rows
```

The main question is:

> **What kind of condition am I trying to express?**

---

## Exact values

Use `=` when matching one specific value.

```sql
WHERE city = 'Mumbai';
```

Meaning:

> Keep rows where the city is exactly Mumbai.

---

## Multiple values

Use `IN` when matching one of several specific values.

```sql
WHERE city IN ('Mumbai', 'Pune');
```

Meaning:

> Keep rows where the city is either Mumbai or Pune.

---

## Excluding values

Use `NOT IN` when excluding multiple specific values.

```sql
WHERE city NOT IN ('Mumbai', 'Pune');
```

Meaning:

> Keep rows where the city is neither Mumbai nor Pune.

---

## Numeric range

Use `BETWEEN` when filtering within a range.

```sql
WHERE price BETWEEN 5000 AND 30000;
```

Meaning:

> Keep rows where the price is between 5,000 and 30,000.

---

## String pattern

Use `LIKE` when the requirement is based on a string pattern.

```sql
WHERE customer_name LIKE 'A%';
```

Meaning:

> Keep customers whose names start with `A`.

---

## Missing value

Use `IS NULL` when checking for a missing value.

```sql
WHERE delivered_at IS NULL;
```

Meaning:

> Keep rows where `delivered_at` has no value.

To find rows where the value exists:

```sql
WHERE delivered_at IS NOT NULL;
```

---

# 4. Quick Filtering Decision Guide

| Requirement | SQL Pattern |
|---|---|
| Exactly one value | `=` |
| Not equal to one value | `<>` |
| One of several values | `IN (...)` |
| None of several values | `NOT IN (...)` |
| Greater than | `>` |
| Less than | `<` |
| Greater than or equal | `>=` |
| Less than or equal | `<=` |
| Within a range | `BETWEEN ... AND ...` |
| Starts with | `LIKE 'A%'` |
| Ends with | `LIKE '%a'` |
| Contains | `LIKE '%an%'` |
| Does not match pattern | `NOT LIKE 'A%'` |
| Missing value | `IS NULL` |
| Value exists | `IS NOT NULL` |

---

# 5. Core Mental Model

When reading an SQL interview question, identify the type of filtering requirement first.

```text
                Filtering Requirement
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   Exact value         Range           Pattern
        │                │                │
        ↓                ↓                ↓
    = / <>          > < >= <=          LIKE
    IN / NOT IN     BETWEEN            NOT LIKE
        │
        ↓
   Missing value
        │
        ↓
 IS NULL / IS NOT NULL
```

The goal is not to memorize queries.

The goal is to recognize:

```text
"What type of filter does the business requirement need?"
```

Then choose the appropriate SQL operator.

---

# 6. Day 1 — What You Should Know

For Day 1, focus primarily on these patterns:

```text
= 
<>
IN (...)
NOT IN (...)
BETWEEN ... AND ...
LIKE '...'
NOT LIKE '...'
IS NULL
IS NOT NULL
```

The most important pattern recognition is:

```text
Exact value
    ↓
=

Multiple allowed values
    ↓
IN (...)

Multiple excluded values
    ↓
NOT IN (...)

Range
    ↓
BETWEEN / comparison operators

String pattern
    ↓
LIKE

Exclude string pattern
    ↓
NOT LIKE

Missing value
    ↓
IS NULL

Existing value
    ↓
IS NOT NULL
```

---

# Key Takeaway

SQL filtering becomes much easier when you stop thinking:

> "Which SQL syntax do I need to memorize?"

and start thinking:

> "What type of condition am I trying to express?"

```text
Exact?
    → =

Not equal?
    → <>

One of these?
    → IN

None of these?
    → NOT IN

Range?
    → BETWEEN / > / < / >= / <=

Starts with?
    → LIKE 'A%'

Ends with?
    → LIKE '%a'

Contains?
    → LIKE '%abc%'

Does not match?
    → NOT LIKE

Missing?
    → IS NULL

Not missing?
    → IS NOT NULL
```

**Next topic: Aggregation — `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, and `GROUP BY`.**
