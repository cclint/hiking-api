import pytest
from unittest.mock import MagicMock
from db import get_connection, get_cursor, get_all_trails, add_trail

@pytest.fixture
def mock_psycopg2_connection():
    mock_conn = MagicMock()
    return mock_conn