import os
from extract import extract_data
from transform import treat_data
from load import load_data

def main():
    print('[PIPELINE] Starting pipeline')

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_path = os.path.join(base_dir, 'data', 'raw_data.csv')
    db_path = os.path.join(base_dir, 'database', 'pipeline.db')

    df = extract_data(csv_path)
    products_df, reviews_df = treat_data(df)
    load_data(products_df, reviews_df, db_path)

    print('[PIPELINE] Pipeline finished successfully')

if __name__ == '__main__':
    main()
