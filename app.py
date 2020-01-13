import json
import mysql.connector
import sqlalchemy
import pymysql

with open('article.json') as json_data: d=json.load(json_data)
  
  
db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        user="root",
        password="password",
        database="spiderIndexer",
        query={"unix_socket": "/cloudsql/cloudcomputing3032:us-central1:spiderindexer"},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,  # 30 seconds
    pool_recycle=1800,  # 30 minutes
)

conn = engine.connect()

for page in d:
  conn.execute(webpages.insert(), page)
               
