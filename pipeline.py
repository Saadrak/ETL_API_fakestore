from config.database import get_connection

from extracion.fecht_products import get_products
from transformacion.transform_products import clean_products
from carga.load_products import load_products

from extracion.fecht_user import get_users
from transformacion.transform_users import clean_users
from carga.load_users import load_users

from extracion.fecht_carts import get_carts
from transformacion.transform_carts import clean_carts
from carga.load_carts import load_carts


def etl_products():
    conn=get_connection()
    df_raw_products = get_products()           
    df_clean_products = clean_products(df_raw_products)  
    df_load_products = load_products(df_clean_products,conn)
    conn.close()
    print("ETL products ejecutada sin problemas.")

def etl_users():
    conn=get_connection()
    df_fecht_users= get_users()
    df_clean_users= clean_users(df_fecht_users)
    df_load_users= load_users(df_clean_users,conn)
    conn.close()
    print("ETL users ejecutada sin problemas.")
    
def etl_carts():
    conn=get_connection()
    df_fecht_carts= get_carts()
    df_clean_carts= clean_carts(df_fecht_carts)
    df_load_carts= load_carts(df_clean_carts,conn)
    conn.close()
    print("ETL carts cargaba sin problemas")



