#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    response = "https://jsonplaceholder.typicode.com/"
    usrs = requests.get(response + "users").json()

    with open("todo_all_employees.json", "w") as json_:
        json.dump({
            n.get("id"): [{
                "task": j.get("title"),
                "completed": j.get("completed"),
                "username": n.get("username")
            } for j in requests.get(response + "todos",
                                    params={"userId": n.get("id")}).json()]
            for n in usrs}, json_)
