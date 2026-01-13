import pytest
from trivia.services.opentdb_service import fetch_questions

# Unit test to ensure amount parameter works correctly
def test_fetch_questions_default_amount():
    params = {'amount': 5}
    data = fetch_questions(params)

    assert isinstance(data, dict)
    assert "results" in data
    assert len(data["results"]) == 5