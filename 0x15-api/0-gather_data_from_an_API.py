#!/usr/bin/python3
"""Gather data from an API"""
from re import I
import requests
from sys import argv


api_todo = "https://jsonplaceholder.typicode.com/todos/"
api_users = "https://jsonplaceholder.typicode.com/users/" + argv[1]
todo = requests.get(api_todo).json()
user = requests.get(api_users).json()

tasks = []
tasksdone = 0

for item in todo:
    if item["userId"] == int(argv[1]):
        tasks.append(item["title"])
        if item["completed"]:
            tasksdone += 1

print("Employee {} is done with tasks({}/{}):"
      .format(user['name'], tasksdone, len(tasks)))

for task in tasks:
    print("\t " + task)
