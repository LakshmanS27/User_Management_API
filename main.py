from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, Base, get_db
from redis_config import init_redis, redis_client
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import json


app = FastAPI(title="User Management API")

# Create tables
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    r = await init_redis()
    await FastAPILimiter.init(r)

@app.post("/users/", response_model=schemas.UserResponse, dependencies=[Depends(RateLimiter(times=2, seconds=60))])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(db=db, user=user)

    # Cache the new user in Redis for 60 seconds
    await redis_client.set(
        f"user:{new_user.id}",
        json.dumps(schemas.UserResponse.from_orm(new_user).dict()),
        ex=60
    )

    return new_user

@app.get("/users/{user_id}", response_model=schemas.UserResponse, dependencies=[Depends(RateLimiter(times=2, seconds=60))])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    # Check Redis cache
    cached = await redis_client.get(f"user:{user_id}")
    if cached:
        print("Data from Redis Cached")
        return schemas.UserResponse(**json.loads(cached))

    db_user = crud.get_user(db, user_id=user_id)
    print("Data from Database")
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Cache result for 60 seconds
    await redis_client.set(f"user:{user_id}", json.dumps(schemas.UserResponse.from_orm(db_user).dict()), ex=60)
    return db_user

@app.delete("/users/{user_id}", response_model=dict, dependencies=[Depends(RateLimiter(times=2, seconds=60))])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    # Remove from Redis cache
    await redis_client.delete(f"user:{user_id}")
    return {"detail": "User deleted"}
