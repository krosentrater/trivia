import pytest
from trivia.services.score_service import add_score, load_scores

# Unit test to ensure score addition works correctly
def test_and_score_creates_entry():
    entry = add_score("Alice", 10)
    assert entry["name"] == "Alice"
    assert entry["score"] == 10

    scores = load_scores()
    assert entry in scores