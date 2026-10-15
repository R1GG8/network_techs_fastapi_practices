from typing import List, Optional
from models.events import Event
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str
    username: Optional[str] = None
    events: Optional[List[Event]] = []

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "Галлямов Ришат",
                "password": "strong!!!",
                "events": [],
            }
        }


# Модель для регистрации нового пользователя
class NewUser(User):
    pass


# Модель для входа пользователя
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }
