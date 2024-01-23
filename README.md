# Building a Hiking Trails API with Flask

## Overview
This documentation provides guidelines and steps to build a RESTful API using Flask to manage hiking trails data. The API allows users to retrieve existing trails and add new trail entries.

## Prerequisites
- Python installed on your system
- Understanding of Python programming
- Basic knowledge of PostgreSQL and databases

## Installation

### 1. Install Flask

```bash
pip install Flask
```

### 2. Install psycopg2 for PostgreSQL connection

```bash
pip install psycopg2-binary
```

## Setting Up the Database

- Create a PostgreSQL database named `test`.
- Create a table named `trails` with columns: `id` (SERIAL), `name` (VARCHAR), `city` (VARCHAR), `description` (TEXT).

## Usage

1. Import necessary modules:

    ```python
    from flask import Flask, jsonify, request
    import psycopg2
    ```

2. Initialize Flask app and establish PostgreSQL connection:

    ```python
    app = Flask(__name__)
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="your_password",
        host="localhost",
        port="5432"
    )
    ```

3. Create routes to manage trails:

    - **GET /trails:** Retrieve all hiking trails.
    - **POST /trails:** Add a new hiking trail.

4. Example code snippet for retrieving trails:

    ```python
    @app.route('/trails', methods=['GET'])
    def get_trails():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trails")
        trails = cursor.fetchall()
        trails_data = [{'id': trail[0], 'name': trail[1], 'city': trail[2]} for trail in trails]
        return jsonify({'trails': trails_data})
    ```

5. Example code snippet for adding a new trail:

    ```python
    @app.route('/trails', methods=['POST'])
    def add_trail():
        new_trail = request.json
        if not new_trail or 'name' not in new_trail or 'city' not in new_trail:
            return jsonify({'error': 'Invalid trail data'}), 400
        cursor = conn.cursor()
        cursor.execute("INSERT INTO trails (name, city) VALUES (%s, %s)", (new_trail['name'], new_trail['city']))
        conn.commit()
        return jsonify({'message': 'New Trail Added Successfully', 'trail': new_trail}), 201
    ```

6. Run the Flask application:

    ```python
    if __name__ == '__main__':
        app.run(debug=True)
    ```

## Testing

- Use tools like Postman or write Python scripts to test API endpoints by sending GET and POST requests to retrieve and add trails.

## Security Considerations

- Implement authentication mechanisms to secure API endpoints and control access.
- Ensure proper error handling to handle failed requests and validation errors.
