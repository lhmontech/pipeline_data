-- total products
SELECT COUNT(*) AS total_products FROM products;

-- total reviews
SELECT COUNT(*) AS total_reviews FROM reviews;

-- products without category (quality problems)
SELECT COUNT(*) AS products_without_category
FROM products
WHERE category IS NULL OR category = '';

-- reviews withou a product associated (integrity)
SELECT COUNT(*) AS orphan_reviews
FROM reviews r
LEFT JOIN products p ON r.product_id = p.product_id
WHERE p.product_id IS NULL;
