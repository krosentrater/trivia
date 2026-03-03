import requests
import html
from .cache_service import cache_get, cache_set

def fetch_categories():
     
	cached = cache_get('categories')
	if cached:
		return cached

	url = 'https://opentdb.com/api_category.php'

	r = requests.get(url, timeout=5)
	r.raise_for_status()
	data = r.json()
	cache_set('categories', data, ttl=60 * 60 * 12)
	return data

def fetch_questions(params):

    params = dict(params)

    if params.get("token") in (None, "", "null", "undefined"):
        params.pop("token", None)

    if "token" in params:
         return _fetch_questions_no_cache(params)
    
    key = 'q:' + '&'.join(f"{k}={params[k]}" for k in sorted(params))
    cached = cache_get(key)
    if cached:
        return cached
    
    data = _fetch_questions_no_cache(params)
    cache_set(key, data, ttl=60 * 60 * 12)

    return data

def _fetch_questions_no_cache(params):
    url = 'https://opentdb.com/api.php'
    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()
    data = r.json()

    if data.get("response_code") != 0:
         print("OPENTDB API error:", data)
         return data

    if 'results' in data:
        for q in data['results']:
            q['question'] = html.unescape(q['question'])
            q['correct_answer'] = html.unescape(q['correct_answer'])
            q['incorrect_answers'] = [html.unescape(ans) for ans in q['incorrect_answers']]
    
    return data