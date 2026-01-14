-- average rating by category
SELECT
    category,
    ROUND(AVG(rating), 2) AS avg_rating
FROM products
GROUP BY category
ORDER BY avg_rating DESC;

-- average descount by category
SELECT
    category,
    ROUND(AVG(discount_percentage) * 100, 2) AS avg_discount_percent
FROM products
GROUP BY category
ORDER BY avg_discount_percent DESC;

-- products with the biggest absolute discount
SELECT
    product_name,
    discount_percentage * 100 AS discount_percent
FROM products
ORDER BY discount_percentage DESC
LIMIT 10;
