USE ecommerce_project;

-- Total Customers
SELECT COUNT(*) FROM customer_churn;

-- Count of Churned customers
SELECT COUNT(*) FROM customer_churn WHERE Churn = 1;

-- Customers by segment [Inactive Customers, Good Customers, Low Value Customers, Best Customers]
SELECT Segment, COUNT(*) 
FROM customer_churn
GROUP BY Segment;
