import pytest
from db import get_connection, get_cursor
'''
Unit tests for the db
'''

# Unit Test: Database Connection
def test_db_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()

# Unit Test: Get Cursor
def test_get_cursor():
    conn = get_connection()
    cursor = get_cursor(conn)
    assert cursor is not None
    cursor.close()
    conn.close()