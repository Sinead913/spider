import json
import mysql.connector
import sqlalchemy

with open('article.json') as json_data: d=json.load(json_data)
  
  
db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        user="root",
        password="password",
        database="spiderIndexer"
        query={"unix_socket": "/cloudsql/cloudcomputing3032:us-central1:spiderindexer",
    ),
)

conn.execute(students.insert(), [
   {'name':'Rajiv', 'lastname' : 'Khanna'},
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])

for page in d:
  conn.execute(students.insert(), page)
               
