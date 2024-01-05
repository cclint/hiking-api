import pytest
from db import get_connection, get_cursor, add_trail

'''
integration tests for db
'''

def test_add_trail():
    conn = get_connection()
    cursor = conn.cursor()

    # Add a trail for testing
    cursor.execute("CREATE TABLE IF NOT EXISTS trails (id SERIAL PRIMARY KEY, name VARCHAR(255), city VARCHAR(255))")
    cursor.execute("INSERT INTO trails (name, city) VALUES ('Test Trail', 'Test City')")
    conn.commit()

    new_trail = {'name': 'New Trail', 'city': 'New City'}
    add_trail(cursor, new_trail)

    cursor.execute("SELECT * FROM trails WHERE name = 'New Trail'")
    result = cursor.fetchone()
    assert result is not None

    # Clean up: Remove the added trail used for testing
    cursor.execute("DELETE FROM trails WHERE name = 'New Trail'")
    conn.commit()

    cursor.close()
    conn.close()
