#!/usr/bin/python3
"""exports information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    response = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(response + "users/{}".format(user_id)).json()
    usrname = usr.get("username")
    todos = requests.get(response + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": usrname
            } for t in todos]}, jsonfile)
