#!/usr/bin/python3
"""
Script that Fetches user and to-do data from JSONPlaceholder
and creates a JSON file
containing tasks for each user.
"""
import json
import requests


def list_dic():
    """
    Script that Fetches user and to-do data, processes tasks for each user, and
    writes the result to a JSON file.
    """
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(url_users)
    todos_response = requests.get(url_todos)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        users = user_response.json()
        todos = todos_response.json()

        user_dict = {}

        for user in users:
            user_id = str(user.get("id"))
            tasks_list = []

            for todo in todos:
                if todo.get("userId") == user["id"]:
                    task = {
                        "username": user.get("username"),
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                    tasks_list.append(task)

            user_dict[user_id] = tasks_list

        filename_json = "todo_all_employees.json"
        with open(filename_json, "w") as file:
            json.dump(user_dict, file)


if __name__ == "__main__":
    list_dic()
