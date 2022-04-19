from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
CORS(app)

DB_USER = "airflow"
DB_PWD = "airflow"
DB_DATABASE = "postgres"
DB_HOST = "localhost"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://{user}:{password}@{host}/{database}".format(user=DB_USER, password=DB_PWD, host=DB_HOST, database=DB_DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route('/')
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
