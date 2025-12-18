import redis.asyncio as redis

REDIS_URL = "redis://localhost:6379"

redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

async def init_redis():
    await redis_client.ping()
    return redis_client
