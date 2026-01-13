import time
import threading

# Simple in-memory TTL cache
_cache = {}
_cache_lock = threading.Lock()

def cache_set(key, value, ttl=300):
	with _cache_lock:
		_cache[key] = (value, time.time() + ttl)

def cache_get(key):
	with _cache_lock:
		item = _cache.get(key)
		if not item:
			return None
		value, expires = item
		if time.time() > expires:
			del _cache[key]
			return None
		return value