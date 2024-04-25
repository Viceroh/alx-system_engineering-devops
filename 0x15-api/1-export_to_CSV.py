#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    user_name = user.json()["username"]
    todos_text = todos.json()
    print(dir(csv.writer))
    with open("{}.csv".format(argv[1]), "w") as f:
        writer = csv.writer(
            f, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos_text:
            writer.writerow(
                [argv[1], user_name, todo["completed"], todo["title"]])
