from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), frozen=True)
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def update(self, description: str = "", status: TaskStatus = TaskStatus.TODO):
        if description:
            self.description = description
        if status:
            self.status = status
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return (
            f"Task(id={self.id}, description={self.description}, status={self.status})"
        )

