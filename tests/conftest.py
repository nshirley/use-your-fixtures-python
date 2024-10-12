# tests/conftest.py

import pytest
import requests

@pytest.fixture(scope="session")
def auth_token():
    # Fetch the auth token once per test session
    print('Fixture fetching auth token...')
    response = requests.post('http://127.0.0.1:5000/auth', json={'username': 'user', 'password': 'p@ssw0rd'})
    return response.json().get('access_token')

@pytest.fixture
def authorized_session(auth_token):
    # Create a session and attach the token automatically
    print('Making an authorized session...')
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {auth_token}'})
    return session