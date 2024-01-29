#!/usr/bin/python3
"""
Script to export data to CSV format
"""

import requests
import csv
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

    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            csv_writer.writerow([user_data['id'], user_data['username'], str(task['completed']), task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
