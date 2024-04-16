#!/usr/bin/python3
import sys
import requests

def fetching_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Failed to fetch data from the API.")
        return

    todos = response.json()
    if not todos:
        print(f"No TODOs found for employee ID {employee_id}.")
        return

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Failed to fetch user data from the API.")
        return

    user_data = response.json()
    employee_name = user_data.get('name', 'Unknown')

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetching_todo_progress(employee_id)
