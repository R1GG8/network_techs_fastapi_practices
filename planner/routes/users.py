from fastapi import APIRouter, HTTPException, status
from models.users import NewUser, UserSignIn

user_router = APIRouter(tags=["User"])

# Временная база данных пользователей в памяти
users = {}


@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с такой почтой уже существует (Галлямов Ришат)",
        )
    users[data.email] = data
    return {"message": "Пользователь успешно зарегистрирован (Галлямов Ришат)!"}


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден (Галлямов Ришат)",
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Неверные учетные данные (Галлямов Ришат)",
        )
    return {"message": "Успешный вход в систему (Галлямов Ришат)"}
