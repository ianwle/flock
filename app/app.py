from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

if __name__ == '__main__':
	conn = psycopg2.connect(
		host="localhost",
		database="postgres",
		user="airflow",
		password="airflow")

	cur = conn.cursor()
	
	# Execute a query
	cur.execute("""SELECT * FROM public.\"Events\"""")

	# Retrieve query results
	records = cur.fetchall()
	headers = cur.description
	
	# app.run(host='0.0.0.0')
	