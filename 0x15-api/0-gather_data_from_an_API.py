#!/usr/bin/python3
"""
Script to gather data from an API
"""

import requests
import sys

def gather_data(employee_id):
    """
    Gather data from the API for a given employee ID
    """
    # API URL for employee data
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    # Fetching user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetching TODO list data
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Display information
    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
