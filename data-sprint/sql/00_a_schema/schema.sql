-- ============================================================
-- DATA INTERVIEW DATABASE
-- Schema Definition
-- PostgreSQL
-- ============================================================

-- Clean practice schema
DROP TABLE IF EXISTS public.events CASCADE;
DROP TABLE IF EXISTS public.employees CASCADE;
DROP TABLE IF EXISTS public.departments CASCADE;
DROP TABLE IF EXISTS public.shipments CASCADE;
DROP TABLE IF EXISTS public.payments CASCADE;
DROP TABLE IF EXISTS public.order_items CASCADE;
DROP TABLE IF EXISTS public.orders CASCADE;
DROP TABLE IF EXISTS public.products CASCADE;
DROP TABLE IF EXISTS public.customers CASCADE;


-- ============================================================
-- CUSTOMERS
-- ============================================================

CREATE TABLE public.customers (
    customer_id BIGINT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(200) NOT NULL,
    city VARCHAR(100),
    signup_date DATE NOT NULL
);


-- ============================================================
-- PRODUCTS
-- ============================================================

CREATE TABLE public.products (
    product_id BIGINT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price NUMERIC(12, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL
);


-- ============================================================
-- ORDERS
-- ============================================================

CREATE TABLE public.orders (
    order_id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    order_date TIMESTAMP NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    order_amount NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES public.customers(customer_id)
);


-- ============================================================
-- ORDER ITEMS
-- ============================================================

CREATE TABLE public.order_items (
    order_item_id BIGINT PRIMARY KEY,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES public.orders(order_id),

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES public.products(product_id)
);


-- ============================================================
-- PAYMENTS
-- ============================================================

CREATE TABLE public.payments (
    payment_id BIGINT PRIMARY KEY,
    order_id BIGINT NOT NULL,
    payment_date TIMESTAMP NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(30) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_payments_order
        FOREIGN KEY (order_id)
        REFERENCES public.orders(order_id)
);


-- ============================================================
-- SHIPMENTS
-- ============================================================

CREATE TABLE public.shipments (
    shipment_id BIGINT PRIMARY KEY,
    order_id BIGINT NOT NULL,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    shipment_status VARCHAR(30) NOT NULL,

    CONSTRAINT fk_shipments_order
        FOREIGN KEY (order_id)
        REFERENCES public.orders(order_id)
);


-- ============================================================
-- DEPARTMENTS
-- ============================================================

CREATE TABLE public.departments (
    department_id BIGINT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


-- ============================================================
-- EMPLOYEES
-- ============================================================

CREATE TABLE public.employees (
    employee_id BIGINT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id BIGINT,
    manager_id BIGINT,
    salary NUMERIC(12, 2),
    hire_date DATE,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES public.departments(department_id),

    CONSTRAINT fk_employee_manager
        FOREIGN KEY (manager_id)
        REFERENCES public.employees(employee_id)
);


-- ============================================================
-- EVENTS
-- ============================================================

CREATE TABLE public.events (
    event_id BIGINT PRIMARY KEY,
    customer_id BIGINT,
    event_type VARCHAR(50) NOT NULL,
    event_timestamp TIMESTAMP NOT NULL,

    CONSTRAINT fk_events_customer
        FOREIGN KEY (customer_id)
        REFERENCES public.customers(customer_id)
);