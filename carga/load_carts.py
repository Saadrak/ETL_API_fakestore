def load_carts(df,conn):
    try:
        df.to_sql('Carts', conn, if_exists='replace', index=False)
        
    except Exception as e:
        print(f"[ERROR][load_carts]: {e}")    