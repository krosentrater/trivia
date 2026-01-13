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
    key = 'q:' + '&'.join(f"{k}={params[k]}" for k in sorted(params))
    cached = cache_get(key)
    if cached:
        return cached

    url = 'https://opentdb.com/api.php'
    r = requests.get(url, params=params, timeout=7)
    r.raise_for_status()
    data = r.json()

    if 'results' in data:
        for item in data['results']:
            for k, v in list(item.items()):
                if isinstance(v, str):
                    item[k] = html.unescape(v)
                elif isinstance(v, list):
                    item[k] = [html.unescape(x) if isinstance(x, str) else x for x in v]

    cache_set(key, data, ttl=60 * 5)
    return data
    