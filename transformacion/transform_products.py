import pandas as pd

def clean_products(df):
    try:
        rating_df= pd.json_normalize(df['rating'])

        rating_df = rating_df.rename(columns={'rate': 'rating', 'count': 'rating_count'})
        clean_df= df.drop(columns=['rating']).join(rating_df)
        return clean_df
    except Exception as e:
        print(f"[ERROR][transform_products]: {e}")
