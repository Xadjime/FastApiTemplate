from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, create_engine


class Todo(SQLModel, table=True):
    __tablename__ = 'todo'
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: bool = Field(default=False)


url = 'postgresql://postgres:1@localhost:5432/postgres'
engine = create_engine(url)
SQLModel.metadata.create_all(engine)


