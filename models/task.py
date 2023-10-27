import uuid
from uuid import UUID
from datetime import datetime

class Task:
    def __init__(self, title: str, description: str) -> None:
        self.id: UUID = uuid.uuid4()  # Generate a unique id
        self.title: str = title
        self.description: str = description
        self.is_completed: bool = False
        self.created_at: datetime = datetime.now()

    def complete(self) -> None:
        self.is_completed = True

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title={self.title}, description={self.description}, is_completed={self.is_completed}, created_at={self.created_at})"
