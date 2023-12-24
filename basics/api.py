from flask import Flask, jsonify, request


import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password="goldie12",
    host="localhost",
    port="5432"
)

# Create a cursor object
cursor = conn.cursor()


# Route to get all hiking trails
@app.route('/trails', methods=['GET'])
def get_trails():
    cursor.execute("SELECT * FROM trails")
    trails = cursor.fetchall()
    trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2]} for trail in trails]
    return jsonify({'trails': trails_data})

@app.route('/trails', methods=['POST'])
def add_trail():
    new_trail = request.json
    if not new_trail or 'name' not in new_trail or 'city' not in new_trail:
        return jsonify({'error': 'Invalid trail data'}), 400

    cursor.execute("INSERT INTO trails (name, city) VALUES (%s, %s)", (new_trail['name'], new_trail['city']))
    conn.commit()

    return jsonify({'message': 'New Trail Added Successfully', 'trail': new_trail}), 201

if __name__ == '__main__':
    app.run(debug=True)
