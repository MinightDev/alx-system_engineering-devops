#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{user_id}"
    todos_endpoint = f"{base_url}/todos?userId={user_id}"

    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    tasks = []
    for task in todos_data:
        task_data = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        }
        tasks.append(task_data)

    all_employees_data = {}
    all_employees_data[user_id] = tasks

    # Export to JSON
    json_file_name = f"todo_all_employees.json"
    with open(json_file_name, "w") as json_file:
        json.dump(all_employees_data, json_file)
