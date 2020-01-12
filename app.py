import json
import mysql.connector

with open('article.json') as json_data: d=json.load(json_data)

db_connection = mysql.connector.connect(
  socketPath="/cloudsql/cloudcomputing3032:us-central1:spiderindexer",
  user="root",
  passwd="password",
  database="spiderIndexer"
  )
db_cursor = db_connection.cursor()

for page in d:
  sqlInputQuery = 'INSERT INTO webpages VALUES (' + page['URL'] + ', ' + page['webContent'] + ');'
  db_cursor.execute(sqlInputQuery)

db_connection.commit()
