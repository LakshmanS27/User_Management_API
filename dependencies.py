from fastapi import Request, HTTPException
from fastapi_limiter.depends import RateLimiter
from redis_config import redis


rate_limit = RateLimiter(times=2, seconds=30)
