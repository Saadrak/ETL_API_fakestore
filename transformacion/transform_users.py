import pandas as pd

def clean_users(df):
    try:
        adress_df= pd.json_normalize(df['address'])
        adress_df= adress_df.apply(lambda col:col.str.lower() if col.dtype == 'object' else col)
        
        name_df= pd.json_normalize(df['name'])
        name_df= name_df.rename(columns={'firstname': 'first_name', 'lastname': 'last_name'})
        
        clean_df= df.drop(columns=['address','name']).reset_index(drop=True) \
                                                    .join(name_df) \
                                                    .join(adress_df)
        return clean_df
    except Exception as e:
        print(f"[ERROR][transform_users]: {e}")
