# Proyecto Pipeline ETL modular utilizando API fakestore

Este proyecto implementa una pipeline ETL modular utilizando Pandas, Sqlite y dato provenientes de la API publica de [FakeStoreAPI](https://fakestoreapi.com)
Se realiza la extracion, transformacion(limpieza y normalizacion) y la carga a una base de datos local
ademas, se incluye el archivo SQL con las consultas realizadas para analisis

## Tecnologias 
-Pandas(Python)
-SQLite
-Request
-FakeStoreAPI

## Estructura del proyecto
/config: Script de conexion con sqlite, base de datos y archivo SQL con consultas realizadas
/extracion: Scripts de extracion para users, products y carts
/transformacion: Scripts de transformacion(limpieza y normalizacion) para users, products y carts
/carga: Scripts de carga para users, products y carts
/pipeline.py: Modulo que integra y ejecuta todas las etapas del pipeline
/main.py: Script principal que ejecuta el pipeline completo


## intalar dependencias

pip install -r requirements.txt

## ejecutar proyecto

python main.py



