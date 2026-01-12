USE ecommerce_project;

-- Total Customers
SELECT COUNT(*) AS total_customers
FROM customer_churn;

-- Churn Rate
SELECT 
    (SUM(Churn) / COUNT(*)) * 100 AS churn_percentage
FROM customer_churn;

-- Active And Churned Customers
SELECT 
    CASE 
        WHEN Churn = 1 THEN 'Churned'
        ELSE 'Active'
    END AS customer_status,
    COUNT(*) AS total_customers
FROM customer_churn
GROUP BY customer_status;

-- Customers By Segment
SELECT Segment, COUNT(*) AS total_customers
FROM customer_churn
GROUP BY Segment
ORDER BY total_customers DESC;

-- Top Value Customers
SELECT CustomerID, Monetary
FROM customer_churn
ORDER BY Monetary DESC
LIMIT 10;

