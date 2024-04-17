#!/usr/bin/python3
"""Gather data from an API for a given employee
ID and display TO-DO list progress."""
import csv
import requests
import sys


def to_do(employee_ID):
    """
    Retrieving employee information and TO-DO
    list progress based on the employee ID.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if employee_response.status_code == 200:
        employee_name = employee_data.get('username')

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    if todos_response.status_code == 200:
        total_tasks = len(todos_data)
        completed_tasks = 0
    for task in todos_data:
        completed_tasks += task['completed']

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))

    for task in todos_data:
        if task['completed']:
            print("\t {}".format(task['title']))

    csv_filename = f"{employee_ID}.csv"
    with open(csv_filename, mode='w') as file:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(file,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_ID,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
            })

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
