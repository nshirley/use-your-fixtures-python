from flask import Flask, request, jsonify, abort

from api.routes import ROUTES

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Jones"}
]

# error handlers


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "unauthorized"}), 401


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "bad request", "details": error.description}), 400

# before hook for authorization


@app.before_request
def check_authorization():
    if request.path not in [ROUTES.AUTH, ROUTES.HEALTH]:
        auth_header = request.headers.get('Authorization')
        if not auth_header or auth_header != 'Bearer super_secret_token':
            abort(401)

# Routes


@app.route(ROUTES.AUTH, methods=['POST'])
def auth():
    data = request.get_json()
    if not data and 'username' not in data or 'password' not in data:
        abort(400, description='username and password are required')
    if data['username'] != 'user' or data['password'] != 'p@ssw0rd':
        abort(401)
    return jsonify({"access_token": "super_secret_token"})


@app.route(ROUTES.USERS, methods=['GET'])
def users():
    user_id = request.args.get('id')
    if user_id:
        user = next(
            (user for user in USERS if user['id'] == int(user_id)), None)
        if not user:
            abort(404)
        return jsonify(user)

    # yes, we wouldn't normally return all users like this
    return jsonify(USERS)


@app.route(ROUTES.HEALTH, methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True)
