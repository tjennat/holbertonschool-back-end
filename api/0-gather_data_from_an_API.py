#!/usr/bin/python3
"""Gathering data from an API"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetching employee data"""
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee = employee_response.json()

    """Fetching TODOs for the employee"""
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos = todos_response.json()

    """Calculating  progress"""
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    
    """Displaying progress"""
    print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [EMPLOYEE_ID]")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
