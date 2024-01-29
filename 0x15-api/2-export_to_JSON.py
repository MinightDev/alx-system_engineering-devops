#!/usr/bin/python3
"""
Script to export data to JSON format
"""

import requests
import json
import sys

def gather_data(employee_id):
    """
    Gather data from the API for a given employee ID
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    user_response = requests.get(user_url)
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    json_filename = f'{employee_id}.json'
    json_data = {str(employee_id): []}

    for task in todo_data:
        json_data[str(employee_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
