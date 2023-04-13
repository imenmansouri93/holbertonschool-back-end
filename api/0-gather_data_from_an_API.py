#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
import sys

if __name__ == '__main__':
    Id = sys.argv[1]
    playload = {"useId": Id}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(Id)).json()
    list = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=playload).json()
    
    completed = []
    for task in list:
        if task.get("completed") is True:
            completed.append(task.get("title"))
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(list)))
        for complete in completed:
            print("\t {}".format(complete))
