# Task Tracker CLI

A simple and efficient command-line task management tool to help you organize your tasks. This project is based on the [Task Tracker CLI project](https://roadmap.sh/projects/task-tracker) from roadmap.sh.

## Features

- ✨ Add, update, and delete tasks
- 📋 List all tasks with optional status filtering
- 🔄 Track task status (todo, in-progress, done)
- 🎯 Simple and intuitive CLI interface
- 💾 Persistent storage of tasks

## Installation

### Quick Install (For Users)
```bash
pip install git+https://github.com/manohySr/task-cli.git
```

### Development Setup (For Contributors)
1. Clone the repository:
   ```bash
   git clone https://github.com/manohySr/task-cli.git
   cd task-cli
   ```

2. Install the package and its dependencies:
   ```bash
   # Install all required dependencies
   pip install -r requirements.txt
   
   # Install the package in development mode
   pip install -e .
   ```

## Usage

### Basic Commands

```bash
# Add a new task
task-cli add "Complete project documentation"

# List all tasks
task-cli list

# List tasks by status
task-cli list --status todo
task-cli list --status in-progress
task-cli list --status done

# Update a task
task-cli update 1 "Updated task description"

# Mark a task as in progress
task-cli mark-in-progress 1

# Mark a task as done
task-cli mark-done 1

# Delete a task
task-cli delete 1
```

### Task Status

Tasks can have one of the following statuses:
- `todo`: New tasks (default)
- `in-progress`: Tasks currently being worked on
- `done`: Completed tasks

## Development

### Project Structure

```bash
https://gitingest.com/manohySr/task-cli
```
