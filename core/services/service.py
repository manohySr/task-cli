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

    def add_task(self, description: str):
        """Write tasks to the JSON file."""
        pass
        

    def update_task(self, task_id: int, new_description: str):
        pass

    def delete_task(self, task_id: int):
        pass

    def list_tasks(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f) 
            tasks = data["tasks"]
        return tasks


    def mark_in_progress(self, task_id: int):
        pass

    def mark_done(self, task_id):
        pass
