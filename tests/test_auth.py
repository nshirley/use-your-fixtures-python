from api.routes import ROUTES
import requests

BASE_URL = 'http://127.0.0.1:5000'

# With fixtures.
# You'll notice, this is a case where using the fixture doesn't
# add much value. The test is simple enough that it doesn't need it
# However, by using the fixtures we maintain the pattern and,
# should we need to change anything with the base `unauthorized_session`
# we'll update _all_ at once.


def test_auth_rejects_without_username_password_with_fixture(unauthorized_session):
    expected_response = {"error": "bad request",
                         "details": "username and password are required"}
    response = unauthorized_session.post(f'{BASE_URL}{ROUTES.AUTH}', json={})
    assert response.status_code == 400
    assert response.json() == expected_response


def test_auth_rejects_with_incorrect_username_password_with_fixture(unauthorized_session):
    expected_response = {"error": "unauthorized"}
    response = unauthorized_session.post(f'{BASE_URL}{ROUTES.AUTH}', json={
                                         'username': 'user', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert response.json() == expected_response


# Without fixtures.
def test_auth_rejects_without_username_password_without_fixture():
    expected_response = {"error": "bad request",
                         "details": "username and password are required"}
    response = requests.post(f'{BASE_URL}{ROUTES.AUTH}', json={})
    assert response.status_code == 400
    assert response.json() == expected_response


def test_auth_rejects_with_incorrect_username_password_without_fixture():
    expected_response = {"error": "unauthorized"}
    response = requests.post(f'{BASE_URL}{ROUTES.AUTH}', json={'username':
                                                               'user', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert response.json() == expected_response
