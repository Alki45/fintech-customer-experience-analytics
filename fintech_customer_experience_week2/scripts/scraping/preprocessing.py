import pandas as pd
import os
from glob import glob

def load_raw_reviews(folder='data/raw/'):
    all_files = glob(os.path.join(folder, '*.csv'))
    dfs = [pd.read_csv(f) for f in all_files]
    return pd.concat(dfs, ignore_index=True)

def preprocess_reviews(df):
    df.drop_duplicates(subset=['review_text'], inplace=True)
    df.dropna(subset=['review_text', 'rating', 'date'], inplace=True)
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    return df

if __name__ == '__main__':
    df = load_raw_reviews()
    df = preprocess_reviews(df)
    df.to_csv('data/processed/cleaned_reviews.csv', index=False)
    print("✅ Preprocessing complete. Saved to data/processed/cleaned_reviews.csv")
