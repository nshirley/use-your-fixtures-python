import requests
from api.routes import ROUTES

BASE_URL = 'http://127.0.0.1:5000'

# With fixtures.


def test_get_users_returns_all_users_with_fixture(authorized_session):
    response = authorized_session.get(f'{BASE_URL}{ROUTES.USERS}')
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 1


def test_get_users_returns_user_by_id_with_fixture(authorized_session):
    response = authorized_session.get(f'{BASE_URL}{ROUTES.USERS}?id=1')
    assert response.status_code == 200
    user = response.json()
    assert user['name'] == 'John Doe'

# Without fixtures.


def test_get_users_returns_all_users_without_fixture():
    auth_response = requests.post(f'{BASE_URL}{ROUTES.AUTH}', json={
                                  'username': 'user', 'password': 'p@ssw0rd'})
    assert auth_response.status_code == 200
    auth_token = auth_response.json().get('access_token')
    response = requests.get(f'{BASE_URL}{ROUTES.USERS}', headers={
                            'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 1


def test_get_users_returns_user_by_id_without_fixture():
    auth_response = requests.post(f'{BASE_URL}{ROUTES.AUTH}', json={
                                  'username': 'user', 'password': 'p@ssw0rd'})
    assert auth_response.status_code == 200
    auth_token = auth_response.json().get('access_token')
    response = requests.get(f'{BASE_URL}{ROUTES.USERS}?id=1', headers={
                            'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    user = response.json()
    assert user['name'] == 'John Doe'
