#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

# Constants
TASKS_FILE = "tasks.json"
VALID_STATUSES = ["todo", "in-progress", "done"]

def load_tasks():
    """
    Load tasks from the JSON file or create a new file if it doesn't exist.
    """
    if not os.path.exists(TASKS_FILE):
        return {"tasks": []}

    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.DecodeError:
        print(f"Error: {TASKS_FILE} is corrupted. Creating a new tasks file.")
        return {"tasks": []}

def save_tasks(tasks_data):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks_data, file, indent=2)

def generate_id(tasks):
    """Generate a new unique ID for a task"""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(description):
    """Add a new task to the tasks list."""
    tasks_data = load_tasks()
    task_id = generate_id(tasks_data["tasks"])

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created-at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated-at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks_data["tasks"].append(new_task)
    save_tasks(tasks_data)
    print(f"Task added successfully with ID: {task_id}")

def update_task(task_id, description=None, status=None):
    """Update an existing task's description or status."""
    tasks_data = load_tasks()

    # Convert task_id to integer
    task_id = int(task_id)

    for task in tasks_data["tasks"]:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            if status:
                if status not in VALID_STATUSES:
                    print(f"Error: Invalid status. Must be one of {VALID_STATUSES}")
                    return
                task["status"] = status
            task["updated-at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_tasks(task_data)
            print(f"Task {task_id} updated successfully")
        return
    
    print(f"Error: Task with ID {task_id} not found")

def delete_task(task_id):
    """delete a task by it's ID."""
    tasks_data = load_tasks()

    # Convert task_id to integer
    task_id = int(task_id)

    initial_count = len(tasks_data["tasks"])
    tasks_data["tasks"] = [task for task in tasks_data["tasks"] if task["id"] != task_id]

    if len(tasks_data["tasks"]) < initial_count:
        save_tasks(tasks_data)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Error: Task ID {task id} not found")


def list_tasks(status_filter=None):
    """List tasks with optional status filtering."""
    tasks_data = load_tasks()

    if not tasks_data["tasks"]:
        print("No tasks found")
        return

    filtered_tasks = tasks_data["tasks"]
    if status_filter:
        if status_filter not in VALID_STATUSES and status_filter != "not_done":
            print(f"Error: Invalid status filter. Must be one of {VALID_STATUSES} or 'not-done'")
            return

        if status_filter == "not-done":
            filtered_tasks = [task for task in tasks_data["tasks"] if task["status"] == status_filter]
        else:
            filtered_tasks = [task for task in tasks_data["tasks"] if task["status"] == status_filter]

    if not filtered_tasks:
        status_msg = f" with status '{status_filter}'" if status_filter else ""
        print(f"No tasks found {status_msg}")
        return
    
    print(f"{'ID':<5} {'Status':<12} {'Description': <50} {'Updated At':<20}")


def print_help():
    """Print help information"""
    print("Task Tracker - A CLI application to manage your tasks")
    print("\nUsage:")
    print("  python task_tracker.py <command> [arguments]")
    print("\nCommands:")
    print("  add <description>              - Add a new task")
    print("  update <id> [description] [status] - Update a task's description or status")
    print("  delete <id>                    - Delete a task")
    print("  list                           - List all tasks")
    print("  list done                      - List all completed tasks")
    print("  list todo                      - List all todo tasks")
    print("  list in_progress               - List all in progress tasks")
    print("  list not_done                  - List all tasks that are not done")
    print("  help                           - Show this help")
    print("\nStatus values:")
    print("  todo, in_progress, done")


def main():
    """
    Main function to handle CLI arguments and
    execute appropriate actions.
    """
    if len(sys.argv) < 2 or sys.argv[1] == 'help':
        print_help()
        return

    command = sys.argv[1].lower()
    try:
        if command == "add" and len(sys.argv) >= 3:
            add_task(" ".join(sys.argv[2:]))
        elif command == "update" and len(sys.argv) >= 3:
            task_id = sys.argv[2]
            description = None
            status = None

            # Check for description and status in arguments
            if len(sys.argv) >= 4:
                # Check if the 4th argument is a valid status
                if sys.argv[-1] in VALID_STATUSES:
                    status = sys.argv[-1]
                    if len(sys.argv) > 4:
                    # If there are more arguments assume it's the description
                        description = " ".join(sys.argv[3:-1])
                else:
                    description = " ".join(sys.argv[3:])

                update_task(task_id, description, status)
            elif command == "delete" and len(sys.argv) == 3:
                delete_task(sys.argv[2])

            elif command == "list":
                if sys.argv < 2:
                    list_tasks()
                elif 




















































































































