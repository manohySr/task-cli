import typer
from typing import Optional
from core.services.service import TaskService
from core.entities.task import TaskStatus


class TaskManager:
    def __init__(self):
        self.app = typer.Typer(help="Task Tracker CLI - Manage your tasks efficiently")
        self.task_service = TaskService()
        self._setup_commands()

    def _setup_commands(self):
        @self.app.command(name="hello")
        def hello():
            """Say hello to the world"""
            typer.echo("Hello World!")

        @self.app.command()
        def add(description: str):
            """
            Add a new task.

            DESCRIPTION: The description of the task to add.
            """
            task = self.task_service.add_task(description)
            typer.echo(f"Task added successfully (ID: {task.id})")

        @self.app.command()
        def update(task_id: int, new_description: str):
            """
            Update a task's description.

            TASK_ID: The ID of the task to update.
            NEW_DESCRIPTION: The new description for the task.
            """

            task = self.task_service.update_task(task_id, new_description)
            typer.echo(f"✅ Updated task")

        @self.app.command()
        def delete(task_id: int):
            """
            Delete a task by its ID.

            TASK_ID: The ID of the task to delete.
            """
            try:    
                deleted_task = self.task_service.delete_task(task_id)
                typer.echo(f"✅ Deleted task: {deleted_task['description']}")
            except ValueError as e:
                typer.echo(f"❌ {e}")

        @self.app.command(name="list")
        def list_tasks(status: str = typer.Option(None)):
            """List all tasks"""
            try:
                tasks = self.task_service.list_tasks(status)
            except ValueError as e:
                typer.echo(f"❌ {e}")
                typer.echo(f"Use one of the following: {', '.join([s.value for s in TaskStatus])}")
                return

            typer.echo(f"\n📋 Task List:")
            # Print the header
            print(f"\t{'ID':<5} {'Description':<20} {'Status':<15}")
            print("\t" + "-" * 50)  # Separator line

            # Print each task in a formatted way
            for task in tasks:
                print(
                    f"\t{task['id']:<5} {task['description']:<20} {task['status']:<15}"
                )

        @self.app.command()
        def mark_in_progress(task_id: int):
            """
            Mark a task as in progress.

            TASK_ID: The ID of the task to mark as in progress.
            """
            task = self.task_service.mark_in_progress(task_id)
            typer.echo("\n📋 Task in progress...")

        @self.app.command()
        def mark_done(task_id: int):
            """
            Mark a task as done.

            TASK_ID: The ID of the task to mark as done.
            """
            task = self.task_service.mark_done(task_id)
            typer.echo("\n📋 Task done!")

    def run(self):
        self.app()


# Create a singleton instance
task_manager = TaskManager()
app = task_manager.app
