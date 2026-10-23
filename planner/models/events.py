from typing import List, Optional
from sqlmodel import JSON, Column, Field, SQLModel


# Таблица событий в БД
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Meetup (Галлямов Ришат)",
                "image": "https://linktomyimage.com/image.png",
                "description": "Обсуждение практической работы №8",
                "tags": ["python", "fastapi", "sqlmodel"],
                "location": "Google Meet",
            }
        }


# Модель для частичного обновления (все поля опциональны)
class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Обновленный митап (Галлямов Ришат)",
                "location": "Офис / Hybrid",
            }
        }
