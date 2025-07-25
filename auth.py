from functools import wraps
from flask import request, jsonify

API_USERNAME = "user"
API_PASSWORD = "password"

def api_authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == API_USERNAME and auth.password == API_PASSWORD):
            return jsonify({"message": "Authentication required"}), 401
        return func(*args, **kwargs)
    return decorated
