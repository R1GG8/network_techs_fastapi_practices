from database.connection import conn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.events import event_router
from routes.users import user_router
import uvicorn

app = FastAPI(title="Event Planner (SQLite + SQLModel) — Галлямов Ришат")

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()  # Создает planner.db и таблицу event при старте


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
