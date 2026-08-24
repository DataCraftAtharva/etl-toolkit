-- ============================================================
-- SQL AGGREGATION
-- COUNT / SUM / AVG / MIN / MAX / GROUP BY / HAVING
-- Dataset: data_interview
-- ============================================================
select * from orders;

select * from customers c ;
select * from products p ;
select * from shipments s  ;
select * from departments d ;
select * from payments pa ;



-- ============================================================
-- LEVEL 1 — SINGLE AGGREGATES
-- ============================================================

-- Q1.
-- How many customers are in the customers table?

select count(*)
from customers c ;


-- Q2.
-- How many orders are in the orders table?
select count(*)
from orders  ; -- if we want to include null values too

select count(order_id)
from orders o ;  -- this won't be the case since order_id is primary key

-- Q3.
-- What is the total value of all orders?
select sum(order_amount)
from orders;

-- Q4.
-- What is the average order amount?
select avg(order_amount)
from orders;

-- Q5.
-- What is the minimum and maximum product price?
select min(price) as minimum_order_price, max(price) as maximimum_order_price
from products;

-- for category wise
select category ,min(price) as minimum_order_price, max(price) as maximimum_order_price
from products
group by category ;

-- Q6.
-- How many unique cities do our customers belong to?

select city,count(*)
from customers c
group by city;

-- ============================================================
-- LEVEL 2 — WHERE + AGGREGATION
-- ============================================================

-- Q7.
-- How many orders have status = 'COMPLETED'?
--Including null
select count(*)
from orders
where order_status = 'COMPLETED';

--Without including null
select count(order_id)
from orders
where order_status = 'COMPLETED';


-- Q8.
-- What is the total value of COMPLETED orders?
select sum(order_amount)
from orders
where order_status = 'COMPLETED';

-- Q9.
-- What is the average amount of COMPLETED orders?
select AVG(order_amount)
from orders
where order_status = 'COMPLETED';

-- Q10.
-- What is the total value of orders from the customer
-- with customer_id = 2?
select sum(order_amount)
from orders
where customer_id = 2;

-- Q11.
-- How many products cost more than 10,000?
select count(*)
from products p
where p.price >10000;

-- ============================================================
-- LEVEL 3 — GROUP BY
-- ============================================================

-- Q12.
-- Count the number of customers in each city.
select city,count(*)
from customers
group by city;

-- Q13.
-- Count the number of orders for each order_status.

select order_status,count(*)
from orders
group by order_status;

-- Q14.
-- Calculate the total order value for each order_status.

select order_status,SUM(order_amount)
from orders
group by order_status;


-- Q15.
-- Calculate the average order amount for each order_status.

select order_status,AVG(order_amount)
from orders
group by order_status;

-- Q16.
-- Find the minimum and maximum order amount for each
-- order_status.
select order_status,MIN(order_amount),MAX(order_amount)
from orders
group by order_status;


-- Q17.
-- Count how many orders each customer has placed.

select customer_id,count(*)
from orders
group by customer_id;

-- ============================================================
-- LEVEL 4 — MULTIPLE AGGREGATES
-- ============================================================

-- Q18.
-- For each customer, return:
--
-- customer_id
-- number of orders
-- total order value
-- average order value

select customer_id,count(*),
MIN(order_amount),MAX(order_amount)
from orders
group by customer_id;



-- Q19.
-- For each product category, return:
--
-- category
-- number of products
-- minimum price
-- maximum price
-- average price

select category,count(*),
MIN(price),MAX(price)
from products
group by category;


-- Q20.
-- For each payment method, return:
--
-- payment_method
-- number of payments
-- total payment amount

select payment_method,count(*),
SUM(amount)
from payments
group by payment_method;


-- ============================================================
-- LEVEL 5 — HAVING
-- ============================================================

-- Q21.
-- Find customers who have placed at least 2 orders.
select customer_id,count(*)
from orders
group by customer_id
having count(*) >=2;

-- Q22.
-- Find customers whose total order value is greater
-- than 50,000.
select customer_id,sum(order_amount) as total_order_value
from orders
group by customer_id
having sum(order_amount)>50000;

-- Q23.
-- Find product categories containing more than 2 products.
select category,count(product_id)
from products
group by category
having count(product_id) > 2

-- Q24.
-- Find order statuses whose total order value is
-- greater than 50,000.
select order_status,sum(order_amount)
from orders o
group by o.order_status
having sum(order_amount) > 50000;


-- Q25.
-- Find payment methods whose total successful payment
-- amount is greater than 50,000.
select pa.payment_method,sum(amount)
from payments pa
where pa.payment_status = 'SUCCESS'
group by pa.payment_method
having sum(amount)>50000;

-- ============================================================
-- LEVEL 6 — WHERE + GROUP BY + HAVING
-- ============================================================

-- Q26.
-- For each customer, calculate the number of COMPLETED
-- orders.
select customer_id,count(*)
from orders
where order_status = 'COMPLETED'
group by customer_id;

--
-- Return only customers who have at least 2 COMPLETED orders.
select customer_id,count(*)
from orders
where order_status = 'COMPLETED'
group by customer_id
having count(*) >= 2;


-- Q27.
-- For each customer, calculate their total COMPLETED
-- order value.
--
select customer_id,sum(order_amount)
from orders
group by customer_id ;

-- Return only customers whose total COMPLETED order
-- value is greater than 50,000.
select customer_id,sum(order_amount)
from orders
group by customer_id
having sum(order_amount)>50000 ;

-- Q28.
-- For each product category, calculate the average price
-- of products costing more than 2,000.
--
select category,AVG(price)
from products
where price > 2000
group by category ;

-- Return only categories whose resulting average price
-- is greater than 5,000.
select category,AVG(price)
from products
where price > 2000
group by category
having AVG(price) >5000;

-- ============================================================
-- LEVEL 7 — BUSINESS / INTERVIEW THINKING
-- ============================================================

-- Q29.
-- Find the city with the highest number of customers.
--
-- Return:
-- city
-- customer_count
select city,count(*) as customer_count
from customers c
group by city
order by count(*) desc
limit 1;



-- Q30.
-- Find the customer with the highest total order value.
--
-- Return:
-- customer_id
-- total_order_value

select customer_id,sum(order_amount)as total_order_value
from orders o
group by customer_id
order by total_order_value desc
limit 1;


-- Q31.
-- Find the order_status with the highest average order amount.
--
-- Return:
-- order_status
-- average_order_amount

select order_status,avg(order_amount)as average_order_amount
from orders o
group by order_status
order by average_order_amount desc
limit 1;

select order_status,mavg(order_amount)as average_order_amount
from orders o
group by order_status
order by average_order_amount desc
limit 1;

-- Q32.
-- Find the product category with the highest average price.
--
-- Return:
-- category
-- average_price

select category,avg(price)as average_price
from products
group by category
order by average_price desc
limit 1;


-- Q33.
-- Calculate the percentage of all orders that are COMPLETED.
--
-- Return:
-- completed_order_count
-- total_order_count
-- completed_percentage

select count(*) FILTER(
	where order_status = 'COMPLETED'
) as completed_order_count,
count(*)  as total_order_count,
ROUND(
100.0 *
count(*) filter (
where order_status = 'COMPLETED'
) / count(*),
2
)
AS completed_percentage
FROM public.orders;



-- I did not understand this how to solve this

-- ============================================================
-- LEVEL 8 — EDGE CASES / THINKING
-- ============================================================

-- Q34.
-- What is the difference between:
--
-- COUNT(*)
-- COUNT(customer_id)
--
-- when customer_id contains NULL values?

--count(*) considers null values to but COUNT(customer_id) this does not consider null values of customer_id columns

-- Q35.
-- What happens to NULL values when using:
--
-- SUM()
-- AVG()
-- MIN()
-- MAX()
--
-- Explain in your own words.
--aggrgate function does not consider null values while doing aggregate operation since its unknown value

-- Q36.
-- Explain the difference between:
--
-- WHERE
-- and
-- HAVING
--
-- using an example from the orders table.
-- where is used when we want to filter out spcific rows based on specific column and its value for eg: customer_id = 101
-- having is used with aggregate functions to filter out the rows based specific count,sum,avg .. aggregate values

-- Q37.
-- Why can't you normally write:
--
-- SELECT customer_id, COUNT(*)
-- FROM orders;
--
-- without GROUP BY?
-- We can can not count the rows based on customer_id group if its not included in group by
--SELECT COUNT(*) FROM orders;  we can do this it calculates total rows; but when we implement SELECT customer_id, COUNT(*)
-- FROM orders; we are telling it to give count based on customer_id but it can not directly calculate that.
--

-- Q38.
-- Conceptually, in this query:
--
-- SELECT
--     customer_id,
--     COUNT(*) AS order_count
-- FROM orders
-- WHERE order_status = 'COMPLETED'
-- GROUP BY customer_id
-- HAVING COUNT(*) >= 2;
--
-- explain what happens at each stage:
--
-- FROM  - we select from which table we are selecting rows
-- WHERE  -- based on what condition we are filtering rows
-- GROUP BY -- based on these column we will create groups together of rows for eg: out of oders table if we want to calculate revenue generated by each customer so we calculate that using grouping based on customer_id and aggregate function on top of ythat
-- COUNT    -- we are using aggregate function count whcih calculates order count for each customer_id group
-- HAVING   -- we are filtering the rows based on count in which we are only selecting rows in which total_order_count across customer_id group should be atleast 2


-- ============================================================
-- AGGREGATION INTERVIEW PATTERNS
-- ============================================================


-- Q1 — SECOND HIGHEST
-- Find the second highest order_amount.
--
-- Return only:
-- order_amount
select order_amount
from orders o
order by o.order_amount desc
limit 1 offset 1;

select distinct order_amount
from orders o
order by o.order_amount desc
limit 1 offset 1;

-- Q2 — SECOND LOWEST
-- Find the second lowest product price.
--
-- Return only:
-- price

select price
from products p
order by p.price
limit 1 offset 1;


-- Q3 — THIRD HIGHEST
-- Find the third highest order_amount.
--
-- Return only:
-- order_amount

select order_amount
from orders o
order by o.order_amount desc
limit 1 offset 2;

select distinct order_amount
from orders o
order by o.order_amount desc
limit 1 offset 2;



-- Q4 — SECOND DISTINCT HIGHEST
-- Find the second highest DISTINCT product price.
--
-- Return only:
-- price

select distinct price
from products p
order by p.price desc
limit 1 offset 1;

--
-- Important:
-- Duplicate prices should count as ONE value.


-- Q5 — ALL ROWS HAVING THE HIGHEST VALUE
-- Find all orders whose order_amount is equal to
-- the highest order_amount in the orders table.
--
-- Return:
-- order_id
-- customer_id
-- order_amount

select order_id,customer_id,order_amount
from orders
where order_amount =
(select max(order_amount) from orders);


-- Q6 — TOP 3 OVERALL
-- Find the 3 most expensive products.
--
-- Return:
-- product_name
-- category
-- price

select product_name,category,price
from products p
order by p.price desc
limit 3;