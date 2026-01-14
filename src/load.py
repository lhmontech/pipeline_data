import sqlite3

def load_data(products_df, reviews_df, db_path):
    print('[LOAD] Connecting to database')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print('[LOAD] Creating table if not exists')

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
           product_id TEXT PRIMARY KEY,
           product_name TEXT,
           category TEXT,
           discounted_price REAL,
           actual_price REAL,
           discount_percentage REAL,
           rating REAL,
           rating_count REAL,
           about_product TEXT,
           img_link TEXT,
           product_link TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id TEXT PRIMARY KEY,
            product_id TEXT,
            user_id TEXT,
            user_name TEXT,
            review_title TEXT,
            review_content TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)
    print('[LOAD] Inserting data into table')

    products_df.to_sql('products', conn, if_exists = 'append', index = False)
    reviews_df.to_sql('reviews', conn, if_exists = 'append', index = False)


    conn.commit()
    conn.close()

    print(f'[LOAD] Load completed | {len(products_df)} rows inserted in products and {len(reviews_df)} rows inserted in reviews')