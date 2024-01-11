from flask import Flask, jsonify, request, render_template
from db import get_connection, get_cursor, get_all_trails, add_trail

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/trails', methods=['GET'])
def get_trails():
    conn = get_connection()
    cursor = get_cursor(conn)
    trails = get_all_trails(cursor)
    trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2]} for trail in trails]
    return jsonify({'trails': trails_data})

@app.route('/trails', methods=['POST'])
def add_trail_route():
    new_trail = request.json
    if not new_trail or 'name' not in new_trail or 'city' not in new_trail:
        return jsonify({'error': 'Invalid trail data'}), 400
    
    conn = get_connection()
    cursor = get_cursor(conn)
    add_trail(cursor, new_trail)
    conn.commit()

    return jsonify({'message': 'New Trail Added Successfully', 'trail': new_trail}), 201

if __name__ == '__main__':
    app.run(debug=True)