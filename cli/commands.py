import typer
from typing import Optional


class TaskManager:
    def __init__(self):
        self.app = typer.Typer(help="Task Tracker CLI - Manage your tasks efficiently")
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
            typer.echo(f"Adding task: {description}")

        @self.app.command()
        def update(task_id: str, new_description: str):
            """
            Update a task's description.

            TASK_ID: The ID of the task to update.
            NEW_DESCRIPTION: The new description for the task.
            """
            typer.echo(f"Updating task {task_id} to: {new_description}")

        @self.app.command()
        def delete(task_id: str):
            """Delete a task by its ID"""
            typer.echo(f"Deleting task: {task_id}")

        @self.app.command(name="list")
        def list_tasks():
            """List all tasks"""
            typer.echo("Listing all tasks...")

        @self.app.command()
        def mark_in_progress(task_id: str):
            """
            Mark a task as in progress.

            TASK_ID: The ID of the task to mark as in progress.
            """
            typer.echo(f"Marking task {task_id} as in progress")

        @self.app.command()
        def mark_done(task_id: str):
            """
            Mark a task as done.

            TASK_ID: The ID of the task to mark as done.
            """
            typer.echo(f"Marking task {task_id} as done")

    def run(self):
        self.app()


# Create a singleton instance
task_manager = TaskManager()
app = task_manager.app
