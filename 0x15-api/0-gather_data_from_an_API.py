#!/usr/bin/python3
"""returns information about employee todo list progress"""
import requests
import sys

if __name__ == "__main__":
    response = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(response + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(response + "todos",
                         params={"userId": sys.argv[1]}).json()

    completed = [n.get("title") for n in todos if n.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(completed), len(todos)))
    [print("\t {}".format(i)) for i in completed]
