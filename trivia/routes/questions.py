from flask import Blueprint, request, jsonify
from trivia.services.opentdb_service import fetch_questions

questions_bp = Blueprint('questions', __name__)

@questions_bp.get('/api/questions')
def get_questions():

    params = request.args.to_dict(flat=True) 

    # Validate amount
    amount_raw = params.get('amount', '10')
    try:
        amount = int(amount_raw)
        if amount < 1 or amount > 50:
            return jsonify({'error': 'amount must be between 1 and 50'}), 400
    except ValueError:
        return jsonify({'error': 'amount must be an integer'}), 400

    params['amount'] = str(amount)

    cleaned = {}
    for k, v in params.items():
        if v not in (None, "", "null", "undefined"):
            cleaned[k] = v
    params = cleaned

    try:
        return jsonify(fetch_questions(params))
    except Exception as e:
        return jsonify({'error': 'failed to fetch questions', 'details': str(e)}), 502