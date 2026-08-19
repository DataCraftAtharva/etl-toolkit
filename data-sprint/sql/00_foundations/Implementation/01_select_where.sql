
-- ============================================================
-- SQL FOUNDATIONS
-- Topic: SELECT / FROM / WHERE / ORDER BY / LIMIT / DISTINCT
-- Dataset: data_interview
-- ============================================================


-- ============================================================
-- 1. SELECT
-- ============================================================

-- Return selected customer columns.

SELECT
    customer_id,
    customer_name,
    city
FROM public.customers;


-- Return all customer columns when full-row inspection is needed.

SELECT *
FROM public.customers;


-- ============================================================
-- 2. WHERE
-- ============================================================

-- Customers who live in Mumbai.

SELECT
    customer_id,
    customer_name,
    city
FROM public.customers
WHERE city = 'Mumbai';


-- Products with price greater than 10,000.

SELECT
    product_id,
    product_name,
    category,
    price
FROM public.products
WHERE price > 10000;


-- Completed orders.

SELECT
    order_id,
    customer_id,
    order_date,
    order_amount
FROM public.orders
WHERE order_status = 'COMPLETED';


-- ============================================================
-- 3. AND / OR
-- ============================================================

-- Completed orders with amount greater than 20,000.

SELECT
    order_id,
    customer_id,
    order_status,
    order_amount
FROM public.orders
WHERE order_status = 'COMPLETED'
  AND order_amount > 20000;


-- Customers from Mumbai or Pune.

SELECT
    customer_id,
    customer_name,
    city
FROM public.customers
WHERE city IN ('Mumbai', 'Pune');


-- ============================================================
-- 4. BETWEEN
-- ============================================================

-- Products priced between 5,000 and 30,000.
-- BETWEEN is inclusive of both boundaries.

SELECT
    product_id,
    product_name,
    category,
    price
FROM public.products
WHERE price BETWEEN 5000 AND 30000;


-- Equivalent comparison form:

SELECT
    product_id,
    product_name,
    category,
    price
FROM public.products
WHERE price >= 5000
  AND price <= 30000;


-- ============================================================
-- 5. ORDER BY
-- ============================================================

-- Electronics products from highest to lowest price.

SELECT
    product_id,
    product_name,
    price
FROM public.products
WHERE category = 'Electronics'
ORDER BY price DESC;


-- Products from lowest to highest price.

SELECT
    product_id,
    product_name,
    price
FROM public.products
ORDER BY price ASC;


-- Multiple sort columns.

SELECT
    customer_name,
    city
FROM public.customers
ORDER BY city ASC,
         customer_name ASC;


-- ============================================================
-- 6. LIMIT + ORDER BY
-- ============================================================

-- Five most expensive products.

SELECT
    product_id,
    product_name,
    price
FROM public.products
ORDER BY price DESC
LIMIT 5;


-- Five most recent orders.

SELECT
    order_id,
    customer_id,
    order_date,
    order_amount
FROM public.orders
ORDER BY order_date DESC
LIMIT 5;


-- Three cheapest Electronics products.

SELECT
    product_id,
    product_name,
    price
FROM public.products
WHERE category = 'Electronics'
ORDER BY price ASC
LIMIT 3;


-- Three highest-value completed orders.

SELECT
    order_id,
    customer_id,
    order_date,
    order_amount
FROM public.orders
WHERE order_status = 'COMPLETED'
ORDER BY order_amount DESC
LIMIT 3;


-- ============================================================
-- 7. DISTINCT
-- ============================================================

-- Unique customer cities.

SELECT DISTINCT
    city
FROM public.customers;


-- Unique city + customer name combinations.

SELECT DISTINCT
    city,
    customer_name
FROM public.customers
ORDER BY city,
         customer_name;


-- ============================================================
-- 8. NULL HANDLING
-- ============================================================

-- Shipments that have not been delivered yet.

SELECT
    shipment_id,
    order_id,
    shipment_status,
    delivered_at
FROM public.shipments
WHERE delivered_at IS NULL;


-- Shipments that have not yet been shipped.

SELECT
    shipment_id,
    order_id,
    shipment_status,
    shipped_at
FROM public.shipments
WHERE shipped_at IS NULL;


-- Shipments that have been delivered.

SELECT
    shipment_id,
    order_id,
    shipment_status,
    delivered_at
FROM public.shipments
WHERE delivered_at IS NOT NULL;


-- ============================================================
-- 9. NOT / <>
-- ============================================================

-- Customers who are not from Mumbai.

SELECT
    customer_id,
    customer_name,
    city
FROM public.customers
WHERE city <> 'Mumbai';


-- Products that are not in Accessories.

SELECT
    product_id,
    product_name,
    category,
    price
FROM public.products
WHERE category <> 'Accessories';


-- ============================================================
-- 10. CORE BUSINESS QUERY
-- ============================================================

-- Latest five completed orders above 20,000.

SELECT
    order_id,
    customer_id,
    order_date,
    order_amount
FROM public.orders
WHERE order_status = 'COMPLETED'
  AND order_amount > 20000
ORDER BY order_date DESC
LIMIT 5;