from typing import List
from database.connection import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from models.events import Event, EventUpdate
from sqlmodel import Session, select

event_router = APIRouter(tags=["Events"])


# 1. Создание события в БД (POST)
@event_router.post("/new")
async def create_event(
    new_event: Event, session: Session = Depends(get_session)
) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": f"Событие с ID {new_event.id} успешно сохранено в БД SQLite (Галлямов Ришат)"
    }


# 2. Получение всех событий из БД (GET)
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(
    session: Session = Depends(get_session),
) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


# 3. Получение события по ID из БД (GET)
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session: Session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с указанным ID не найдено в БД (Галлямов Ришат)",
    )


# 4. Обновление события в БД (PUT)
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(
    id: int, new_data: EventUpdate, session: Session = Depends(get_session)
) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено для обновления (Галлямов Ришат)",
        )

    # Исключаем поля, которые клиент не прислал
    event_data = new_data.dict(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)
    return event


# 5. Удаление события из БД (DELETE)
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session: Session = Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено для удаления (Галлямов Ришат)",
        )
    session.delete(event)
    session.commit()
    return {"message": "Событие успешно удалено из БД SQLite (Галлямов Ришат)"}
