import pandas as pd
import requests

def get_users():
    try:
        url="https://fakestoreapi.com/users"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"[ERROR][fecht_users]: {e}")


