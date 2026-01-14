import pandas as pd

def extract_data(csv_path):
    print('[EXTRACT] Starting data extraction')

    df = pd.read_csv(csv_path)

    print(f'[EXTRACT] Extraction completed | {len(df)} records found')

    return df