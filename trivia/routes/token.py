import requests
from flask import Blueprint, jsonify, request

token_bp = Blueprint('token', __name__)

@token_bp.get('/api/token')
def get_token():
    print("TOKEN ROUTE LOADED")
    url = "https://opentdb.com/api_token.php?command=request"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['response_code'] == 0:
            return jsonify({'token': data['token']}), 200
        else:
            return jsonify({'error': 'Failed to retrieve token'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500