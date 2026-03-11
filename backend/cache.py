# backend/cache.py

import aioredis
import json
from functools import wraps
from backend.config import settings

redis = aioredis.from_url(settings.redis_url)

async def get_cache(key: str):
    value = await redis.get(key)
    if value is not None:
        return json.loads(value)
    return None

async def set_cache(key: str, value: any, ttl: int):
    await redis.set(key, json.dumps(value), ex=ttl)

async def delete_cache(key: str):
    await redis.delete(key)

async def invalidate_cache_key(key_prefix: str):
    keys = await redis.keys(f"{key_prefix}*")
    if keys:
        await redis.delete(*keys)

def cache_result(ttl: int):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_result = await get_cache(cache_key)
            if cached_result is not None:
                return cached_result
            result = await func(*args, **kwargs)
            await set_cache(cache_key, result, ttl)
            return result
        return wrapper
    return decorator