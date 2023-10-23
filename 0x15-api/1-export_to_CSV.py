#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    usrId = sys.argv[1]
    response = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(response + "users/{}".format(usrId)).json()
    usrname = usr.get("username")
    todos = requests.get(response + "todos", params={"userId": usrId}).json()

    with open("{}.csv".format(usrId), "w", newline="") as csv_:
        wt = csv.writer(csv_, quoting=csv.QUOTE_ALL)
        [wt.writerow(
            [usrId, usrname, n.get("completed"), n.get("title")]
        ) for n in todos]
