import psycopg2

# connect to postgresql
def get_connection():
    return psycopg2.connect(
        dbname="test",
        user="postgres",
        password="goldie12",
        host="localhost",
        port="5432"
    )

# create the cursor object (this acts as middleware between postgresql db connection and the query itself.)
# essentially the cursor object is used to send commands to a postgresql db session
def get_cursor(conn):
    return conn.cursor()

def get_all_trails(cursor):
    cursor.execute("SELECT * FROM trails")
    return cursor.fetchall()

def add_trail(cursor, new_trail):
    cursor.execute("INSERT INTO trails (name, city) VALUES (%s, %s)", (new_trail['name'], new_trail['city']))