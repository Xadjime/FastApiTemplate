import os
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, create_engine


class Todo(SQLModel, table=True):
    __tablename__ = 'todo'

    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: bool = Field(default=False)


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1@localhost:5432/postgres")
engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

