#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    api_todo = "https://jsonplaceholder.typicode.com/todos/"
    api_users = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todo = requests.get(api_todo).json()
    user = requests.get(api_users).json()

    tasks = []

    for item in todo:
        if item["userId"] == int(argv[1]):
            task = []
            task.append("{}".format(item["userId"]))
            task.append("{}".format(user["username"]))
            task.append("{}".format(item["completed"]))
            task.append("{}".format(item["title"]))
            tasks.append(task)

    with open('{}.csv'.format(argv[1]), 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        write.writerows(tasks)
