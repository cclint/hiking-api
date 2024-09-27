import psycopg2

import click
from flask import current_app, g

# connect to postgresql
def get_connection():
    try:
        return psycopg2.connect(
            dbname="hiking_trails",
            user="postgres",
            password="goldie12",
            host="db",
            port="5432"
        )
    except Exception as e:
        print(e)

# Initialize the db with the necessary table
def init_db(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS trails (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, city VARCHAR(255) NOT NULL, description TEXT)")
    conn.commit()

    # with current_app.open_resource('init_db/create_table.sql') as f:
    #     db.executescript(f.read().decode('utf8'))
    print("database initialized")

# create the cursor object (this acts as middleware between postgresql db connection and the query itself.)
# essentially the cursor object is used to send commands to a postgresql db session
def get_cursor(conn):
    return conn.cursor()

def get_all_trails(cursor):
    try:
        cursor.execute("SELECT * FROM trails ORDER BY name")
    except Exception as e:
        print(e)
    return cursor.fetchall()

def add_trail(cursor, new_trail):
    cursor.execute("INSERT INTO trails (name, city, description) VALUES (%s, %s, %s)", (new_trail['name'], new_trail['city'], new_trail['description']))