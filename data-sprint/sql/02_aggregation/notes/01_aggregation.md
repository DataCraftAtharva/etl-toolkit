# SQL Aggregation

## Why this matters

Aggregation is how SQL answers questions such as:

* How many customers do we have?
* What is the total revenue?
* What is the average order value?
* Which city has the most customers?
* Which product category generates the most revenue?
* Which groups meet a business condition?

The core aggregation functions are:

```text
COUNT
SUM
AVG
MIN
MAX
```

The two clauses that make aggregation useful are:

```text
GROUP BY
HAVING
```

### Central mental model

```text
Rows
  ↓
(optional WHERE)
  ↓
GROUP BY
  ↓
Aggregation
  ↓
HAVING
  ↓
Result
```

---

# 1. COUNT

`COUNT` counts rows or non-NULL values depending on what you count.

## Count all rows

```sql
SELECT COUNT(*) AS customer_count
FROM customers;
```

This counts every row.

With our dataset:

```text
10 customers
```

## Count a column

```sql
SELECT COUNT(customer_id) AS customer_count
FROM customers;
```

If `customer_id` is `NOT NULL`, this also returns:

```text
10
```

## Important distinction

```text
COUNT(*)
    ↓
Counts rows

COUNT(column)
    ↓
Counts non-NULL values
```

This distinction becomes important when NULL values exist.

---

# 2. COUNT(DISTINCT ...)

Use `COUNT(DISTINCT column)` to count unique values.

```sql
SELECT COUNT(DISTINCT city) AS city_count
FROM customers;
```

This answers:

> How many unique cities do our customers come from?

Mental model:

```text
DISTINCT
    ↓
Unique values
    ↓
COUNT
    ↓
Number of unique values
```

For example:

```text
Mumbai
Mumbai
Pune
Pune
Delhi
```

After `DISTINCT`:

```text
Mumbai
Pune
Delhi
```

Then `COUNT` returns:

```text
3
```

---

# 3. SUM

`SUM` adds numeric values.

```sql
SELECT SUM(order_amount) AS total_order_value
FROM orders;
```

This gives the total order value.

Common business metrics:

* Revenue
* Sales
* Quantity
* Cost
* Discounts
* Transaction value

Mental model:

```text
100
200
300
400
 ↓
SUM
 ↓
1000
```

---

# 4. AVG

`AVG` calculates the average of non-NULL numeric values.

```sql
SELECT AVG(order_amount) AS average_order_value
FROM orders;
```

Conceptually:

```text
SUM of non-NULL values
----------------------
COUNT of non-NULL values
```

For example:

```text
100
200
300
```

Then:

```text
AVG = (100 + 200 + 300) / 3
    = 200
```

### Important

`AVG` ignores NULL values.

If the values are:

```text
100
200
NULL
300
```

The average is:

```text
(100 + 200 + 300) / 3
= 200
```

It does **not** divide by 4.

---

# 5. MIN and MAX

## Minimum

```sql
SELECT MIN(price) AS minimum_price
FROM products;
```

## Maximum

```sql
SELECT MAX(price) AS maximum_price
FROM products;
```

Typical business questions:

```text
Cheapest product
Most expensive product
Earliest order
Latest order
Lowest salary
Highest salary
```

For numeric or date/time columns, `MIN` and `MAX` are commonly used.

---

# 6. Aggregation Without GROUP BY

When there is no `GROUP BY`, the entire filtered result is treated as **one group**.

```sql
SELECT
    COUNT(*) AS order_count,
    SUM(order_amount) AS total_value,
    AVG(order_amount) AS average_order_value,
    MIN(order_amount) AS minimum_order_value,
    MAX(order_amount) AS maximum_order_value
FROM orders;
```

Conceptually:

```text
All matching rows
       ↓
    ONE GROUP
       ↓
 ┌─────┼─────┬─────┬─────┐
 ↓     ↓     ↓     ↓     ↓
COUNT SUM   AVG   MIN   MAX
```

This is useful for overall business KPIs.

Example:

```text
Total orders
Total revenue
Average order value
Minimum order
Maximum order
```

---

# 7. WHERE + Aggregation

`WHERE` filters rows **before** aggregation.

Example:

```sql
SELECT
    COUNT(*) AS completed_orders,
    SUM(order_amount) AS completed_value
FROM orders
WHERE order_status = 'COMPLETED';
```

Mental model:

```text
All orders
    ↓
WHERE order_status = 'COMPLETED'
    ↓
Remaining rows
    ↓
Aggregate
```

This distinction is extremely important.

### Think:

```text
WHERE
    ↓
Which rows should participate?

Aggregation
    ↓
What should I calculate from those rows?
```

---

# 8. GROUP BY

`GROUP BY` creates separate groups.

Example:

```sql
SELECT
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

Conceptually:

```text
Customers
    ↓
Group by city
    ↓
┌─────────────┐
│ Mumbai      │
├─────────────┤
│ Pune        │
├─────────────┤
│ Delhi       │
└─────────────┘
    ↓
COUNT each group
```

Example result:

| city   | customer_count |
| ------ | -------------: |
| Mumbai |              4 |
| Pune   |              3 |
| Delhi  |              3 |

Each city becomes one group.

### Key mental model

```text
GROUP BY X
    ↓
One result row per X
```

For example:

```text
GROUP BY city
```

means:

```text
One result row per city
```

---

# 9. GROUP BY with Multiple Aggregates

You can calculate several metrics for each group.

```sql
SELECT
    order_status,
    COUNT(*) AS order_count,
    SUM(order_amount) AS total_value,
    AVG(order_amount) AS average_value,
    MIN(order_amount) AS minimum_value,
    MAX(order_amount) AS maximum_value
FROM orders
GROUP BY order_status;
```

Conceptually:

```text
orders
   ↓
GROUP BY order_status
   ↓
┌─────────────┐
│ COMPLETED   │
│ PENDING     │
│ CANCELLED   │
└─────────────┘
   ↓
Calculate metrics for each group
```

Example result:

| order_status | order_count | total_value | average_value |
| ------------ | ----------: | ----------: | ------------: |
| COMPLETED    |          20 |      500000 |         25000 |
| PENDING      |           5 |       80000 |         16000 |
| CANCELLED    |           3 |       45000 |         15000 |

---

# 10. GROUP BY Multiple Columns

You can group by more than one dimension.

Example:

```sql
SELECT
    city,
    signup_date,
    COUNT(*) AS customer_count
FROM customers
GROUP BY
    city,
    signup_date;
```

The grouping key becomes:

```text
(city, signup_date)
```

Think of it as a composite grouping key.

```text
Mumbai + 2026-01-01
Mumbai + 2026-01-02
Pune   + 2026-01-01
Pune   + 2026-01-02
```

Each unique combination becomes a separate group.

### Connection to DISTINCT

This:

```sql
SELECT DISTINCT
    city,
    signup_date
FROM customers;
```

identifies unique combinations.

While:

```sql
SELECT
    city,
    signup_date,
    COUNT(*) AS customer_count
FROM customers
GROUP BY
    city,
    signup_date;
```

identifies the same grouping combinations **and calculates metrics for each group**.

---

# 11. HAVING

`HAVING` filters **groups after aggregation**.

Example:

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

This answers:

> Which customers placed at least 2 orders?

Mental model:

```text
Rows
  ↓
GROUP BY customer_id
  ↓
COUNT orders
  ↓
HAVING COUNT(*) >= 2
  ↓
Keep qualifying groups
```

### Key distinction

```text
WHERE
    ↓
Filters rows

HAVING
    ↓
Filters groups
```

---

# 12. WHERE vs HAVING

This is one of the most important SQL interview concepts.

## WHERE

Filters individual rows:

```sql
WHERE order_status = 'COMPLETED'
```

## HAVING

Filters groups:

```sql
HAVING COUNT(*) >= 2
```

Mental model:

```text
WHERE
  ↓
Before grouping

GROUP BY
  ↓
Create groups

HAVING
  ↓
After grouping
```

### Example

```sql
SELECT
    customer_id,
    COUNT(*) AS completed_orders
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

Process:

```text
All orders
    ↓
Keep completed orders
    ↓
Group by customer
    ↓
Count each customer
    ↓
Keep customers with >= 2 orders
```

---

# 13. NULL Behavior in Aggregation

NULL handling matters in aggregation.

## COUNT(*)

Counts rows, including rows containing NULL values.

```sql
COUNT(*)
```

## COUNT(column)

Counts only non-NULL values.

```sql
COUNT(delivered_at)
```

For example:

| delivered_at |
| ------------ |
| 2026-08-01   |
| 2026-08-02   |
| NULL         |
| 2026-08-04   |

Then:

```sql
COUNT(*)
```

returns:

```text
4
```

But:

```sql
COUNT(delivered_at)
```

returns:

```text
3
```

## SUM / AVG / MIN / MAX

These aggregate functions generally ignore NULL inputs.

For example:

```text
100
200
NULL
300
```

Then:

```text
SUM = 600
AVG = 200
MIN = 100
MAX = 300
```

NULL is **not automatically treated as zero**.

If business logic requires NULL to behave as zero, you must explicitly handle it, commonly with `COALESCE`.

```sql
SELECT
    SUM(COALESCE(discount_amount, 0)) AS total_discount
FROM orders;
```

---

# 14. Business Examples

## Total Number of Customers

```sql
SELECT
    COUNT(*) AS customer_count
FROM customers;
```

---

## Total Order Value

```sql
SELECT
    SUM(order_amount) AS total_order_value
FROM orders;
```

---

## Average Completed Order

```sql
SELECT
    AVG(order_amount) AS average_completed_order
FROM orders
WHERE order_status = 'COMPLETED';
```

---

## Orders by Status

```sql
SELECT
    order_status,
    COUNT(*) AS order_count
FROM orders
GROUP BY order_status;
```

---

## Revenue by Status

```sql
SELECT
    order_status,
    SUM(order_amount) AS total_value
FROM orders
GROUP BY order_status;
```

---

## Customers with at Least Two Orders

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

---

# 15. Common Mistakes

## Mistake 1 — Using WHERE for Aggregate Results

Incorrect:

```sql
WHERE COUNT(*) >= 2
```

Correct:

```sql
HAVING COUNT(*) >= 2
```

Why?

Because `COUNT(*)` is calculated at the **group level**.

Therefore, the condition belongs in `HAVING`.

---

## Mistake 2 — Forgetting GROUP BY

Suppose you want one result per customer.

Incorrect:

```sql
SELECT
    customer_id,
    COUNT(*)
FROM orders;
```

`customer_id` is not aggregated and is not grouped.

Correct:

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id;
```

### Rule

When using aggregation, every selected expression should generally be either:

```text
An aggregate
```

or:

```text
Included in GROUP BY
```

---

## Mistake 3 — Confusing COUNT(*) and COUNT(column)

Remember:

```text
COUNT(*)
    ↓
Counts rows

COUNT(column)
    ↓
Counts non-NULL values
```

---

## Mistake 4 — Treating NULL as Zero

NULL means:

```text
Missing / unknown
```

It does not automatically mean:

```text
0
```

If you need zero behavior, explicitly define it:

```sql
COALESCE(column, 0)
```

---

## Mistake 5 — Forgetting the Grouping Grain

Always ask:

> What does one output row represent?

For:

```sql
GROUP BY customer_id
```

one output row represents:

```text
One customer
```

For:

```sql
GROUP BY city
```

one output row represents:

```text
One city
```

For:

```sql
GROUP BY city, order_status
```

one output row represents:

```text
One city + one order status combination
```

This concept of **grain** becomes extremely important in data engineering.

---

# 16. Pattern Recognition

When you see:

| Requirement                   | Think                    |
| ----------------------------- | ------------------------ |
| "How many?"                   | `COUNT`                  |
| "Total?"                      | `SUM`                    |
| "Average?"                    | `AVG`                    |
| "Lowest?"                     | `MIN`                    |
| "Highest?"                    | `MAX`                    |
| "per customer"                | `GROUP BY customer_id`   |
| "per city"                    | `GROUP BY city`          |
| "per status"                  | `GROUP BY order_status`  |
| "at least N" after grouping   | `HAVING`                 |
| "filter rows before grouping" | `WHERE`                  |
| "unique values"               | `COUNT(DISTINCT column)` |

### The key recognition pattern

Whenever you see:

```text
"per X"
```

think:

```text
GROUP BY X
```

Example:

> Revenue per product category

Immediately think:

```sql
GROUP BY category
```

Then decide which metric is required:

```sql
SUM(revenue)
```

---

# 17. Aggregation Execution Mental Model

For basic SQL reasoning, use:

```text
FROM
  ↓
WHERE
  ↓
GROUP BY
  ↓
Aggregate functions
  ↓
HAVING
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
    city,
    COUNT(*) AS customer_count
FROM customers
WHERE customer_status = 'ACTIVE'
GROUP BY city
HAVING COUNT(*) >= 2
ORDER BY customer_count DESC
LIMIT 5;
```

Think:

```text
1. FROM
   Get customers

2. WHERE
   Keep active customers

3. GROUP BY
   Create one group per city

4. COUNT
   Count customers in each city

5. HAVING
   Keep cities with at least 2 customers

6. SELECT
   Return city and customer_count

7. ORDER BY
   Highest count first

8. LIMIT
   Keep top 5 cities
```

> Note: This is a **logical reasoning model**, not necessarily the exact physical execution plan used by the database optimizer.

---

# 18. Data Engineering Connection

Aggregation is everywhere in data engineering.

Common examples:

```text
Daily revenue
Orders per customer
Events per user
Records per partition
Average processing time
Error count by pipeline
Transactions per merchant
```

For example, a daily revenue pipeline might conceptually perform:

```text
Raw orders
    ↓
Filter valid orders
    ↓
Group by order date
    ↓
SUM(order_amount)
    ↓
Daily revenue table
```

Aggregation also becomes important in distributed systems.

In PySpark:

```python
df.groupBy("customer_id").count()
```

can require a **shuffle** because records belonging to the same customer may exist on different partitions.

Conceptually:

```text
Large Dataset
      ↓
groupBy
      ↓
Shuffle
      ↓
Records with same key
      ↓
Aggregation
```

This becomes important later when learning:

* PySpark `groupBy`
* Shuffle
* Partitioning
* Data skew
* Aggregation optimization

For now, focus on SQL correctness and grouping logic.

---

# 19. The Most Important Aggregation Patterns

## Pattern 1 — Overall metric

```sql
SELECT
    SUM(order_amount) AS total_revenue
FROM orders;
```

Think:

```text
No GROUP BY
    ↓
One overall result
```

---

## Pattern 2 — Metric per group

```sql
SELECT
    customer_id,
    SUM(order_amount) AS customer_revenue
FROM orders
GROUP BY customer_id;
```

Think:

```text
"revenue per customer"
        ↓
GROUP BY customer_id
```

---

## Pattern 3 — Filter rows before aggregation

```sql
SELECT
    customer_id,
    SUM(order_amount) AS completed_revenue
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id;
```

Think:

```text
WHERE
  ↓
Filter rows
  ↓
GROUP BY
  ↓
Aggregate
```

---

## Pattern 4 — Filter groups after aggregation

```sql
SELECT
    customer_id,
    SUM(order_amount) AS total_revenue
FROM orders
GROUP BY customer_id
HAVING SUM(order_amount) > 50000;
```

Think:

```text
GROUP BY
  ↓
SUM
  ↓
HAVING
  ↓
Keep groups above 50,000
```

---

## Pattern 5 — Top groups

```sql
SELECT
    customer_id,
    SUM(order_amount) AS total_revenue
FROM orders
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;
```

Think:

```text
GROUP BY
    ↓
Calculate metric
    ↓
ORDER BY metric
    ↓
LIMIT
```

This pattern appears constantly in SQL interviews.

---

# 20. Interview Checklist

Before writing an aggregation query, ask:

* [ ] Am I calculating a metric?
* [ ] What aggregation function do I need?
* [ ] Am I calculating one overall result or one result per group?
* [ ] If per group, what is the grouping key?
* [ ] What does one output row represent?
* [ ] Do I need to filter rows before grouping?
* [ ] If yes, should I use `WHERE`?
* [ ] Do I need to filter groups after aggregation?
* [ ] If yes, should I use `HAVING`?
* [ ] Are NULL values relevant?
* [ ] Should I use `COUNT(*)` or `COUNT(column)`?
* [ ] Do I need `COUNT(DISTINCT column)`?
* [ ] Do I need `ORDER BY` after aggregation?
* [ ] If I need Top-N groups, did I use `ORDER BY ... LIMIT`?

---

# 21. Core Mental Model

For aggregation problems, remember:

```text
SELECT
    ↓
What should I return?

FROM
    ↓
Where does the data come from?

WHERE
    ↓
Which rows participate?

GROUP BY
    ↓
How should rows be grouped?

COUNT / SUM / AVG / MIN / MAX
    ↓
What metric should I calculate?

HAVING
    ↓
Which groups should remain?

ORDER BY
    ↓
How should the groups be ranked?

LIMIT
    ↓
How many results do I need?
```

The most important distinction:

```text
WHERE
    → filters rows

GROUP BY
    → creates groups

Aggregate functions
    → calculate metrics

HAVING
    → filters groups
```

---

# 22. Foundation Summary

At this stage, you should be comfortable writing:

```sql
SELECT
    grouping_column,
    AGGREGATE_FUNCTION(metric_column) AS metric
FROM table
WHERE row_condition
GROUP BY grouping_column
HAVING aggregate_condition
ORDER BY metric DESC
LIMIT n;
```

Not every query needs every clause.

The key is recognizing the business requirement and selecting only the clauses you need.

### The progression

```text
SELECT / WHERE
      ↓
Filtering
      ↓
COUNT / SUM / AVG / MIN / MAX
      ↓
Aggregation
      ↓
GROUP BY
      ↓
Per-group metrics
      ↓
HAVING
      ↓
Filter groups
      ↓
ORDER BY + LIMIT
      ↓
Top-N analysis
```

**Next topic: SQL Joins — `INNER JOIN`, `LEFT JOIN`, join keys, unmatched rows, and one-to-many relationships.**
