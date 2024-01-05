from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# get database credentials from environment variables
db_name = os.getenv('DB_NAME', 'hiking_trails')
db_user = os.getenv('DB_USER', 'clint')
db_password = os.getenv('DB_PASSWORD', 'goldie12')
db_host = os.getenv('DB_HOST', 'db')
db_port = os.getenv('DB_PORT', '5432')

# connect to PostgreSQL using environment variables
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object
cursor = conn.cursor()

# Initialize the trails table (execute this in the PostgreSQL console)
# CREATE TABLE trails (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     city VARCHAR(100)
# );

# Route to get ALL hiking trails
@app.route('/trails', methods=['GET'])
def get_trails():
    cursor.execute("SELECT * FROM trails")
    trails = cursor.fetchall()
    trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2]} for trail in trails]
    return jsonify({'trails': trails_data})

@app.route('/trail', methods=['POST'])
def add_trail():
    new_trail = request.json
    if not new_trail or 'name' not in new_trail or 'city' not in new_trail:
        return jsonify({'error': 'Invalid trail data'}), 400
    
    cursor.execute("INSERT INTO trails (name, city) VALUES (%s, %s)", (new_trail['name'], new_trail['city']))
    conn.commit()

    return jsonify({'message': 'New Trail Added Successfully', 'trail': new_trail}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
