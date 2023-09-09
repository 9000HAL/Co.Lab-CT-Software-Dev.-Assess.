import psycopg2
from flask import Flask
import requests

app = Flask(__name__)



# Database configuration
DATABASE_URL = "postgres://tagzmraj:U7pLZTuQTLxrKR5Dzd0E70awv1WzJPkv@bubble.db.elephantsql.com/tagzmraj"



@app.route('/')
def home():

# Fetch data from an example API: JSONPlaceholder
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    api_data = response.json()

    return render_template('index.html', api_data=api_data)


    # Connect to PostgreSQL
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    conn.close()
    return f"Connected to PostgreSQL version: {version[0]}"

if __name__ == "__main__":
    app.run(debug=True)
