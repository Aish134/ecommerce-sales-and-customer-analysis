
-- 1. Check total customer records
SELECT COUNT(*) AS total_records
FROM customers;

-- 2. Find the top 10 states
SELECT
    customer_state,
    COUNT(*) AS customer_records
FROM customers
GROUP BY customer_state
ORDER BY customer_records DESC
LIMIT 10;

-- 3. Count unique customers
SELECT
    COUNT(DISTINCT customer_unique_id) AS unique_customers
FROM customers;
