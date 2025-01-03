import motor.motor_asyncio
from typing import Optional, Union, Annotated
from Rapid import (Rapid, RapidCRUDRouter, MongoModel, MongoObjectId, ObjectId)

# Database connection using motor
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/local")

# store the database in a global variable
db = client.local


class UserModel(MongoModel):
    id: Annotated[ObjectId, MongoObjectId] | None = None
    name: str
    email: str
    password: str


# Model Out -> Schema
class UserModelOut(MongoModel):
    id: str
    name: str
    email: str

users_router = RapidCRUDRouter(
    model=UserModel,
    model_out=UserModelOut,
    db=db,
    collection_name="users",
    prefix="/users",
    tags=["users"],
)

app = Rapid()
app.include_router(users_router)