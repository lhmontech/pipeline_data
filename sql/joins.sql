-- quantity of reviews by product
SELECT
    p.product_name,
    COUNT(r.review_id) AS total_reviews
FROM products p
LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY p.product_name
ORDER BY total_reviews DESC
LIMIT 10;

-- average rating of most commented products
SELECT
    p.product_name,
    ROUND(AVG(p.rating), 2) AS avg_rating,
    COUNT(r.review_id) AS total_reviews
FROM products p
JOIN reviews r ON p.product_id = r.product_id
GROUP BY p.product_name
HAVING total_reviews >= 10
ORDER BY total_reviews DESC;
