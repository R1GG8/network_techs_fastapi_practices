from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPI Book Launch (Галлямов Ришат)",
                "image": "https://linktomyimage.com/image.png",
                "description": "Обсуждение материалов книги по FastAPI.",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }
