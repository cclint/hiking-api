from flask import Flask, jsonify, request, render_template
from db import get_connection, get_cursor, get_all_trails, add_trail, init_db
import psycopg2

app = Flask(__name__)



@app.route('/add') 
def addtrailform():
    return render_template('add.html')

@app.route('/')
@app.route('/trails', methods=['GET'])
def get_trails():
    conn = get_connection()
    print(conn)
    cursor = get_cursor(conn)
    init_db(conn)
    try:
        trails = get_all_trails(cursor)
    except psycopg2.Error as e:
        return "failed"

    trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2], 'description': trail[3]} for trail in trails]
    return render_template('view.html', trails_data=trails_data)
    return "success"

@app.route('/trails', methods=['POST'])
def add_trail_route():
    new_trail = request.form.to_dict()
    if not new_trail or 'name' not in new_trail or 'city' not in new_trail:
        message = "Invalid trail data" 
    else: 
        conn = get_connection()
        cursor = get_cursor(conn)
        add_trail(cursor, new_trail)
        conn.commit()
        message = "Trail Information Added Successfully"
    trails = get_all_trails(cursor)
    trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2], 'description': trail[3]} for trail in trails]
    return render_template('view.html', trails_data=trails_data, message=message)

@app.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')



if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
    #I love comments
