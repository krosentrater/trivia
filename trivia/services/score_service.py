import os
import json
import time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCORES_FILE = os.path.join(BASE_DIR, 'data', 'scores.json')

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_scores(scores):
    try:
        with open(SCORES_FILE, 'w', encoding='utf-8') as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def add_score(name, score):
    scores = load_scores()
    entry = {'name': name, 'score': score, 'time': int(time.time())}
    scores.append(entry)
    save_scores(scores)
    return entry