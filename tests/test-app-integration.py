import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_trails_integration(client):
    response = client.get('/trails')
    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200

def test_add_trail_route_integration(client):
    new_trail = {'name': 'New Trail', 'city': 'New City'}

    response = client.post('/trails', json=new_trail)
    data = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 201

