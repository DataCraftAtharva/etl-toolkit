# SQL Aggregation

## Why this matters

Aggregation converts many rows into useful business metrics.

Typical questions:

- How many customers are there?
- What is the total revenue?
- What is the average order value?
- How many orders does each customer have?
- Which categories have the highest sales?
- Which customers have placed at least 2 orders?

Core aggregate functions:

```text
COUNT
SUM
AVG
MIN
MAX
```

Core clauses:

```text
GROUP BY
HAVING
```

The main mental model is:

```text
Rows
  ↓
WHERE          ← filter rows
  ↓
GROUP BY       ← create groups
  ↓
Aggregate      ← calculate metrics
  ↓
HAVING         ← filter groups
  ↓
ORDER BY       ← sort result
  ↓
LIMIT          ← keep top N
```

---

# 1. `COUNT`

## Count all rows

```sql
SELECT COUNT(*) AS customer_count
FROM customers;
```

`COUNT(*)` counts rows.

It does not care whether a particular column contains `NULL`.

---

## Count a column

```sql
SELECT COUNT(customer_id)
FROM customers;
```

`COUNT(column)` counts only rows where that column is **not `NULL`**.

### Important distinction

```text
COUNT(*)
→ number of rows

COUNT(column)
→ number of non-NULL values in that column
```

Example:

```text
customer_id
-----------
1
2
NULL
3
```

Then:

```text
COUNT(*)           = 4
COUNT(customer_id) = 3
```

---

## Count distinct values

```sql
SELECT COUNT(DISTINCT city) AS unique_city_count
FROM customers;
```

Use this when the question asks:

> How many unique cities are there?

Do not confuse this with:

```sql
GROUP BY city
```

Because:

```text
COUNT(DISTINCT city)
→ returns one number

GROUP BY city + COUNT(*)
→ returns one row per city
```

---

# 2. `SUM`

`SUM` calculates a total.

```sql
SELECT SUM(order_amount) AS total_order_value
FROM orders;
```

Common business uses:

```text
revenue
sales
cost
quantity
payment amount
```

Mental mapping:

```text
"total"
   ↓
SUM(...)
```

---

# 3. `AVG`

`AVG` calculates an average.

```sql
SELECT AVG(order_amount) AS average_order_value
FROM orders;
```

Conceptually:

```text
SUM(non-NULL values)
--------------------
COUNT(non-NULL values)
```

`NULL` inputs are ignored.

Mental mapping:

```text
"average"
    ↓
AVG(...)
```

---

# 4. `MIN` and `MAX`

```sql
SELECT
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products;
```

Typical questions:

```text
lowest price
highest price
earliest date
latest date
lowest salary
highest salary
```

Mental mapping:

```text
lowest
  ↓
MIN

highest
  ↓
MAX
```

---

# 5. Aggregation Without `GROUP BY`

Without `GROUP BY`, all matching rows are treated as **one group**.

```sql
SELECT
    COUNT(*) AS order_count,
    SUM(order_amount) AS total_value,
    AVG(order_amount) AS average_value,
    MIN(order_amount) AS minimum_value,
    MAX(order_amount) AS maximum_value
FROM orders;
```

Mental model:

```text
All rows
   ↓
ONE group
   ↓
Calculate multiple metrics
   ↓
One result row
```

This is useful for overall business KPIs.

For example:

```text
Total orders
Total revenue
Average order value
Minimum order value
Maximum order value
```

---

# 6. `WHERE` + Aggregation

`WHERE` filters rows **before** aggregation.

```sql
SELECT
    COUNT(*) AS completed_order_count,
    SUM(order_amount) AS completed_order_value
FROM orders
WHERE order_status = 'COMPLETED';
```

Think:

```text
All orders
    ↓
WHERE order_status = 'COMPLETED'
    ↓
Keep completed orders
    ↓
Aggregate remaining rows
```

Important:

```text
WHERE
→ filters rows before grouping/aggregation
```

---

# 7. `GROUP BY`

`GROUP BY` creates separate groups.

Example:

```sql
SELECT
    city,
    COUNT(*) AS customer_count
FROM customers
GROUP BY city;
```

Mental model:

```text
customers
    ↓
GROUP BY city
    ↓
Mumbai group
Pune group
Delhi group
...
    ↓
COUNT each group
```

### Key interview trigger

If the question says:

> "per customer"

Think:

```sql
GROUP BY customer_id
```

If it says:

> "per city"

Think:

```sql
GROUP BY city
```

If it says:

> "per category"

Think:

```sql
GROUP BY category
```

The important question is:

> One result for each **what**?

That usually tells you the grouping column.

---

# 8. Multiple Aggregates Per Group

You can calculate several metrics for each group.

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count,
    SUM(order_amount) AS total_order_value,
    AVG(order_amount) AS average_order_value
FROM orders
GROUP BY customer_id;
```

Translate the English requirement:

```text
number
→ COUNT

total
→ SUM

average
→ AVG

lowest
→ MIN

highest
→ MAX
```

Mental model:

```text
Orders
   ↓
GROUP BY customer_id
   ↓
Customer 1 → COUNT, SUM, AVG
Customer 2 → COUNT, SUM, AVG
Customer 3 → COUNT, SUM, AVG
```

---

# 9. `GROUP BY` Multiple Columns

You can group by multiple dimensions.

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

The grouping key is the combination:

```text
(city, signup_date)
```

Conceptually:

```text
Same city
+
Same signup_date
=
One group
```

For example:

```text
Mumbai | 2026-01-01
Mumbai | 2026-01-01
→ same group

Mumbai | 2026-01-02
→ different group

Pune | 2026-01-01
→ different group
```

---

# 10. `HAVING`

`HAVING` filters groups **after aggregation**.

Example:

```sql
SELECT
    customer_id,
    COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

Meaning:

```text
Orders
  ↓
GROUP BY customer_id
  ↓
COUNT orders per customer
  ↓
HAVING COUNT(*) >= 2
  ↓
Keep only matching groups
```

This returns customers who have placed at least 2 orders.

---

# 11. `WHERE` vs `HAVING`

This is one of the most important SQL interview concepts.

## `WHERE`

Filters individual rows.

Example:

```sql
WHERE order_status = 'COMPLETED'
```

Think:

```text
Check each row
↓
Keep/remove row
```

---

## `HAVING`

Filters groups after aggregation.

Example:

```sql
HAVING COUNT(*) >= 2
```

Think:

```text
Create groups
↓
Calculate aggregate
↓
Keep/remove group
```

---

## Example Using Both

```sql
SELECT
    customer_id,
    COUNT(*) AS completed_order_count
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

Mental model:

```text
All orders
    ↓
WHERE completed
    ↓
Only completed orders
    ↓
GROUP BY customer
    ↓
COUNT completed orders
    ↓
HAVING count >= 2
    ↓
Final result
```

Remember:

```text
WHERE
→ row-level filtering

HAVING
→ group-level filtering
```

---

# 12. Full Aggregation Pattern

A very common query shape is:

```sql
SELECT
    grouping_column,
    aggregate_function(...)
FROM table
WHERE row_condition
GROUP BY grouping_column
HAVING aggregate_function(...) condition
ORDER BY ...
LIMIT ...;
```

Example:

```sql
SELECT
    customer_id,
    SUM(order_amount) AS total_completed_value
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id
HAVING SUM(order_amount) > 50000
ORDER BY total_completed_value DESC;
```

Read it in logical order:

```text
1. Read orders
2. Keep completed orders
3. Group them by customer
4. Calculate total order value
5. Keep customers above 50,000
6. Sort by total value descending
```

This pattern is extremely important for interviews.

---

# 13. Conditional Aggregation

Conditional aggregation means calculating an aggregate only for rows matching a condition.

Example:

> What percentage of all orders are completed?

Think:

```text
completed orders
---------------- × 100
all orders
```

In PostgreSQL:

```sql
SELECT
    COUNT(*) FILTER (
        WHERE order_status = 'COMPLETED'
    ) AS completed_order_count,

    COUNT(*) AS total_order_count,

    ROUND(
        100.0 *
        COUNT(*) FILTER (
            WHERE order_status = 'COMPLETED'
        ) / COUNT(*),
        2
    ) AS completed_percentage
FROM orders;
```

Mental model:

```text
All orders
    ↓
Count completed orders
    ↓
Count all orders
    ↓
completed / total × 100
    ↓
Percentage
```

---

## Portable Conditional Aggregation Pattern

A common portable SQL pattern uses `CASE`.

```sql
SUM(
    CASE
        WHEN order_status = 'COMPLETED' THEN 1
        ELSE 0
    END
)
```

Think:

```text
COMPLETED
→ 1

Not COMPLETED
→ 0

SUM
→ total completed orders
```

Common uses:

```text
completion rate
failure rate
success rate
conversion rate
percentage by status
conditional revenue
```

---

# 14. `NULL` Behavior

For common aggregates:

```text
SUM
AVG
MIN
MAX
```

`NULL` inputs are generally ignored.

Do not think of:

```text
NULL
```

as:

```text
0
```

Example:

```text
Values:

100
200
NULL
300
```

Then:

```text
SUM = 600
AVG = 200
```

The `NULL` value is ignored.

If all values reaching an aggregate are `NULL`, the aggregate result can itself be `NULL`.

Later we will learn:

```sql
COALESCE(...)
```

when an explicit fallback value is required.

---

# 15. Aggregation Interview Patterns

Aggregation questions often become ranking questions.

## Highest Value

```sql
SELECT
    order_amount
FROM orders
ORDER BY order_amount DESC
LIMIT 1;
```

Pattern:

```text
Highest
↓
ORDER BY DESC
↓
LIMIT 1
```

---

## Lowest Value

```sql
SELECT
    order_amount
FROM orders
ORDER BY order_amount ASC
LIMIT 1;
```

Pattern:

```text
Lowest
↓
ORDER BY ASC
↓
LIMIT 1
```

---

## Top N Overall

```sql
SELECT
    product_name,
    category,
    price
FROM products
ORDER BY price DESC
LIMIT 3;
```

Think:

```text
Top N overall
→ ORDER BY DESC
→ LIMIT N
```

---

# 16. Nth Highest / Lowest

For simple sorted-position problems:

```text
Nth highest
→ DESC
→ LIMIT 1
→ OFFSET N - 1
```

Example: second highest:

```sql
SELECT
    order_amount
FROM orders
ORDER BY order_amount DESC
LIMIT 1 OFFSET 1;
```

Third highest:

```sql
SELECT
    order_amount
FROM orders
ORDER BY order_amount DESC
LIMIT 1 OFFSET 2;
```

---

## Nth Lowest

Pattern:

```text
Nth lowest
→ ASC
→ LIMIT 1
→ OFFSET N - 1
```

Example: second lowest:

```sql
SELECT
    order_amount
FROM orders
ORDER BY order_amount ASC
LIMIT 1 OFFSET 1;
```

---

# 17. Distinct Nth Highest

This is different from the Nth sorted row.

Suppose the values are:

```text
100
100
90
80
```

Sorted rows:

```text
1 → 100
2 → 100
3 → 90
4 → 80
```

Distinct values:

```text
1 → 100
2 → 90
3 → 80
```

For the second distinct highest value:

```sql
SELECT DISTINCT
    order_amount
FROM orders
ORDER BY order_amount DESC
LIMIT 1 OFFSET 1;
```

### Important interview distinction

```text
Nth row
≠
Nth distinct value
```

Always read the wording carefully.

---

# 18. Return All Rows Having the Highest Value

Suppose the question says:

> Find all orders having the highest amount.

Do not use:

```sql
ORDER BY order_amount DESC
LIMIT 1;
```

Because that returns only one row.

Instead:

```sql
SELECT
    order_id,
    customer_id,
    order_amount
FROM orders
WHERE order_amount = (
    SELECT MAX(order_amount)
    FROM orders
);
```

Mental model:

```text
MAX()
  ↓
Find highest value
  ↓
Compare every row against that value
  ↓
Return all matching rows
```

This handles ties.

Example:

```text
order_id | order_amount
---------+-------------
1        | 1000
2        | 5000
3        | 5000
4        | 3000
```

Both order `2` and order `3` are returned.

---

# 19. Top N Overall vs Top N Per Group

These are different interview patterns.

## Top 3 Overall

```sql
ORDER BY price DESC
LIMIT 3
```

Meaning:

```text
One global Top 3
```

---

## Top 3 Per Category

Meaning:

```text
Electronics → Top 3
Accessories → Top 3
Furniture   → Top 3
...
```

`LIMIT 3` cannot solve this requirement.

This usually requires a window function:

```sql
ROW_NUMBER() OVER (
    PARTITION BY category
    ORDER BY price DESC
)
```

Then:

```sql
row_number <= 3
```

For now, remember:

> `Top N per group` is a window-function pattern.

We will study it formally in Window Functions.

---

# 20. Highest / Lowest Per Group

Example:

> Find the highest-paid employee in each department.

Recognize:

```text
for each department
↓
group/partition by department
```

And:

```text
highest
↓
descending salary
```

This is also commonly solved using window functions.

For now, recognize the pattern.

---

# 21. Above / Below Average Pattern

Example:

> Find customers whose total order value is above the average customer total.

Break it down:

```text
Step 1
Calculate total per customer

        ↓

Step 2
Calculate average of customer totals

        ↓

Step 3
Compare each customer total
against that average
```

This typically needs:

```text
CTE
or
subquery
```

We will study this pattern later.

---

# 22. Pattern Recognition Table

| Interview wording | Think |
|---|---|
| How many? | `COUNT` |
| Total? | `SUM` |
| Average? | `AVG` |
| Lowest? | `MIN` |
| Highest? | `MAX` |
| Per customer | `GROUP BY customer_id` |
| Per city | `GROUP BY city` |
| At least N | `HAVING COUNT(...) >= N` |
| Total above X | `HAVING SUM(...) > X` |
| Top N | `ORDER BY DESC LIMIT N` |
| Nth highest | `DESC + OFFSET` |
| Nth lowest | `ASC + OFFSET` |
| Nth distinct highest | `DISTINCT + DESC + OFFSET` |
| All rows tied for max | `MAX()` + filter |
| Top N per group | Window function |
| Highest per group | Window function |
| Conditional percentage | Conditional aggregation |
| Above average | CTE / subquery |

---

# 23. Interview Decision Framework

Before writing an aggregation query, ask:

```text
1. What metric is required?

2. Is this one overall result
   or one result per group?

3. What rows should be filtered
   before aggregation?

4. What grouping key is required?

5. Do I need HAVING?

6. Are NULL values relevant?

7. Is this actually a ranking problem?

8. Are duplicates or ties important?

9. Do I need one value
   or all matching rows?

10. Is this Top N overall
    or Top N per group?
```

---

# 24. Common Mistakes

## Mistake 1 — Confusing unique count with grouping

Question:

> How many unique cities?

Use:

```sql
SELECT COUNT(DISTINCT city)
FROM customers;
```

This is different from:

> How many customers are there per city?

Which requires:

```sql
SELECT
    city,
    COUNT(*)
FROM customers
GROUP BY city;
```

---

## Mistake 2 — Forgetting a required filter

Requirement:

> Find completed order value.

The query must include:

```sql
WHERE order_status = 'COMPLETED'
```

when that condition is part of the requirement.

---

## Mistake 3 — Using the wrong aggregate

Translate English carefully:

```text
number
→ COUNT

total
→ SUM

average
→ AVG

lowest
→ MIN

highest
→ MAX
```

---

## Mistake 4 — Using `LIMIT 1` when all tied rows are required

This:

```sql
ORDER BY order_amount DESC
LIMIT 1
```

returns one row.

If all rows tied for the maximum are required, use:

```text
MAX()
+
filter the original table
```

or a ranking approach depending on the requirement.

---

## Mistake 5 — Using `LIMIT N` for Top-N-per-group

This:

```sql
ORDER BY price DESC
LIMIT 3;
```

returns the global Top 3.

It does not return Top 3 for every category.

Top-N-per-group is a window-function pattern.

---

# 25. What We Have Mastered

```text
COUNT                   ✅
COUNT(DISTINCT)         ✅
SUM                     ✅
AVG                     ✅
MIN                     ✅
MAX                     ✅

WHERE + aggregate       ✅
GROUP BY                ✅
Multiple aggregates     ✅
HAVING                  ✅
WHERE + GROUP BY
      + HAVING          ✅

Conditional aggregation ✅

Top N overall           ✅
Nth highest             ✅
Nth lowest              ✅
Nth distinct            ✅
All rows at MAX         ✅

Top N per group
→ recognize now
→ learn formally with window functions

Ties / ranking
→ recognize now
→ learn formally with window functions

Above average
→ recognize now
→ learn with CTE / subquery
```

---

# 26. Core Takeaway

Do not memorize individual SQL queries.

Learn this mapping:

```text
Business requirement
        ↓
Pattern
        ↓
SQL structure
```

For example:

```text
"Customers with at least 2 completed orders"
        ↓
Filter completed rows
        ↓
GROUP BY customer
        ↓
COUNT orders
        ↓
HAVING count >= 2
```

Which becomes:

```sql
SELECT
    customer_id,
    COUNT(*) AS completed_order_count
FROM orders
WHERE order_status = 'COMPLETED'
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

The goal is to look at a business question and immediately identify:

```text
What rows?
→ WHERE

One result per what?
→ GROUP BY

What metric?
→ COUNT / SUM / AVG / MIN / MAX

Which groups should remain?
→ HAVING

How should the result be ranked?
→ ORDER BY

How many rows should be returned?
→ LIMIT
```