from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    city: str
    phone_number: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
