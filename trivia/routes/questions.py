from flask import Blueprint, request, jsonify
from trivia.services.opentdb_service import fetch_questions

questions_bp = Blueprint('questions', __name__)

@questions_bp.get('/api/questions')
def get_questions():
    params = {}

    # Validate amount
    amount_raw = request.args.get('amount', '10')
    try:
        amount = int(amount_raw)
        if amount < 1 or amount > 50:
            return jsonify({'error': 'amount must be between 1 and 50'}), 400
    except ValueError:
        return jsonify({'error': 'amount must be an integer'}), 400

    params['amount'] = str(amount)

    for p in ('category', 'difficulty', 'type', 'encode'):
        v = request.args.get(p)
        if v:
            params[p] = v

    try:
        return jsonify(fetch_questions(params))
    except Exception as e:
        return jsonify({'error': 'failed to fetch questions', 'details': str(e)}), 502