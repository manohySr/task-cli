from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(BaseModel):
    id: int = Field(default=0)
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __init__(
        self,
        description: str,
        id: Optional[int] = None,
        status: Optional[TaskStatus] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        super().__init__(
            id=id or 0,
            description=description,
            status=status or TaskStatus.TODO,
            created_at=created_at or datetime.now(),
            updated_at=updated_at or datetime.now(),
        )

    def update(self, description: str = "", status: Optional[TaskStatus] = None) -> None:
        """Update task description and/or status"""
        if description:
            self.description = description
        if status:
            self.status = status
        self.updated_at = datetime.now()

    def model_dump(self) -> dict:
        """Convert task to dictionary with serializable datetime"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __str__(self) -> str:
        return f"Task(id={self.id}, description={self.description}, status={self.status})"

