# Description: Flask App for API     v.2

import psycopg2
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Database configuration
DATABASE_URL = "postgres://tagzmraj:U7pLZTuQTLxrKR5Dzd0E70awv1WzJPkv@bubble.db.elephantsql.com/tagzmraj"

@app.route('/')
def home():

    # Fetch multiple data items from an example API: JSONPlaceholder
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    api_data = response.json()[0:3]  # Fetch first 3 todo items
    
    # Connect to PostgreSQL
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    conn.close()

    return render_template('index.html', api_data=api_data, version=version[0])

if __name__ == "__main__":
    app.run(debug=True)


































































































