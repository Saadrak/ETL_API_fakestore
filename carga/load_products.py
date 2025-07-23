def load_products(df,conn):
    try:
        df.to_sql('Products', conn, if_exists='replace', index=False)

    except Exception as e:
        print(f"[ERROR][load_products]: {e}")