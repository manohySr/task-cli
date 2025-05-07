
from core.entities.task import Task, TaskStatus
from datetime import datetime

def test_create_task_defaults():
    task = Task(description="Test Task")
    assert task.description == "Test Task"
    assert task.status == TaskStatus.TODO
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)
    assert isinstance(task.id, str)

def test_update_task_description():
    task = Task(description="Initial")
    task.update(description="Updated")
    assert task.description == "Updated"
    assert task.updated_at > task.created_at

def test_update_task_status():
    task = Task(description="Word")
    task.update(status=TaskStatus.DONE)
    assert task.status == TaskStatus.DONE