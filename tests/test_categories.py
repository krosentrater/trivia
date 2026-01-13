import pytest
from trivia.services.opentdb_service import fetch_categories

# Unit test to call service directly and confirms expected data structure
def test_fetch_categories():
    data = fetch_categories()
    assert isinstance(data, dict)
    assert "trivia_categories" in data