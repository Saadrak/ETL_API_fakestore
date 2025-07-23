def load_users(df,conn):
    try:
        df.to_sql('Users', conn, if_exists='replace', index=False)

    except Exception as e:
        print(f"[ERROR][load_users]: {e}")