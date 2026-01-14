def treat_data(df):
    print('[TRANSFORM] Starting data treatment')
    #remove empty lines
    df = df.dropna(subset=['product_name'])

    #remove duplicates
    df = df.drop_duplicates()

    #standardize text
    for col in ['product_name', 'category', 'about_product']:
        if col in df.columns:
            df[col] = df[col].str.strip().str.upper()

    #adjusting the data type
    # Prices
    for col in ['discounted_price', 'actual_price']:
        if col in df.columns:
            df[col] = (
                df[col]
                .str.replace(r'[^\d\.]', '', regex=True)
                .astype(float)
            )

    # Percentage
    if 'discount_percentage' in df.columns:
        df['discount_percentage'] = (
            df['discount_percentage']
            .str.replace('%', '')
            .astype(float)
            / 100
        )

    # Rating
    if 'rating' in df.columns:
        df['rating'] = (
            df['rating']
            .str.extract(r'(\d+\.?\d*)')
            .astype(float)
        )

    # Rating count
    if 'rating_count' in df.columns:
        df['rating_count'] = (
            df['rating_count']
            .str.replace(',', '')
            .astype(float)
        )

    print(f'[TRANSFORM] Treatment completed | {len(df)} rows')
    products_df = df[
        [
            'product_id',
            'product_name',
            'category',
            'discounted_price',
            'actual_price',
            'discount_percentage',
            'rating',
            'rating_count',
            'about_product',
            'img_link',
            'product_link'
        ]
    ].drop_duplicates(subset=['product_id'])

    reviews_df = df[
        [
            'review_id',
            'product_id',
            'user_id',
            'user_name',
            'review_title',
            'review_content'
        ]
    ].drop_duplicates(subset=['review_id'])

    return products_df, reviews_df