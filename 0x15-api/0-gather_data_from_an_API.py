#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


api_todo = "https://jsonplaceholder.typicode.com/todos/"
api_users = "https://jsonplaceholder.typicode.com/users/" + argv[1]
todo = requests.get(api_todo).json()
user = requests.get(api_users).json()

tasks = []
tasks_done = 0
tasks_count = 0

for item in todo:
    if item["userId"] == int(argv[1]):
        if item["completed"]:
            tasks.append(item["title"])
            tasks_done += 1
        tasks_count += 1

print("Employee {} is done with tasks({}/{}):".format(user['name'],
                                                      tasks_done,
                                                      tasks_count))

for task in tasks:
    print("\t " + task)
