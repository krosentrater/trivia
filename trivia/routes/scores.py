from flask import Blueprint, request, jsonify
from trivia.services.score_service import load_scores, add_score

scores_bp = Blueprint('scores', __name__)

@scores_bp.post('/api/score')
def post_score():
    data = request.get_json() or {}
    name = data.get('name') or 'anonymous'
    score = data.get('score')

    if score is None:
        return jsonify({'error': 'score is required'}), 400

    entry = add_score(name, score)
    return jsonify({'status': 'ok', 'entry': entry}), 201


@scores_bp.get('/api/scores')
def get_scores():
    scores = load_scores()
    scores_sorted = sorted(scores, key=lambda s: s.get('score', 0), reverse=True)
    return jsonify({'scores': scores_sorted[:50]})