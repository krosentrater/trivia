from flask import Blueprint, jsonify
from trivia.services.opentdb_service import fetch_categories

categories_bp = Blueprint('categories', __name__)

@categories_bp.get('/api/categories')
def get_categories():
    try:
        return jsonify(fetch_categories())
    except Exception as e:
        return jsonify({'error': 'failed to fetch categories', 'details': str(e)}), 502