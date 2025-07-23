import pandas as pd

def clean_carts(df):
    try:
        df['date']=pd.to_datetime(df['date'])
        df= df.rename(columns={'date':'cart_date'})
        explode_carts= df.explode('products').reset_index(drop=True)
        carts_df= pd.json_normalize(explode_carts['products'])
        clean_df= explode_carts.drop(columns=['products']).join(carts_df)
        return clean_df
        
    except Exception as e:
        print(f"[ERROR][transform_carts]: {e}")
        
        