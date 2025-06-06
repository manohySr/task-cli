import json
import os
from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from core.entities.task import Task, TaskStatus


class TaskService:
    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "core", "repositories", "data.json"
        )

    def _ensure_data_file_exists(self):
        """Ensure the data file exists with proper structure"""
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            initial_data = {"tasks": [], "last_id": 0}
            with open(self.file_path, "w") as f:
                json.dump(initial_data, f, indent=2)

    def _load_data(self) -> dict:
        """Load data from JSON file"""
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"tasks": [], "last_id": 0}

    def _save_data(self, data: dict):
        self._ensure_data_file_exists()

        """Save data to JSON file"""
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def _get_next_id(self) -> int:
        """Get the next available task ID"""
        data = self._load_data()
        next_id = data.get("last_id", 0) + 1
        return next_id

    def add_task(self, description: str) -> Task:
        try:
            data = self._load_data()

            # Create new task with next available ID
            new_id = self._get_next_id()
            task = Task(description=description, id=new_id)

            # Add task to the list
            data["tasks"].append(task.model_dump())
            data["last_id"] = new_id

            # Save updated data
            self._save_data(data)

            return task

        except Exception as e:
            raise Exception(f"Error adding task: {str(e)}")

    def update_task(self, task_id: int, new_description: str = None, status: TaskStatus = None) -> Task:
        data = self._load_data()
        tasks = data["tasks"]

        # Find the task
        task_to_update = None
        for task in tasks:
            if task["id"] == task_id:
                task_to_update = task
                break

        if not task_to_update:
            raise ValueError(f"Task with ID {task_id} not found")

        if status:
            if status not in [s.value for s in TaskStatus]:
                raise ValueError(f"Invalid status: {status}")

        # Update the task
        if new_description:
            task_to_update["description"] = new_description
        if status:
            task_to_update["status"] = status.value
        task_to_update["updated_at"] = datetime.now().isoformat()

        # Save updated data
        self._save_data(data)
        return Task(**task_to_update)

    def delete_task(self, task_id: int) -> Task:
        data = self._load_data()
        tasks = data["tasks"]

        # Find and remove the task
        task_to_delete = None
        for task in tasks:
            if task["id"] == task_id:
                task_to_delete = task
                break

        if not task_to_delete:
            raise ValueError(f"Task with ID {task_id} not found")

        tasks.remove(task_to_delete)
        
        # Save updated data
        self._save_data(data)
        return task_to_delete

    def list_tasks(self, status: Optional[TaskStatus] = None):
        data = self._load_data()
        tasks = data["tasks"]

        if status:
            valid_statuses = [s.value for s in TaskStatus]
            if status not in valid_statuses:
                raise ValueError(f"Invalid status: {status}")

            tasks = [task for task in tasks if task["status"] == status]

        return tasks

    def mark_in_progress(self, task_id: int) -> Task:
        return self.update_task(task_id, status=TaskStatus.IN_PROGRESS)

    def mark_done(self, task_id: int) -> Task:
        return self.update_task(task_id, status=TaskStatus.DONE)
