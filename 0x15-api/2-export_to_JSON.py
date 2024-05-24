#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    user_name = user.json()["username"]
    todos_data = todos.json()
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user_name})
    with open("{}.json".format(argv[1]), "w") as f:
        obj = {argv[1]: tasks}
        json.dump(obj, f)
