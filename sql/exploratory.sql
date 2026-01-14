-- avaible categories
SELECT DISTINCT category
FROM products
ORDER BY category;

-- rating distribution
SELECT
    ROUND(rating, 1) AS rating_value,
    COUNT(*) AS total
FROM products
GROUP BY rating_value
ORDER BY rating_value DESC;

-- top 10 most rated products
SELECT
    product_name,
    rating_count
FROM products
ORDER BY rating_count DESC
LIMIT 10;
