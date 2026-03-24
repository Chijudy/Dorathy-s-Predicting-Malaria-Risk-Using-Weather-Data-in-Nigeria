from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Create router
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Pydantic model for User
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory "database" for demo purposes
fake_users_db: List[User] = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com")
]

# GET all users
@router.get("/", response_model=List[User])
async def get_users():
    return fake_users_db

# GET single user by id
@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# POST a new user
@router.post("/", response_model=User)
async def create_user(user: User):
    fake_users_db.append(user)
    return user

# DELETE a user
@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            fake_users_db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")