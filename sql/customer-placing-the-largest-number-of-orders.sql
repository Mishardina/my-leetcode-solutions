--https://leetcode.com/problems/customer-placing-the-largest-number-of-orders

SELECT customer_number FROM orders
GROUP BY customer_number
HAVING COUNT(DISTINCT order_number) IN (
    SELECT MAX(cnt) FROM (SELECT COUNT(distinct order_number) AS cnt FROM orders
    GROUP BY customer_number) AS T
)