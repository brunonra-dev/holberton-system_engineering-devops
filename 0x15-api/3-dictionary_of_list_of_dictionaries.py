#!/usr/bin/python3
"""Export to JSON"""
import json
import requests

if __name__ == '__main__':
    api_todo = "https://jsonplaceholder.typicode.com/todos/"
    api_users = "https://jsonplaceholder.typicode.com/users/"
    todo = requests.get(api_todo).json()
    users = requests.get(api_users).json()

    all_todo = {}
    for user in users:
        user_list = []
        for item in todo:
            if item["userId"] == user["id"]:
                list_dict = {}
                list_dict["username"] = user["username"]
                list_dict["task"] = item["title"]
                list_dict["completed"] = item["completed"]
                user_list.append(list_dict)

        all_todo["{}".format(user['id'])] = user_list

    with open('todo_all_employees.json', 'wt') as f:
        json.dump(all_todo, f)
