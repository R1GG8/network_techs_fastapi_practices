from models.events import Event
from sqlmodel import Session, SQLModel, create_engine

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"

# check_same_thread: False необходим для работы SQLite в асинхронном FastAPI
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string, echo=True, connect_args=connect_args
)


def conn():
    """Создает таблицы в БД при запуске"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """Генератор сессий для внедрения зависимостей в маршрутах"""
    with Session(engine_url) as session:
        yield session
