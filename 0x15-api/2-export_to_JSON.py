#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    api_todo = "https://jsonplaceholder.typicode.com/todos/"
    api_users = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    todo = requests.get(api_todo).json()
    user = requests.get(api_users).json()

    user_dict = {}
    user_list = []

    for item in todo:
        if item["userId"] == int(argv[1]):
            list_dict = {}
            list_dict["task"] = item["title"]
            list_dict["completed"] = item["completed"]
            list_dict["username"] = user["username"]
            user_list.append(list_dict)

    user_dict["{}".format(user['id'])] = user_list

    with open('{}.json'.format(user['id']), 'wt') as f:
        json.dump(user_dict, f)
