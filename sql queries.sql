
-- Day 13: Sales Analysis Queries

-- 1. Sales by Region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 2. Sales by Category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 3. Profit by Segment
SELECT
    Segment,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Segment
ORDER BY Total_Profit DESC;
