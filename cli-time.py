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

















